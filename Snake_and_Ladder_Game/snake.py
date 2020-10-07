import random
#Assigning position of the snakes and ladders
snakepos={11:2,25:4,38:9,65:46,89:70,93:64}
ladderpos={8:37,13:34,40:68,52:81,76:97}
def generate_random():
    '''
    A function to return a random number between 1 and 12 to roll the dice
    Return type: Integer
    '''
    return random.randrange(1,13)

def get_player_dict(n):
    '''
    A function to generate a dictionary containing the players name and associate it with the score
    Arguments: Number of players, int
    Return type: dict
    '''
    adict={}
    for i in range(1,n+1):
        a=input("Enter the name of player "+str(i)+" : ")
        adict[a]=0
    return adict

#Beginning of the game UI
    
print("Welcome to the game of Snake and Ladder.")
num=int(input("Enter the number of players: "))
player_list=get_player_dict(num) #Gets the player list
flag=True
while(flag==True):
    print("*****************************************************************************")
    print("Beginning of round.")
    print()
    for i in player_list.keys():    #iterating over the list of players
        print(i+'\'s'+" turn.")
        input("Press <Enter> to continue.")
        print()
        dice=generate_random()
        print("The roll of dice results in:",dice)
        print()
        player_list[i]+=dice
        if(player_list[i] in snakepos):
            print("Oops, you landed on the snake! You are downgraded.")
            player_list[i]=snakepos[player_list[i]]
        elif(player_list[i] in ladderpos):
            print("Yippie! You landed on the ladder! You are upgraded.")
            player_list[i]=ladderpos[player_list[i]]
        elif(player_list[i]>=100):
            print(i,"won the game! Congratulations!")
            flag=False
            break                    #exits out of the for loop
        print("Score of",i,"is:",player_list[i])            
        print()         
    if(player_list[i]<100):    
        print("End of round. Scores of all players:-")      #prints only if the game continues
        for k in player_list.keys():
            print(k+":",player_list[k])
    print("*****************************************************************************")
