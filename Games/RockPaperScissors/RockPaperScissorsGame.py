from __future__ import annotations
from typing import Dict, List
from random import choice


##
# This class encapsulates the general case of game where both players
# pick an option, the winner is determined by a set of rules definining which
# options beat which other options
##
class RockPaperScissorsGame:
    beats: Dict[str, List[str]]
    options: List[str]

    def __init__(self):
        self.beats = {}

    def x_beats_y(self, x: str, y: str) -> RockPaperScissorsGame:
        if x not in self.beats:
            self.beats[x] = []

        self.beats[x].append(y)
        return self

    def does_x_beat_y(self, x: str, y: str) -> bool:
        if x not in self.beats:
            raise Exception('This option does not exist: {}'.format(x))

        return y in self.beats[x]

    def done(self) -> RockPaperScissorsGame:
        self.options = list(self.beats.keys())
        return self

    def play(self):
        player_choice = self.player_choose()
        cpu_choice = self.cpu_choose()

        print('Player Chose: {}'.format(player_choice))
        print('CPU Chose: {}'.format(cpu_choice))

        if player_choice == cpu_choice:
            print('Draw, both chose {}'.format(player_choice))
        if self.does_x_beat_y(player_choice, cpu_choice):
            print('Player Wins, {} beats {}'.format(player_choice, cpu_choice))
        else:
            print('CPU Wins, {} beats {}'.format(cpu_choice, player_choice))

    def player_choose(self) -> str:
        print('Make a choice:')
        for i, o in enumerate(self.options):
            print('{}: {}'.format(i, o))

        player_choice: int = 0
        # Loop forever until player makes a valid selection
        while True:
            try:
                player_choice = int(input('Type the number of your choice: '))
                if player_choice >= len(self.options):
                    print('Invalid choice: {}'.format(player_choice))
                    continue
                else:
                    break
                # otherwise safe to continue
            except ValueError:
                print('Invalid number')

        return self.options[player_choice]

    def cpu_choose(self) -> str:
        return choice(self.options)


