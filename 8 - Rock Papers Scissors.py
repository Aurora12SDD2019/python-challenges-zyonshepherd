play = True

while play == True:
    
    player1 = input('Player1 = Rock, Paper, or Scissors? ')
    player2 = input('Player2 = Rock, Paper, or Scissors? ')
    
    if player1 == 'Rock' and player2 == 'Scissors':
        print('player1 wins')
    elif player2 == 'Rock' and player1 == 'Scissors':
        print('player2 wins')
        
    elif player1 == 'Scissors' and player2 == 'Paper':
        print('player1 wins')
    elif player2 == 'Scissors' and player1 == 'Paper':
        print('player2 wins')
        
    elif player1 == 'Paper' and player2 == 'Rock':
        print('player1 wins')
    elif player2 == 'Paper' and player1 == 'Rock':
        print('player2 wins')
        
    else:
        print('try again')
        
    choice = input('Would you like to keep playing? ')
    
    if choice == 'no':
        print('Ok, Goodbye')
        break
