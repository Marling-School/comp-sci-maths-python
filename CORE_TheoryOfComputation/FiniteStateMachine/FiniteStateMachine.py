from __future__ import annotations
from typing import Set, Dict


class FSMRunner:
    """
    An instance of this class is created to process an input with a given state machine.
    It tracks the state as input is processed.
    """
    __machine: FiniteStateMachine  # The machine that governs our behaviour
    __state: str  # The current state of this instance

    def __init__(self, machine: FiniteStateMachine):
        self.__machine = machine;
        self.__state = machine.get_start_state()

    def process(self, input_str: str) -> bool:
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


class FiniteStateMachine:
    """
    Encapsulates the rules of a given state machine. Once the rules are established
    machine runners can be created to process inputs.
    """
    __start_state: str  # the start state of a new instance of the machine
    __all_states: Set[str]  # All the known states for the machine
    __valid_end_states: Set[str]  # All the valid end states for the machine
    __alphabet: Set[str]  # The set of know input characters

    # The registry of all the transition rules, keyed by start state, sub key by input char
    __transitions: Dict[str, Dict[str, str]]

    def __init__(self,
                 start_state: str,
                 all_states: Set[str],
                 valid_end_states: Set[str],
                 alphabet: Set[str]):
        # Validate that the start state is within the known states
        if start_state not in all_states:
            raise Exception("Start state not included in all states")

        # Validate that the end states are a subset of all the known states
        if not valid_end_states.issubset(all_states):
            raise Exception("Valid end states {} is not a subset of all states {}".format(
                valid_end_states,
                all_states
            ))

        # Remember all the rules for this FSM
        self.__start_state = start_state
        self.__all_states = all_states
        self.__valid_end_states = valid_end_states
        self.__alphabet = alphabet
        self.__transitions = dict()

    def with_transition(self,
                        start_state: str,
                        input_char: str,
                        end_state: str) -> FiniteStateMachine:
        """
        Register transition rules with this Finite State Machine.
        All of the rules should be registered before runners are created and used.
        :param start_state: The start state for the transition being defined
        :param input_char: The alphabet character to look for
        :param end_state: The end state for the transition being defined
        :return: Instance of self, so we can use method chaining
        """
        # Validate the start and end states against the list of known states
        if not {start_state, end_state}.issubset(self.__all_states):
            raise Exception("One of states {}, {} not in set of known states {}".format(
                start_state,
                end_state,
                self.__all_states
            ))
        # Validate the input character against the alphabet
        if input_char not in self.__alphabet:
            raise Exception("Input Char {} not in alphabet {}".format(
                input_char,
                self.__alphabet
            ))
        # Create storage for transitions from this state if it doesn't already exist
        if start_state not in self.__transitions:
            self.__transitions[start_state] = dict()

        # Retrieve the transition rules for this start state
        transitions: Dict[str] = self.__transitions[start_state]

        # Validate that we do not already have a rule defined for this input char
        if input_char in transitions:
            raise Exception("Transition already defined for state {} alphabet {}, it is {}".format(
                start_state,
                input_char,
                transitions[input_char]
            ))

        # Register the end state for this combination
        transitions[input_char] = end_state

        return self

    def get_start_state(self) -> str:
        """
        Getter for the start state of any new instance of the machine
        :return: The start state
        """
        return self.__start_state

    def get_next_state(self, start_state: str, input_char: str) -> str:
        """
        Given a start state and input character, this calculates the next state.

        :param start_state: The starting state for this transition
        :param input_char: The character to process
        :return: The next state from the machine
        :raise Exception:
            If the start state is not in list of known states
            If the input_char is not in the alphabet
            If there are no transitions defined for this start_state
            If there is no transition defined for this specific start_state/input_char combination
        """
        # Validate the start state is within all the known states
        if start_state not in self.__all_states:
            raise Exception("State {} not in list of known states {}".format(
                start_state,
                self.__all_states
            ))

        # Validate that the input character is within the alphabet
        if input_char not in self.__alphabet:
            raise Exception("Input Character {} not in alphabet {}".format(
                input_char,
                self.__alphabet
            ))

        # Validate that we have transitions defined for this start state
        if start_state not in self.__transitions:
            raise Exception("No transitions defined for {}".format(start_state))

        # Locate those transitions
        transitions: Dict[str] = self.__transitions[start_state]

        # Validate that we have a transition rule defined for this specific input char
        if input_char not in transitions:
            raise Exception("No transition defined for {} with character {}".format(
                start_state,
                input_char
            ))

        # Return the new state
        return transitions[input_char]

    def is_state_valid(self, state: str):
        """
        Validate a state against the list of valid end states.
        :param state: The state to validate
        :return: Boolean to indicate if the given state is in the valid list
        :raise Exception: If the state given is not even in the list of known states
        """
        if state not in self.__all_states:
            raise Exception("State for validating {} is not even in the known list of states {}".format(
                state,
                self.__all_states))
        return state in self.__valid_end_states

    def create_instance(self) -> FSMRunner:
        """
        Create a runner for a finite state machine, a runner should be created for each input that needs processing.
        This FSM class itself acts as a template for runners.
        :return: New instance of FSM Runner
        """
        return FSMRunner(self)

    def process(self, input_str: str) -> bool:
        """
        convenience function to create a new instance and process in one go
        :param input_str: The input to process
        :return: If the input left the FSM in a valid state
        """
        return FSMRunner(self).process(input_str)
