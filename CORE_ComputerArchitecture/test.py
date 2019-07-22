from unittest import TestCase
from CORE_ComputerArchitecture.Computer import Computer, StatusRegister


class TestComputer(TestCase):
    def test_direct(self) -> None:
        """
        Test directly setting memory and registers on the CPU and printing them
        """
        computer: Computer = Computer()
        computer.set_memory(0, 5)
        computer.set_memory(1, 90)
        computer.set_memory(2, 43)
        computer.set_memory(4, 78)
        computer.set_register('R1', 45)
        computer.set_register('R2', 78)
        computer.set_status(StatusRegister.EQ, True)
        print(computer)

        check_mem_2: int = computer.get_memory(2)
        check_reg_2: int = computer.get_register('R2')
        check_status: bool = computer.get_status(StatusRegister.EQ)
        self.assertEqual(43, check_mem_2)
        self.assertEqual(78, check_reg_2)
        self.assertTrue(check_status)