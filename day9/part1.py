#!/usr/bin/python3
#coding: utf8
from math import ceil
from itertools import permutations, cycle

class IntcodeHalt(Exception):
    pass

class IntcodeContinue(Exception):
    pass

class IntcodeError(Exception):
    pass

class IntcodeOutput(Exception):
    pass

class IntcodeEngine:
    POSITION_MODE = 0
    IMMEDIATE_MODE = 1
    RELATIVE_MODE = 2

    HALT = 99
    ADD = 1
    MUL = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    ADJUST_REL_BASE = 9

    def __init__(self, filename, interactive=True):
        self.memory = {}
        self.awaiting_inputs = []
        self.awaiting_outputs = []
        self.pointer = 0
        self.is_halted = False
        self.relative_base = 0
        self.interactive = interactive
        with open(filename) as f:
            self.memory = {k: int(x) for k, x in enumerate(f.readline().split(','))}

    def get_memory_value(self, index, default=0):
        return self.memory.get(index, default)

    def get_pointer_value(self, index, default=0):
        return self.get_memory_value(self.get_memory_value(index), default)

    def set_memory_value(self, index, value):
        self.memory[index] = value
        return value

    def add(self, opcode):
        self.pointer += 1
        n1 = self.get_parameter_value(opcode, 0)
        n2 = self.get_parameter_value(opcode, 1)
        pos = self.get_relative_pointer(opcode, 2)
        self.set_memory_value(pos, n1+n2)
        self.pointer += 2

    def mul(self, opcode):
        self.pointer += 1
        n1 = self.get_parameter_value(opcode, 0)
        n2 = self.get_parameter_value(opcode, 1)
        pos = self.get_relative_pointer(opcode, 2)
        self.set_memory_value(pos, n1*n2)
        self.pointer += 2

    def input(self, opcode):
        self.pointer += 1
        value = self.get_input()
        pos = self.get_relative_pointer(opcode, 0)
        self.set_memory_value(pos, value)

    def add_input(self, value):
        self.awaiting_inputs.append(value)
        return self

    def get_input(self):
        if not self.awaiting_inputs:
            if not self.interactive:
                raise IntcodeError("Not enough inputs")
            while True:
                try:
                    self.awaiting_inputs.append(int(input('Input:')))
                except ValueError:
                    print("Erroneous value, please retry")
                else:
                    break
        return self.awaiting_inputs.pop(0)

    def get_output(self):
        if not self.awaiting_outputs:
            return 0
        return self.awaiting_outputs.pop(0)

    def output(self, opcode):
        self.pointer += 1
        value = self.get_parameter_value(opcode, 0)
        #print("output :",value)
        self.awaiting_outputs.append(value)
        raise IntcodeOutput()

    def jump_if_true(self, opcode):
        self.pointer += 1
        if not self.get_parameter_value(opcode, 0):
            self.pointer += 1
            return
        self.pointer = self.get_parameter_value(opcode, 1)
        raise IntcodeContinue()

    def jump_if_false(self, opcode):
        self.pointer += 1
        if self.get_parameter_value(opcode, 0):
            self.pointer += 1
            return
        self.pointer = self.get_parameter_value(opcode, 1)
        raise IntcodeContinue()

    def less_than(self, opcode):
        self.pointer += 1
        n1 = self.get_parameter_value(opcode, 0)
        n2 = self.get_parameter_value(opcode, 1)
        pos = self.get_relative_pointer(opcode, 2)
        self.set_memory_value(pos, int(n1 < n2))
        self.pointer += 2

    def equals(self, opcode):
        self.pointer += 1
        n1 = self.get_parameter_value(opcode, 0)
        n2 = self.get_parameter_value(opcode, 1)
        pos = self.get_relative_pointer(opcode, 2)
        self.set_memory_value(pos, int(n1 == n2))
        self.pointer += 2

    def adjust_relative_base(self, opcode):
        self.pointer += 1
        self.relative_base += self.get_parameter_value(opcode, 0)

    def halt(self, opcode):
        raise IntcodeHalt()

    def get_parameter_mode(self, opcode, index):
        n = 10**(2+index)
        return int(opcode%(n*10)/n)

    def get_parameter_value(self, opcode, index, default=0):
        mode = self.get_parameter_mode(opcode, index)
        value = self.get_memory_value(self.pointer+index, default=default)
        if mode == IntcodeEngine.POSITION_MODE:
            return self.get_memory_value(value, default=default)
        elif mode == IntcodeEngine.RELATIVE_MODE:
            return self.get_memory_value(value+self.relative_base, default=default)
        return value

    def get_relative_pointer(self, opcode, index=0):
        mode = self.get_parameter_mode(opcode, index)
        relative_add = self.relative_base*(mode == IntcodeEngine.RELATIVE_MODE)
        return self.get_memory_value(self.pointer+index) + relative_add

    def run(self):
        operations = {
            IntcodeEngine.ADD: self.add,
            IntcodeEngine.MUL: self.mul,
            IntcodeEngine.HALT: self.halt,
            IntcodeEngine.INPUT: self.input,
            IntcodeEngine.OUTPUT: self.output,
            IntcodeEngine.JUMP_IF_TRUE: self.jump_if_true,
            IntcodeEngine.JUMP_IF_FALSE: self.jump_if_false,
            IntcodeEngine.LESS_THAN: self.less_than,
            IntcodeEngine.EQUALS: self.equals,
            IntcodeEngine.ADJUST_REL_BASE: self.adjust_relative_base
        }

        while self.pointer < len(self.memory):
            opcode = self.memory[self.pointer]
            try:
                operations[opcode%100](opcode)
            except KeyError:
                print("unknown opcode : ", opcode)
                print(self.memory)
                break
            except IntcodeHalt:
                break
            except IntcodeOutput:
                self.pointer += 1
                return
            except IntcodeContinue:
                continue
            self.pointer += 1
        self.is_halted = True

if __name__ == '__main__':
    engine = IntcodeEngine('input')
    while not engine.is_halted:
        engine.run()
        print(engine.get_output())
