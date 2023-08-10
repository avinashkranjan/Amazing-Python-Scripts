import random

def pb(b):
    for r in b:
        print('|'.join(r))
        print('-'*5)

def iw(b, p):
    return any(all(c == p for c in r) for r in b) or any(all(b[i][j] == p for i in range(3)) for j in range(3)) or all(b[i][i] == p for i in range(3)) or all(b[i][2-i] == p for i in range(3))

def id(b):
    return all(all(c != '.' for c in r) for r in b)

def gec(b):
    return [(i, j) for i in range(3) for j in range(3) if b[i][j] == '.']

def mm(b, d, im):
    s = {'X': 1, 'O': -1, 'draw': 0}
    if iw(b, 'X'):
        return s['X'] - d
    elif iw(b, 'O'):
        return s['O'] + d
    elif id(b):
        return s['draw']
    if im:
        bs = float('-inf')
        for i, j in gec(b):
            b[i][j] = 'X'
            s = mm(b, d + 1, False)
            b[i][j] = '.'
            bs = max(bs, s)
        return bs
    else:
        bs = float('inf')
        for i, j in gec(b):
            b[i][j] = 'O'
            s = mm(b, d + 1, True)
            b[i][j] = '.'
            bs = min(bs, s)
        return bs

def gbm(b):
    bs = float('-inf')
    bm = None
    for i, j in gec(b):
        b[i][j] = 'X'
        s = mm(b, 0, False)
        b[i][j] = '.'
        if s > bs:
            bs = s
            bm = (i, j)
    return bm

def main():
    b = [['.' for _ in range(3)] for _ in range(3)]
    p = 'X'
    while True:
        pb(b)
        if iw(b, 'X'):
            print("You win!")
            break
        elif iw(b, 'O'):
            print("AI wins!")
            break
        elif id(b):
            print("It's a draw!")
            break
        if p == 'X':
            r, c = map(int, input("Enter row and column (0-2) separated by space: ").split())
            if b[r][c] != '.':
                print("Invalid move. Try again.")
                continue
            b[r][c] = 'X'
            p = 'O'
        else:
            print("AI is thinking...")
            r, c = gbm(b)
            b[r][c] = 'O'
            p = 'X'

if __name__ == "__main__":
    main()
