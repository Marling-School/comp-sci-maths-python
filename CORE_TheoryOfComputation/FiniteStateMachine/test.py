import unittest
from typing import List, Set
from CORE_TheoryOfComputation.FiniteStateMachine.FSMConfig import FSMConfig
from CORE_TheoryOfComputation.FiniteStateMachine.FSM import FSM
from CORE_TheoryOfComputation.FiniteStateMachine.MealyMachine import MealyMachine
from CORE_TheoryOfComputation.generate_permutations import generate_permutations


class Test(unittest.TestCase):

    def test_fsm_1(self):
        # Build the Finite State Machine using rules
        all_states: Set[str] = {"q0", "q1"}
        alphabet: Set[str] = {"0", "1"}
        fsm: FSMConfig = FSMConfig(
            start_state="q0",
            all_states=all_states,
            valid_end_states={"q1"},
            alphabet=alphabet)\
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
            is_valid: bool = FSM(fsm).process(my_input)
            # This state machine should end in a valid state if any '1's were seen in the input
            self.assertEqual("1" in my_input, is_valid)

    def test_fsm_2(self):
        # Build the Finite State Machine using rules
        all_states: Set[str] = {"p", "q", "r", "s"}
        alphabet: Set[str] = {"a", "b"}
        fsm: FSMConfig[str, str] = FSMConfig[str, str](
            start_state="p",
            all_states=all_states,
            valid_end_states={"s"},
            alphabet=alphabet)\
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
            is_valid: bool = FSM(fsm).process(my_input)
            print("Input {}, valid? {}".format(my_input, is_valid))

    def test_mealy_machine_1(self):
        # Build the Finite State Machine using rules
        all_states: Set[str] = {"s0", "s1", "s2"}
        alphabet: Set[str] = {"0", "1"}
        fsm: FSMConfig[str, str] = FSMConfig[str, str](
            start_state="s0",
            all_states=all_states,
            alphabet=alphabet)\
            .with_transition("s0", "0", "s2", "0")\
            .with_transition("s0", "1", "s1", "0")\
            .with_transition("s1", "0", "s2", "1")\
            .with_transition("s1", "1", "s1", "1")\
            .with_transition("s2", "0", "s2", "0")\
            .with_transition("s2", "1", "s1", "0")

        print("Mealy Machine FSM: {}".format(fsm))

        for an_input, expected_output in [("00110", "00011"), ("01010101", "00101010")]:
            an_output: List[str] = []
            MealyMachine(fsm, lambda x: an_output.append(x)).process(an_input)
            an_output_str: str = "".join(an_output)
            print("{} -> {}".format(an_input, an_output_str))
            self.assertEqual(expected_output, an_output_str)
        print("Done")
