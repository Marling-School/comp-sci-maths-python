from __future__ import annotations
from typing import List, Dict, Optional, Tuple
from CORE_Algorithms.Queue.QueueImpl import Queue, QueueImpl

RulePart = Tuple[bool, str]
Rule = List[RulePart]


GIVEN_BY: str = '::='
OR: str = '|'


class BackusNaurForm:
    __rules: Dict[str, List[Rule]] = dict()

    def __repr__(self):
        as_str: str = "Backus-Naur Form{}"
        for name, alternative_rules in self.__rules.items():
            for rule in alternative_rules:
                as_str += "\n\t{}: ".format(name)
                for is_tag, value in rule:
                    as_str += "<{}>, ".format(value) if is_tag else "'{}',".format(value)
        return as_str

    def add_rule(self, rule_str: str) -> BackusNaurForm:
        # Separate out the name of the definition from what it is given by
        outer_parts = [x.strip() for x in rule_str.split(GIVEN_BY)]
        if len(outer_parts) != 2:
            raise Exception("Could not parse {}, unexpected number of parts divided by {}".format(
                rule_str,
                GIVEN_BY
            ))
        rule_name: str = outer_parts[0].strip()[1:-1]

        # Separate out all the alternatives using the OR
        alternatives_str: List[str] = [x.strip() for x in outer_parts[1].split(OR)]

        alternatives: List[Rule] = []
        for alternative_str in alternatives_str:
            form: List[RulePart] = []
            is_building_tag: bool = False
            is_building_literal: bool = False
            current_literal: str = ""
            for c in alternative_str:
                if c == "<":
                    if len(current_literal) > 0:
                        form.append((False, current_literal))
                        current_literal = ""
                    is_building_tag = True
                elif c == ">":
                    if not is_building_tag:
                        raise Exception("Saw close tag without open tag")
                    is_building_tag = False
                    form.append((True, current_literal))
                    current_literal = ""
                elif c == "'":
                    if not is_building_literal:
                        if len(current_literal) > 0:
                            form.append((False, current_literal))
                            current_literal = ""
                    if is_building_literal:
                        form.append((False, current_literal))
                        current_literal = ""
                    is_building_literal = not is_building_literal
                else:
                    current_literal += c
            if len(current_literal) > 0:
                form.append((False, current_literal))
            alternatives.append(form)

        self.__rules[rule_name] = alternatives
        return self

    def __check_value_against_rule_part(self,
                                        input_str: str,
                                        from_index: int,
                                        to_index: int,
                                        rule_part: RulePart) -> bool:
        is_tag, rule_value = rule_part
        if is_tag:
            sub_rule_alternatives: List[Rule] = self.__rules[rule_value]
            if sub_rule_alternatives is None or len(sub_rule_alternatives) == 0:
                raise Exception("Cannot find any rules for {}".format(rule_value))

            for sub_rule in sub_rule_alternatives:
                is_match: bool = self.__check_match(input_str, from_index, to_index, sub_rule)
                if is_match:
                    return True

        else:
            return rule_value == input_str[from_index:to_index]

        return False

    def __check_match(self,
                      input_str: str,
                      from_index: int,
                      to_index: int,
                      rule: Rule) -> bool:
        # Build a Queue of Rule Parts to satisfy
        rule_part_q: Queue[RulePart] = QueueImpl()
        for rule_part in rule:
            rule_part_q.enqueue(rule_part)

        # While there are rule parts to satisfy...
        while not rule_part_q.is_empty():
            rule_part = rule_part_q.dequeue()

            # Match the rule part against as much of the remaining string as possible
            temp_to_index: int = to_index
            match_found: bool = False

            # While there is any remaining string to try and match
            while temp_to_index > from_index and not match_found:
                # Attempt a match at this rule part
                match: bool = self.__check_value_against_rule_part(input_str, from_index, temp_to_index, rule_part)
                if match:
                    # The next rule needs to match 'from' the end of the string we just matched against
                    from_index = temp_to_index
                    match_found = True
                else:
                    # Take one character off the end
                    temp_to_index -= 1

            if not match_found:
                return False

        # If we satisfied all the rule parts AND consumed the whole string, this is a match
        return rule_part_q.is_empty() and from_index == to_index

    def find_match(self, input_str: str) -> Optional[str]:
        for name, alternative_rules in self.__rules.items():
            for rule in alternative_rules:
                if self.__check_match(input_str, 0, len(input_str), rule):
                    return name
        return None
