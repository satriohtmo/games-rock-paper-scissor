import random

user_wins = 0
computer_wins = 0
draw = 0

rps = ['rock', 'paper', 'scissor']

while True:
    user_input = input('Type Rock/Paper/Scissor or q to quit: ').lower()
    if user_input == 'q':
     break

    if user_input not in rps:
       continue

    random_number = random.randint(0, 2)

    computer_pick = rps[random_number]
    print('computer pick', computer_pick + '.')

    if user_input == 'rock' and computer_pick == 'scissor':
       print('user wins')
       user_wins +=1
    
    elif user_input == 'paper' and computer_pick == 'rock':
       print('user wins')
       user_wins +=1
    
    elif user_input == 'scissor' and computer_pick == 'paper':
       print('user wins')
       user_wins +=1

    elif user_input == 'scissor' and computer_pick == 'scissor':
       print('draws')
       draw +=1
    
    elif user_input == 'paper' and computer_pick == 'paper':
       print('draws')
       draw +=1
    
    elif user_input == 'rock' and computer_pick == 'rock':
       print('draws')
       draw +=1
    
    else:
       print('computer wins')
       computer_wins +=1

print('user wins: ' + str(user_wins))
print('computer wins: ' + str(computer_wins))
print('draw: ' + str(draw))
print('thx 4 playing have a good day! ;)')
