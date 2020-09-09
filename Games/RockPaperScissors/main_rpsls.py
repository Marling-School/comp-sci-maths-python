from Games.RockPaperScissors.RockPaperScissorsGame import RockPaperScissorsGame

rock_paper_scissors_lizard_spock = RockPaperScissorsGame()\
    .x_beats_y('paper', 'rock')\
    .x_beats_y('paper', 'spock')\
    .x_beats_y('rock', 'scissors')\
    .x_beats_y('rock', 'lizard')\
    .x_beats_y('scissors', 'paper')\
    .x_beats_y('scissors', 'lizard')\
    .x_beats_y('spock', 'scissors')\
    .x_beats_y('spock', 'rock')\
    .x_beats_y('lizard', 'paper')\
    .x_beats_y('lizard', 'spock')\
    .done()

print('Now Playing Rock, Paper, Scissors, Lizard, Spock')
rock_paper_scissors_lizard_spock.play()
