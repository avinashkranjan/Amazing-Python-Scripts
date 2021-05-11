import random


# get tarot deck of 78 cards and 'predictions' from tarot.txt
file_handle = open("./Tarot Reader/tarot.txt", "r")
cards = file_handle.readlines()
tarot_deck = []
for card in cards:
    tarot_deck.append(card)


# Close file, display outro text
def fin():
    file_handle.close()
    print("Whichever your choice was...")
    input(">> press enter")
    print("May the cards ever be in your favour")
    input(">> press enter")
    print()
    print("\x1B[3mFin\x1B[23m".center(72))
    print("*"*72)


# Display when 'Y' or 'y' is entered
def youve_chosen_yes():
    print("I see that you've chosen to divine your future....")
    input(">> press enter")
    print("Let's make haste then...")
    input(">> press enter")
    print("Neither fame nor fortune wait for man")
    input(">> press enter")
    print()
    print("You have drawn three cards")
    print()
    print("Your first card is...")
    pick_card1 = random.randint(0, 77)
    print(tarot_deck[pick_card1])
    input(">> press enter")
    print()
    print("Your second card is...")
    pick_card2 = random.randint(0, 78)
    print(tarot_deck[pick_card2] if pick_card2 !=
          pick_card1 else tarot_deck[random.randint(0, 78)])
    input(">> press enter")
    print()
    print("And your third and final card is...")
    pick_card3 = random.randint(0, 78)
    print(tarot_deck[pick_card3] if pick_card3 != pick_card1 and pick_card3 !=
          pick_card2 else tarot_deck[random.randint(0,      78)])
    input(">> press enter")
    print()
    fin()


# Display when 'N' or 'n' is entered
def youve_chosen_no():
    print("Are you wise...")
    input(">> press enter")
    print("Or foolish?")
    input(">> press enter")
    print("I suppose only time will tell")
    input(">> press enter")
    fin()


# Handles other cases
def youve_chosen_neither():
    print("*le sigh*")
    input(">> press enter")
    print("I suppose you think this is a game...")
    input(">> press enter")
    print("You wouldn't be wrong...")
    input(">> press enter")
    print("But the only thing that you've played...")
    input(">> press enter")
    print("Is yourself.")
    input(">> press enter")
    print("\nNever gonna give you up,\nNever gonna let you down,\nNever gonna run around and desert you.\nNever gonna make you cry,\nNever gonna say goodbye,\nNever gonna tell a lie and hurt you.\n")
    fin()


# Intro text
print("In this black box, you read white words")
input(">> press enter")
print("Words that might warn you of danger...")
input(">> press enter")
print("Words that might foretell great fortune...")
input(">> press enter")
print("Or words that might make you laugh")
input(">> press enter")
print()


# Choice made here
print("Do you dare draw a card?")
ch = input(">> enter Y/n: ")
print("\nInteresting...")


# Driver code
if ch.lower() == 'y':
    print()
    youve_chosen_yes()

elif ch.lower() == 'n':
    print()
    youve_chosen_no()

else:
    print()
    youve_chosen_neither()
