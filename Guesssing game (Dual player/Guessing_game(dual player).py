import random

r=random.randint(1,100)
st=1;
def toss():
    while(True):
            print('enter the choice(H/T)',player1,':')
            ch=input().upper()
            print()
            
            tos=random.choice(['H','T'])
            if(ch not in ['H','T']):
                    print('enter a valid charecter')
            else :
                  break
            
    if(ch==tos):
        print('toss won by',player1)
        return 1
    else :
        print('toss won by',player2)
        return 0 
def play(winner):
    p1st=1
    p2st=1
    while(True):
            
            if(winner==1):
                        print('enter',player1)
                        s=int(input())
                        if(s==r):
                            
                            return player1,p1st
                        elif(s>r):
                            print('enter a smaller number')
                        else :
                            print('enter a bigger number')
                        print('')
                        p1st+=1
                        winner=not winner
            else :      
                        print('enter',player2)
                        s=int(input())
                        if(s==r):
                            
                            
                            return player2,p2st
                        elif(s>r):
                            print('enter a smaller number')
                        else :
                            print('enter a bigger number')
                        print('')
                        p2st+=1
                        winner=not winner
            
  
print('-----------GAME START------------\n\n')
player1=input('enter your name: ')
print()
player2=input('enter your name: ')
print()
winner=toss()
print()
winner,steps=play(winner)
print('-----------GAME OVER--------------\n\nWinner is:',winner,'\nyou have guessed it in',steps,'number of steps\n')
print('----------------------------------\n\n')