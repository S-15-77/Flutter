

#XO game





#1.Display the game board
#2.Make th board empty
#3.Provide Nos to cells
#4.Error in cell is >9
#5.Apperance
#6.Logic

keysBoard ={'7':' ','8':' ','9':' ',
            '4':' ','5':' ','6':' ',
            '1':' ','2':' ','3':' '} # to set up the board index

Keys = []
for key in keysBoard: #to fill the board
    Keys.append(key)

#print(Keys)
def priBoard(board): #board design
    print(board['7']+ '/'+ board['8']+ '/'+ board['9']+'/')
    print('------')
    print(board['4']+ '/'+ board['5']+ '/'+ board['6']+ '/')
    print('------')
    print(board['1']+ '/'+ board['2']+ '/'+ board['3']+ '/')
    print('------')
#priBoard(keysBoard)
def game():
    turn = 'X'
    count = 0
    for i in range(10):
        priBoard(keysBoard) #to display the board
        print('Turn of',turn,'Specifie the place to enter:')
        move = input() #input the title from user
        if keysBoard[move] == ' ':
            keysBoard[move] = turn
            count +=1
        else:
            print('Filled ,Enter anyother')
            continue
        if count >= 5: #to check the pairs
            if keysBoard['7'] == keysBoard['8'] == keysBoard['9'] != ' ':
                priBoard(keysBoard)
                print('Game Over')
                print('Player',turn,'Won')
                break
            if keysBoard['4'] == keysBoard['5'] == keysBoard['6'] != ' ':
                priBoard(keysBoard)
                print('Game Over')
                print('Player',turn,'Won')
                break
            if keysBoard['1'] == keysBoard['2'] == keysBoard['3'] != ' ':
                priBoard(keysBoard)
                print('Game Over')
                print('Player',turn,'Won')
                break
            if keysBoard['1'] == keysBoard['4'] == keysBoard['7'] != ' ':
                priBoard(keysBoard)
                print('Game Over')
                print('Player',turn,'Won')
                break
            if keysBoard['2'] == keysBoard['5'] == keysBoard['8'] != ' ':
                priBoard(keysBoard)
                print('Game Over')
                print('Player',turn,'Won')
                break
            if keysBoard['3'] == keysBoard['6'] == keysBoard['9'] != ' ':
                priBoard(keysBoard)
                print('Game Over')
                print('Player',turn,'Won')
                break
            if keysBoard['1'] == keysBoard['5'] == keysBoard['9'] != ' ':
                priBoard(keysBoard)
                print('Game Over')
                print('Player',turn,'Won')
                break
            if keysBoard['3'] == keysBoard['5'] == keysBoard['7'] != ' ':
                priBoard(keysBoard)
                print('Game Over')
                print('Player',turn,'Won')
                break
        if count == 9: #if no pairs matches
            print('Game Over')
            print('Tied')
        if turn == 'X':
            turn = '0'
        else:
            turn = "X"
    cont = input('Do u want to continue:')
    if cont.lower() == 'yes':
        for k in Keys:
            keysBoard[k] = ''
        game()
if __name__ == "__main__": #main function
    game()