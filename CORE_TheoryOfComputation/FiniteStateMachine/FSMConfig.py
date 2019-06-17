from __future__ import annotations
from typing import Set, Dict, Generic, TypeVar, Tuple, Optional

State = TypeVar('State')
Alphabet = TypeVar('Alphabet')


class FSMConfig(Generic[State, Alphabet]):
    """
    Encapsulates the rules of a given state machine. Once the rules are established
    machine runners can be created to process inputs.
    """
    __start_state: State  # the start state of a new instance of the machine
    __all_states: Set[State]  # All the known states for the machine
    __valid_end_states: Set[State]  # All the valid end states for the machine
    __alphabet: Set[Alphabet]  # The set of know input characters

    # The registry of all the transition rules, keyed by start state, sub key by input char
    __transitions: Dict[State, Dict[Alphabet, Tuple[State, Alphabet]]]

    def __init__(self,
                 start_state: State,
                 all_states: Set[State],
                 alphabet: Set[Alphabet],
                 valid_end_states=None):
        # Validate that the start state is within the known states
        if start_state not in all_states:
            raise Exception("Start state not included in all states")

        # Validate that the end states are a subset of all the known states
        if valid_end_states is None:
            valid_end_states = set()
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

    def __repr__(self):
        return "FSM - States: {}, Start: {}, Valid Ends: {}, Alphabet: {}, Transitions: {}".format(
            self.__all_states,
            self.__start_state,
            self.__valid_end_states,
            self.__alphabet,
            self.__transitions
        )

    def with_transition(self,
                        start_state: State,
                        input_char: Alphabet,
                        end_state: State,
                        output_char: Optional[Alphabet] = None) -> FSMConfig:
        """
        Register transition rules with this Finite State Machine.
        All of the rules should be registered before runners are created and used.
        :param start_state: The start state for the transition being defined
        :param input_char: The alphabet character to look for
        :param end_state: The end state for the transition being defined
        :param output_char: Optional output character to spit out for this transition, used for mealy machines
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
        transitions: Dict[Alphabet] = self.__transitions[start_state]

        # Validate that we do not already have a rule defined for this input char
        if input_char in transitions:
            raise Exception("Transition already defined for state {} alphabet {}, it is {}".format(
                start_state,
                input_char,
                transitions[input_char]
            ))

        # Register the end state for this combination
        transitions[input_char] = (end_state, output_char)

        return self

    def get_start_state(self) -> str:
        """
        Getter for the start state of any new instance of the machine
        :return: The start state
        """
        return self.__start_state

    def get_next_tuple(self, start_state: State, input_char: Alphabet) -> Tuple[State, Alphabet]:
        """
        Given a start state and input character, this calculates the next tuple from our state transitions.

        :param start_state: The starting state for this transition
        :param input_char: The character to process
        :return: The tuple containing the next state and next output value
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
        transitions: Dict[State, Tuple[State, Alphabet]] = self.__transitions[start_state]

        # Validate that we have a transition rule defined for this specific input char
        if input_char not in transitions:
            raise Exception("No transition defined for {} with character {}".format(
                start_state,
                input_char
            ))

        # Return the new state, just return the
        return transitions[input_char]

    def get_next_state(self, start_state: State, input_char: Alphabet) -> Alphabet:
        """
        Given a start state and input character, this calculates the next state from the transition rules

        :param start_state: The starting state for this transition
        :param input_char: The character to process
        :return: The next state from the machine
        """
        return self.get_next_tuple(start_state, input_char)[0]

    def is_state_valid(self, state: State):
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

