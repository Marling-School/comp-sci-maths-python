from typing import Dict, List
from enum import Enum


class StatusRegister(Enum):
    EQ = 0
    NE = 1
    LT = 2
    GT = 3


class Computer:
    DEFAULT_MEMORY_CONTENTS: int = 0
    """
    Simulates the data stored within a computer.
    Can be used to simulate AQA assembler instructions
    """
    __memory: Dict[int, int]
    __cpu_registers: Dict[str, int]
    __status_registers: List[bool]

    def __init__(self):
        self.__memory = dict()
        self.__cpu_registers = dict()
        self.__status_registers = [False for s in StatusRegister]

    def __repr__(self):
        as_str: str = "Computer\n"

        as_str += "Memory\n"
        mem_keys: List[int] = list(self.__memory.keys())
        mem_keys.sort()
        for mem_location in mem_keys:
            as_str += "\t{:02X}: {:02X}\n".format(
                mem_location, self.__memory[mem_location])

        as_str += "Registers\n"
        reg_keys: List[str] = list(self.__cpu_registers.keys())
        reg_keys.sort()
        for register in reg_keys:
            as_str += "\t{}: {:02X}\n".format(
                register, self.__cpu_registers[register])

        as_str += "Status\n"
        for status in StatusRegister:
            as_str += "\t{}: {}\n".format(
                status.name, self.__status_registers[status.value])

        return as_str

    def execute_instruction(self, instruction: str) -> bool:
        """
        Given an instruction in AQA Assembler, this function parses the opcode and operands and
        runs the instruction.
        :param instruction: The instruction in AQA Assembler
        :return boolean to indicate to continue, the HALT command will cause this to return False
        """
        parts: List[str] = instruction.split(" ")

        return False

    def get_memory(self, location: int) -> int:
        """
        Retrieve the contents of a memory cell
        :param location: The location to retrieve
        :return: The contents of that location, or 0 (zero) by default
        """
        return Computer.DEFAULT_MEMORY_CONTENTS \
            if location not in self.__memory \
            else self.__memory.get(location)

    def set_memory(self, location: int, contents: int) -> None:
        """
        Set the value of a memory location
        :param location: The location to set
        :param contents: The new contents
        """
        self.__memory[location] = contents

    def get_register(self, register: str) -> int:
        """
        Retrieve the contents of the register
        :param register: The register to retrieve
        :return: The contents of that register, or 0 (zero) by default
        """
        return Computer.DEFAULT_MEMORY_CONTENTS \
            if register not in self.__cpu_registers \
            else self.__cpu_registers[register]

    def set_register(self, register: str, contents: int) -> None:
        """
        Set the value of the named register
        :param register: The register to set
        :param contents: The new contents
        """
        self.__cpu_registers[register] = contents

    def get_status(self, register: StatusRegister) -> bool:
        """
        Retrieve the value of a status register
        :param register: The register to retrieve
        :return: The value of that register
        """
        return self.__status_registers[register.value]

    def set_status(self, register: StatusRegister, value: bool) -> None:
        """
        Set the value of the status register
        :param register: The status register to set
        :param value: The new value
        """
        self.__status_registers[register.value] = value
