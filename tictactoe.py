import time

class tictacToeError(Exception):
    pass

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
    except Exception:
        raise tictacToeError('Please enter an integer.')
    return modifyRow

def modify(modifyRow, rotate, columnsList):
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
        print('Please input a proper value.')

def winCheck(columnsList):
    '''checks win condition'''
    for i in range(len(columnsList) - 3):
        if columnsList[i] == columnsList[i + 1] == columnsList[i + 2] != " ":
            return 'win'
    for i in range(len(columnsList) - 6):
        if columnsList[i] == columnsList[i + 3] == columnsList[i + 3] != " ":
            return 'win'
    for i in range(len(columnsList) - 8):
        if columnsList[i] == columnsList[i + 4] == columnsList[i + 8] != " ":
            return 'win'

def main():
    while True:
        columnsList = [' ', ' ', ' ',
                       ' ', ' ', ' ',
                       ' ', ' ', ' ']
        print('Welcome to tic-tac-toe.')
        rotate = playerAsk()
        while True:
            print(f'|{columnsList[0]}|{columnsList[1]}|{columnsList[2]}|')
            print(f'|{columnsList[3]}|{columnsList[4]}|{columnsList[5]}|')
            print(f'|{columnsList[6]}|{columnsList[7]}|{columnsList[8]}|')
            wincheck = winCheck(columnsList)
            if wincheck == 'win':
                print('You win!')
                time.sleep(1)
                print('.')
                time.sleep(2)
                print('..')
                time.sleep(2)
                print('...')
                break
            elif rotate == 'X' or 'O':
                modifyRow = adder(rotate)
                if rotate == 'X':
                    rotate = modify(modifyRow, rotate, columnsList)
                elif rotate == 'O':
                    rotate = modify(modifyRow, rotate, columnsList)

if __name__ == '__main__':
    main()