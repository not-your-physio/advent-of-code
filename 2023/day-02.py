## CODE TO ACCESS day-02.TXT


adventofcode2docpath = "day-02.txt"
##print(adventofcode2docpath)

with open(adventofcode2docpath, 'r') as file:
    originalinput = ''.join(file.readlines()).strip()

def is_valid_move(move):
    move = move.strip()
    splitmove = move.split()
    number = int(splitmove[0])
    colour = splitmove[1]
    if colour == "red":
        if number > 12:
            return False
    if colour == "green":
        if number > 13:
            return False
    if colour == "blue":
        if number > 14:
            return False
    return True


def is_valid_turn(turn):
    moves = turn.split(',')
    for move in moves:
        if is_valid_move(move) == False:
            return False
    return True



def is_valid_game(game):
    turns = game.split(';')
    for turn in turns:
        if is_valid_turn(turn) == False:
            return False
    
    return True


games = originalinput.split("Game ")[1:] #removes first empty string

gameIDs = []
for game in games:
    splitgame = game.split(':')
    number = splitgame[0]
    turns = splitgame[1]
    if is_valid_game(turns) == True:
        gameIDs.append(int(number))
print(sum(gameIDs))
