from __future__ import annotations
from typing import List, Dict, Optional, Tuple

RulePart = Tuple[bool, str]


class BNFRule:
    __name: str
    __form: List[RulePart]

    def __init__(self, name: str, form: List[RulePart]):
        self.__name = name
        self.__form = form

    def __repr__(self):
        return "".join(["<{}>".format(value) if is_tag else "\"{}\"".format(value) for is_tag, value in self.__form])

    def get_name(self) -> str:
        return self.__name

    def is_match(self, thus_far: List[BNFRule], remaining_str: str) -> bool:
        return False


GIVEN_BY: str = '::='
OR: str = '|'


class BackusNaurForm:
    __rules: Dict[str, List[BNFRule]] = dict()

    def __repr__(self):
        return "Backus-Naur Form{}".format(
            "".join(["\n\t{} - {}".format(n, r) for n, r in self.__rules.items()]))

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

        alternatives: List[BNFRule] = []
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
            alternatives.append(BNFRule(rule_name, form))

        self.__rules[rule_name] = alternatives
        return self

    def find_match(self, input_str: str) -> Optional[BNFRule]:
        return None