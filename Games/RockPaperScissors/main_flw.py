from Games.RockPaperScissors.RockPaperScissorsGame import RockPaperScissorsGame

fire_logs_water = RockPaperScissorsGame()\
    .x_beats_y('fire', 'logs')\
    .x_beats_y('logs', 'water')\
    .x_beats_y('water', 'fire')\
    .done()

print('Now Playing Fire, Logs, Water')
fire_logs_water.play()
