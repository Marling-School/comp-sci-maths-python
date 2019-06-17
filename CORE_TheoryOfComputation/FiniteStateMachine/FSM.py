from typing import Generic, Iterable
from CORE_TheoryOfComputation.FiniteStateMachine.FSMConfig import FSMConfig, Alphabet, State


class FSM(Generic[State, Alphabet]):
    """
    An instance of this class is created to process an input with a given state machine.
    It tracks the state as input is processed.
    """
    __machine: FSMConfig[State, Alphabet]  # The machine that governs our behaviour
    __state: State  # The current state of this instance

    def __init__(self, machine: FSMConfig[State, Alphabet]):
        self.__machine = machine;
        self.__state = machine.get_start_state()

    def process(self, input_str: Iterable[Alphabet]) -> bool:
        """
        Given an input, it puts each character through the machine,
        iterating the state according to the transition rules.
        This function can be called repeatedly, which should allow it to work with streaming inputs.
        :param input_str: The next portion of the input string
        :return: Returns bool to indicate if the state at the end of this input is still valid.
        """
        for c in input_str:
            self.__state = self.__machine.get_next_state(self.__state, c)

        return self.is_state_valid()

    def get_state(self) -> str:
        return self.__state

    def is_state_valid(self) -> bool:
        return self.__machine.is_state_valid(self.__state)

