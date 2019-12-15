#!/usr/bin/python3
#coding: utf8
from math import ceil

HALT = 99
ADD = 1
MUL = 2

class IntcodeHalt(Exception):
    pass

class IntcodeEngine:
    POSITION_MODE = 0
    IMMEDIATE_MODE = 1

    HALT = 99
    ADD = 1
    MUL = 2
    INPUT = 3
    OUTPUT = 4

    def __init__(self, filename):
        self.memory = []
        self.pointer = 0
        with open(filename) as f:
            self.memory = [int(x) for x in f.readline().split(',')]

    def get_memory_value(self, index, default=0):
        try:
            return self.memory[index]
        except IndexError:
            return default

    def get_pointer_value(self, index, default=0):
        return self.get_memory_value(self.get_memory_value(index), default)

    def set_memory_value(self, index, value):
        self.memory[index] = value
        return value

    def output(self, opcode):
        self.pointer += 1
        value = self.get_parameter_value(opcode, 0)
        print("output :",value)

    def input(self, opcode):
        self.pointer += 1
        while True:
            try:
                self.set_memory_value(self.get_memory_value(self.pointer), int(input('Input:')))
            except ValueError:
                print("Erroneous value, please retry")
            else:
                break

    def add(self, opcode):
        self.pointer += 1
        n1 = self.get_parameter_value(opcode, 0)
        n2 = self.get_parameter_value(opcode, 1)
        self.pointer += 2
        pos = self.get_memory_value(self.pointer)
        self.set_memory_value(pos, n1+n2)

    def mul(self, opcode):
        self.pointer += 1
        n1 = self.get_parameter_value(opcode, 0)
        n2 = self.get_parameter_value(opcode, 1)
        self.pointer += 2
        pos = self.get_memory_value(self.pointer)
        self.set_memory_value(pos, n1*n2)

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
        return value

    def run(self):
        operations = {
            IntcodeEngine.ADD: self.add,
            IntcodeEngine.MUL: self.mul,
            IntcodeEngine.HALT: self.halt,
            IntcodeEngine.INPUT: self.input,
            IntcodeEngine.OUTPUT: self.output
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
                print("program halt")
                break
            self.pointer += 1

if __name__ == '__main__':
    engine = IntcodeEngine('input')
    engine.run()
