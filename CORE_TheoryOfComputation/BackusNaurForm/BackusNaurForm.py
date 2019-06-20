from __future__ import annotations
from typing import List, Dict, Optional, Tuple
from CORE_DataStructures.CircularQueue.CircularQueue import CircularQueue

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
        rule_name: str = outer_parts[0]

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

    def __check_match(self,
                      input_str: str,
                      rule: Rule,
                      from_index: int,
                      to_index: int) -> bool:
        print("Checking Match of {} [{}:{}] against rule: {}".format(
            input_str, from_index, to_index, rule
        ))

        # Put all the rule parts on a queue
        rule_parts_q: CircularQueue[RulePart] = CircularQueue(len(rule))
        for rule_part in rule:
            rule_parts_q.enqueue(rule_part)

        # We we have elements to resolve
        while not rule_parts_q.is_empty():
            # Pick the next one
            is_tag, rule_value = rule_parts_q.dequeue()
            print("Checking {} [{}:{}] against {}, {}".format(input_str, from_index, to_index, is_tag, rule_value))

            temp_to_index: int = to_index
            while temp_to_index > from_index:
                input_sub_str = input_str[from_index:temp_to_index]
                if is_tag:
                    sub_rule_alternatives: List[Rule] = self.__rules[rule_value]
                    if sub_rule_alternatives is None or len(sub_rule_alternatives) == 0:
                        raise Exception("Cannot find any rules for {}".format(rule_value))

                    for sub_rule in sub_rule_alternatives:
                        is_match: bool = self.__check_match(input_sub_str, sub_rule, from_index, temp_to_index)
                        if is_match:
                            print("Match Found {} - [{}:{}]".format(sub_rule, from_index, temp_to_index))
                            if temp_to_index == to_index:
                                return True
                            from_index = temp_to_index
                            break

                else:
                    print("Comparing Literal Rule: '{}' to Value: '{}'".format(rule_value, input_sub_str))
                    # This is literal, just compare the value
                    if rule_value == input_sub_str:
                        print("Match Found [{}:{}]".format(from_index, temp_to_index))
                        if temp_to_index == to_index:
                            return True
                        from_index = temp_to_index
                        break

                temp_to_index -= 1
            print("Index Ran Out {} [{}:{}]".format(input_str, from_index, to_index))

        return False

    def find_match(self, input_str: str) -> Optional[str]:
        print("Find Match for {}".format(input_str))

        for name, alternative_rules in self.__rules.items():
            for rule in alternative_rules:
                if self.__check_match(input_str, rule, 0, len(input_str)):
                    return name
        return None
