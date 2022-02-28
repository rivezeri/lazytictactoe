import time

def playerAsk():
    '''Asks before main() for tic-tac-toe'''
    while True:
        ask = input('Who will start first? X or O?\n/-> ')
        if ask.capitalize() == 'X':
            rotate = 'X'
            return rotate
        elif ask.capitalize() == 'O':
            rotate = 'O'
            return rotate
        else:
            print('Please input a proper value.')

def adder(rotate):
    '''adds the values to index and find which value to replace.'''
    try:
        modifyRow = int(input(f'It\'s now {rotate}\'s turn. Please select a row to modify.\n(rows 1-3) /-> '))
        if modifyRow == 1:
            modifyRow -= 1
        elif modifyRow == 2:
            modifyRow += 1
        elif modifyRow == 3:
            modifyRow += 3
        elif modifyRow == '':
            print('Please make an entry.')
        else:
            print('Please try again.')
        return modifyRow
    except:
        print('Please try again.')
        return rotate

def modify(modifyRow, rotate, columnsList):
    '''modifying body'''
    try:
        modifyColumn = int(input('Select a column to modify:\n(columns 1-3) /-> '))
        if modifyColumn == 1 or 2 or 3:
            toReplace = modifyColumn + modifyRow - 1
            if columnsList[toReplace] != ' ':
                print('Please select a space that is not filled.')
                return rotate
            else:
                columnsList[toReplace] = rotate
                if rotate == 'X':
                    return 'O'
                elif rotate == 'O':
                    return 'X'
        else:
            print('Between 1-3.')
    except:
        print('Please try again.')
        return rotate


def winCheck(columnsList):
    '''checks win condition'''
    if columnsList[0] == columnsList[1] == columnsList[2] != " ":
        return 'win'
    elif columnsList[3] == columnsList[4] == columnsList[5] != " ":
        return 'win'
    elif columnsList[6] == columnsList[7] == columnsList[8] != " ":
        return 'win'
    elif columnsList[2] == columnsList[4] == columnsList[6] != " ":
        return 'win'
    for i in range(len(columnsList) - 6):
        if columnsList[i] == columnsList[i + 3] == columnsList[i + 6] != " ":
            return 'win'
    for i in range(len(columnsList) - 8):
        if columnsList[i] == columnsList[i + 4] == columnsList[i + 8] != " ":
            return 'win'

def isFull(board): # partial cite from stackoverflow. i know what i'm doing
    '''checks if tie'''
    count = 0
    for i in range(0,9):
        if board[i] == "X" or board[i] == "O":
            count += 1
    if count == 9:
        return True
    return False

def main():
    columnsList = [' ', ' ', ' ',
                   ' ', ' ', ' ',
                   ' ', ' ', ' ']
    print('Welcome to tic-tac-toe.')
    rotate = playerAsk()
    while True:
        tie = isFull(columnsList)
        print(f'|{columnsList[0]}|{columnsList[1]}|{columnsList[2]}| < - Row')
        print(f'|{columnsList[3]}|{columnsList[4]}|{columnsList[5]}|')
        print(f'|{columnsList[6]}|{columnsList[7]}|{columnsList[8]}|\n^ - Column')
        wincheck = winCheck(columnsList)
        if wincheck == 'win':
            if rotate == 'X':
                rotate = 'O'
            else:
                rotate = 'X'
            print(f'\n{rotate} wins!')
            time.sleep(2)
            print('...')
            break
        elif tie == True:
            print('Tie.')
            time.sleep(2)
            print('...')
            break
        else:
            modifyRow = adder(rotate)
            if rotate == 'X':
                rotate = modify(modifyRow, rotate, columnsList)
            elif rotate == 'O':
                rotate = modify(modifyRow, rotate, columnsList)

if __name__ == '__main__':
    main()
