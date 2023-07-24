#hasla to mało znane biblioteki Pythona

import random

def hangman():
    lista = ['pygame','psutil','seaborn','pywebview','pendulum','fabulous','pyforest','modin','pandasprofiling']
    x = random.randint(0, len(lista)-1)
    word = lista[x]
    wrong = 0
    stages = ['',
             '________     ',
             '|       |    ',
             '|       0    ',
             '|      /|\   ',
             '|       |    ',
             '|      / \   ',
             '|            ',
              ]
    letters = list(word)
    board = ['__'] * len(word)
    win = False
    print('Gra wisielec2')
    while wrong < len(stages) -1:
        print('\n')
        messi = 'podaj literę: '
        char = input(messi)
        if char in letters:
            cind= letters.index(char)
            board[cind] = char
            letters[cind] = '$'
        else:
            wrong += 1
        print((' '.join(board)))
        s = wrong + 1
        print('\n'.join(stages[0: s]))
        if '__' not in board:
            print('Brawo wygrałeś/aś!!!')
            print(' '.join(board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0: wrong]))
        print('Przegrałeś/aś :(( Hasło to: {}.'.format(word))
        
hangman()
