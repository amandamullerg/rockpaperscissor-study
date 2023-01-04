# ROCK, PAPER, SCISSORS

import random, sys

wins = 0
losses = 0
ties = 0

while True: # main loop
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties)) # scores
    while True: # player input loop
        print('Please choose your move: (r)ock, (p)aper, (s)cissor or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
        print('Please answer with r, p, s or q')

# player choice
    if playerMove == 'r':
        print('ROCK versus...')
    if playerMove == 'p':
        print('PAPER versus...')
    if playerMove == 's':
        print('SCISSORS versus...')

# machine choice   
    RandomNumber = random.randint(1,3)
    if RandomNumber == 1:
        computerMove = 'r'
        print('ROCK!')
    if RandomNumber == 2:
        computerMove = 'p'
        print('PAPER!')
    if RandomNumber == 3:
        computerMove = 's'
        print('SCISSORS!')

# results
    if playerMove == computerMove:
        print("IT'S A TIE!")
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('YOU WIN!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('YOU LOSE!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('YOU WIN!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 's':
        print('YOU LOSE!)')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'p':
        print('YOU WIN!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'r':
        print('YOU LOSE!')
        losses = losses + 1