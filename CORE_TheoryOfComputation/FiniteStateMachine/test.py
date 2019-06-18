import unittest
from typing import List, Set, Tuple, Optional
from CORE_TheoryOfComputation.FiniteStateMachine.FSMConfig import FSMConfig
from CORE_TheoryOfComputation.FiniteStateMachine.FSM import FSM
from CORE_TheoryOfComputation.FiniteStateMachine.MealyMachine import MealyMachine
from CORE_TheoryOfComputation.FiniteStateMachine.TuringMachine import TuringMachine, TuringTransition, Direction
from CORE_TheoryOfComputation.generate_permutations import generate_permutations
from CORE_TheoryOfComputation.FiniteStateMachine.parse_turing_machine import parse_turing_machine


class TestFiniteStateMachines(unittest.TestCase):

    def test_fsm_1(self):
        # Build the Finite State Machine using rules
        all_states: Set[str] = {"q0", "q1"}
        alphabet: Set[str] = {"0", "1"}
        fsm: FSMConfig[str, str, None] = FSMConfig[str, str, None](
            start_state="q0",
            all_states=all_states,
            valid_end_states={"q1"},
            alphabet=alphabet,
            is_deterministic=True)\
            .with_transition("q0", "0", "q0")\
            .with_transition("q0", "1", "q1")\
            .with_transition("q1", "0", "q1")\
            .with_transition("q1", "1", "q1")

        # Generate a list of inputs that contain every combination of 1 and 0 up to length of 3 digits
        my_inputs: List[str] = []
        generate_permutations(alphabet, lambda x: my_inputs.append(x), 3)

        # Work through each input, check the response from the machine
        # This FSM just requires a 1 anywhere in the input
        for my_input in my_inputs:
            machine: FSM = FSM(fsm)
            is_valid: bool = machine.process(my_input)
            # This state machine should end in a valid state if any '1's were seen in the input
            self.assertEqual("1" in my_input, is_valid)

    def test_fsm_2(self):
        # Build the Finite State Machine using rules
        all_states: Set[str] = {"p", "q", "r", "s"}
        alphabet: Set[str] = {"a", "b"}
        fsm: FSMConfig[str, str, None] = FSMConfig[str, str, None](
            start_state="p",
            all_states=all_states,
            valid_end_states={"s"},
            alphabet=alphabet,
            is_deterministic=True)\
            .with_transition("p", "a", "s")\
            .with_transition("p", "b", "q")\
            .with_transition("q", "a", "s")\
            .with_transition("q", "b", "r")\
            .with_transition("r", "a", "r")\
            .with_transition("r", "b", "r")\
            .with_transition("s", "a", "s")\
            .with_transition("s", "b", "s")

        my_inputs: List[str] = []
        generate_permutations(alphabet, lambda x: my_inputs.append(x), 3)

        for my_input in my_inputs:
            machine: FSM = FSM(fsm)
            is_valid: bool = machine.process(my_input)
            print("Input {}, valid? {}".format(my_input, is_valid))

    def test_mealy_machine_1(self):
        # Build the Finite State Machine using rules
        all_states: Set[str] = {"s0", "s1", "s2"}
        alphabet: Set[str] = {"0", "1"}
        fsm: FSMConfig[str, str, str] = FSMConfig[str, str, str](
            start_state="s0",
            all_states=all_states,
            alphabet=alphabet,
            is_deterministic=True)\
            .with_transition("s0", "0", "s2", "0")\
            .with_transition("s0", "1", "s1", "0")\
            .with_transition("s1", "0", "s2", "1")\
            .with_transition("s1", "1", "s1", "1")\
            .with_transition("s2", "0", "s2", "0")\
            .with_transition("s2", "1", "s1", "0")

        print("Mealy Machine FSM: {}".format(fsm))

        test_cases: List[Tuple[str, str]] = [
            ("00110", "00011"),
            ("01010101", "00101010")
        ]
        for an_input, expected_output in test_cases:
            an_output: List[str] = []
            machine: MealyMachine = MealyMachine(fsm, lambda x: an_output.append(x))
            machine.process(an_input)
            an_output_str: str = "".join(an_output)
            print("{} -> {}".format(an_input, an_output_str))
            self.assertEqual(expected_output, an_output_str)
        print("Done")

    def test_turing_machine_1(self):
        """
        Even number of zeros
        """
        all_states: Set[str] = {"q0", "q1", "qAccept"}
        alphabet: Set[str] = {None, "0", "1"}
        fsm: FSMConfig[str, str, TuringTransition] = FSMConfig[str, str, TuringTransition](
            start_state="q0",
            all_states=all_states,
            valid_end_states={"qAccept"},
            alphabet=alphabet,
            is_deterministic=False)\
            .with_transition("q0", "0", "q1", ("0", Direction.MOVE_RIGHT))\
            .with_transition("q1", "0", "q0", ("0", Direction.MOVE_RIGHT))\
            .with_transition("q0", "1", "q0", ("1", Direction.MOVE_RIGHT))\
            .with_transition("q1", "1", "q1", ("1", Direction.MOVE_RIGHT))\
            .with_transition("q0", None, "qAccept", (None, Direction.NO_MOVE))

        print("Turing Machine to Check Even Number of Zeros")
        test_cases: List[Tuple[str, bool]] = [
            ("0001", False),
            ("00001", True),
            ("01010001", False),
            ("001010", True)
        ]
        for an_input, expected_output in test_cases:
            an_input_list = [c for c in an_input]
            machine: TuringMachine = TuringMachine(fsm, an_input_list)
            an_output, is_valid, num_steps = machine.process(callback=lambda x: print(x))
            an_output_str: str = "".join([c for c in an_output if c is not None])
            print("Test Input {}, expected {}, received ({}, {}), steps: {}".format(
                an_input, expected_output, an_output_str, is_valid, num_steps
            ))
            self.assertEqual(expected_output, is_valid)

    def test_turing_machine_2(self):
        """
        Divisible by 3
        """
        all_states: Set[str] = {"q0", "q1", "q2", "qAccept"}
        alphabet: Set[str] = {None, "0", "1"}
        fsm: FSMConfig[str, str, TuringTransition] = FSMConfig[str, str, TuringTransition](
            start_state="q0",
            all_states=all_states,
            valid_end_states={"qAccept"},
            alphabet=alphabet,
            is_deterministic=False)\
            .with_transition("q0", "0", "q0", ("0", Direction.MOVE_RIGHT))\
            .with_transition("q0", "1", "q1", ("1", Direction.MOVE_RIGHT))\
            .with_transition("q1", "0", "q2", ("0", Direction.MOVE_RIGHT))\
            .with_transition("q1", "1", "q0", ("1", Direction.MOVE_RIGHT))\
            .with_transition("q2", "0", "q1", ("0", Direction.MOVE_RIGHT))\
            .with_transition("q2", "1", "q2", ("1", Direction.MOVE_RIGHT))\
            .with_transition("q0", None, "qAccept", (None, Direction.NO_MOVE))

        print("Turing Machine to Check Number Divisible By 3")
        test_cases: List[Tuple[str, bool]] = [
            ("001", False),
            ("011", True),
            ("100101", False),
            ("101101", True)
        ]
        for an_input, expected_output in test_cases:
            an_input_list = [c for c in an_input]
            machine: TuringMachine = TuringMachine(fsm, an_input_list)
            an_output, is_valid, num_steps = machine.process(callback=lambda x: print(x))
            an_output_str: str = "".join([c for c in an_output if c is not None])
            print("Test Input {}, expected {}, received ({}, {}), steps: {}".format(
                an_input, expected_output, an_output_str, is_valid, num_steps
            ))
            self.assertEqual(expected_output, is_valid)

    def test_turing_machine_parsed(self):
        fsm: Optional[FSMConfig] = None
        with open("./turing_machines/decimal_to_binary.txt") as f:
            fsm = parse_turing_machine(list(f))

        print("Turing Machine to Convert Decimal to Binary")
        print(fsm)
        test_cases: List[Tuple[str, bool]] = [
            ("45", True),
        ]
        for an_input, expected_output in test_cases:
            an_input_list = [c for c in an_input]
            machine: TuringMachine = TuringMachine(fsm, an_input_list)
            an_output, is_valid, num_steps = machine.process(callback=lambda x: print(x))
            an_output_str: str = "".join([c for c in an_output if c is not None])
            print("Test Input {}, expected {}, received ({}, {}), steps: {}".format(
                an_input, expected_output, an_output_str, is_valid, num_steps
            ))
            self.assertEqual(expected_output, is_valid)
