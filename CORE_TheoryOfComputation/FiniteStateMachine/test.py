import unittest
from typing import List, Set, Callable
from CORE_TheoryOfComputation.FiniteStateMachine.FiniteStateMachine import FiniteStateMachine, FSMRunner


def generate_inputs(alphabet: Set[str],
                    callback: Callable[[str], None],
                    length_limit: int,
                    current: str = "") -> None:
    """
    Recursively generate all the possible inputs given a specific alphabet and a length limit.
    :param alphabet: The list of characters we have to play with
    :param callback: Called with all the inputs as they are generated
    :param length_limit: The longest inputs to generate, gives us the exit condition for recursion
    :param current: The current accumulated input
    """
    for a in alphabet:
        next_input: str = "{}{}".format(current, a)
        callback(next_input)
        if len(next_input) < length_limit:
            generate_inputs(alphabet, callback, length_limit, next_input)


class Test(unittest.TestCase):

    def test_generate_inputs(self):
        my_inputs: List[str] = []
        generate_inputs({"0", "1"}, lambda x: my_inputs.append(x), 3)
        print("Inputs Generated: {}".format(my_inputs))

    def test_1(self):
        alphabet: Set[str] = {"0", "1"}
        fsm: FiniteStateMachine = FiniteStateMachine(
            start_state="q0",
            all_states={"q0", "q1"},
            valid_end_states={"q1"},
            alphabet=alphabet)\
            .with_transition("q0", "0", "q0")\
            .with_transition("q0", "1", "q1")\
            .with_transition("q1", "0", "q1")\
            .with_transition("q1", "1", "q1")

        my_inputs: List[str] = []
        generate_inputs(alphabet, lambda x: my_inputs.append(x), 3)

        for my_input in my_inputs:
            is_valid: bool = fsm.process(my_input)
            # This state machine should end in a valid state if any '1's were seen in the input
            self.assertEqual("1" in my_input, is_valid)

    def test_2(self):
        alphabet: Set[str] = {"a", "b"}
        fsm: FiniteStateMachine = FiniteStateMachine(
            start_state="p",
            all_states={"p", "q", "r", "s"},
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
        generate_inputs(alphabet, lambda x: my_inputs.append(x), 3)

        for my_input in my_inputs:
            is_valid: bool = fsm.process(my_input)
            print("Input {}, valid? {}".format(my_input, is_valid))