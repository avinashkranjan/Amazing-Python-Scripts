import random


# tarot deck of 78 cards and 'predictions'
tarot_deck = [
    "The Fool: \n\tExperience is your best teacher",
    "The Magician: \n\tLife is Magic... do you control yours?",
    "The High Priestess: \n\tStay away from worldly affairs",
    "The Empress: \n\tThe world bows before you, you bow to none",
    "The Emperor: \n\tThe world bows before you, you bow to none",
    "The Hierophant: \n\tFollow the 4rc@n3 principles",
    "The Lovers: \n\tI've never writ, nor no man never loved",
    "The Chariot: \n\tYou'll get to see your dream ride soon",
    "Strength: \n\tYou are stong enough",
    "The Hermit: \n\tThe World hurtles forward, yet you remain uncaught in its riptide",
    "Wheel of Fortune: \n\tYour luck today depends on whether the first living thing you see is a plant or an animal",
    "Justice: \n\tThe Mills of God grind slow but fine",
    "The Hanged Man: \n\tThat's rough buddy",
    "Death: \n\tLife's younger sibling brushed your shoulder just now, but you're fine- it was just lint",
    "Temperance: \n\tThe World needs more of it, and of you",
    "The Devil: \n\tGet over here so I can prove that you exist",
    "The Tower: \n\tExchange places with the king",
    "The Star: \n\tLike diamonds in the sky~",
    "The Moon: \n\tYou might find that your enthusiasm waxes and wanes, but that's alright",
    "The Sun: \n\tYou're the light of someone's life",
    "Judgement: \n\t*judges you in spanish*",
    "The World: \n\tThese hands could hold you but it'll never be enough~",
    "Ace of Wands: \n\tYou're a wizard, Harry",
    "Two of Wands: \n\tYour sibling is pretty cool",
    "Three of Wands: \n\tTry to avoid tournaments for the time being",
    "Four of Wands: \n\tFind trouble and make it double",
    "Five of Wands: \n\tExpecto Patronum",
    "Six of Wands: \n\tDraw your wand",
    "Seven of Wands: \n\tIf you see a noseless man with the complexion of crushed eggshells, RUN",
    "Eight of Wands: \n\tI'm surprised you got this tbh... I'll let you in on a secret - Seven didn't actually eat Nine",
    "Nine of Wands: \n\tOh, the card you're looking for is 3 quarters to the right",
    "Ten of Wands: \n\tOh, the card you're looking for is a quarter to the left",
    "Page of Wands: \n\tYou're going to be called to the Head's Office - you shouldn't have messed with alchemy unsupervised",
    "Knight of Wands: \n\tYou just had to buy that giant chess set, didn't you?",
    "Queen of Wands: \n\tWith great power...",
    "King of Wands: \n\tWith great power...",
    "Ace of Cups: \n\tIf you ever see a trophy in the middle of a hedge maze...",
    "Two of Cups: \n\tBottoms up, friend!",
    "Three of Cups: \n\tTwo's company, three's better company!",
    "Four of Cups: \n\tThe more the merrier!",
    "Five of Cups: \n\tYeah, social distancing is important",
    "Six of Cups: \n\tNow that's one too many",
    "Seven of Cups: \n\tTwo's company enough",
    "Eight of Cups: \n\tTake a break",
    "Nine of Cups: \n\tIf three's a crowd...",
    "Ten of Cups: \n\tStop it now",
    "Page of Cups: \n\tI don't think you should drive until you clear your head",
    "Knight of Cups: \n\tPut that sword down right this instant",
    "Queen of Cups: \n\tDon't offend anyone influential",
    "King of Cups: \n\tDon't get on your gaurdians' bad side",
    "Ace of Swords: \n\tDraw your sword",
    "Two of Swords: \n\tEn garde",
    "Three of Swords: \n\tAllez!",
    "Four of Swords: \n\tParry!",
    "Five of Swords: \n\tLearn enough to be dangerous",
    "Six of Swords: \n\tGet yourself a teacher",
    "Seven of Swords: \n\tParlay!",
    "Eight of Swords: \n\tDo something nice for a stranger",
    "Nine of Swords: \n\tBe chivalrous",
    "Ten of Swords: \n\tI'm not asking for much, just be nice",
    "Page of Swords: \n\tThe pen is mightier",
    "Knight of Swords: \n\tLive by the code you're honour-bound to follow",
    "Queen of Swords: \n\tPledge alliance",
    "King of Swords: \n\tPledge alliance",
    "Ace of Coins: \n\tYou now have an iron nail",
    "Two of Coins: \n\tFlip a coin",
    "Three of Coins: \n\tFor want of a nail...",
    "Four of Coins: \n\tYou now have a paperclip",
    "Five of Coins: \n\tSleep well, it is a blessing",
    "Six of Coins: \n\tRoll a die",
    "Seven of Coins: \n\tYou're a lucky one",
    "Eight of Coins: \n\tYou're like a pineapple tree - i.e. you're a factual error",
    "Nine of Coins: \n\tAccessory fruit(affectionate)",
    "Ten of Coins: \n\t<insert cool fruit fact here>",
    "Page of Coins: \n\tYou're due for a promotion soon",
    "Knight of Coins: \n\tTreat your subordinates",
    "Queen of Coins: \n\tYou're worth your weight in gold",
    "King of Coins: \n\tYou're worth your weight in gold"
]


def fin():
    print("Whichever your choice was...")
    input(">> press enter")
    print("May the cards ever be in your favour")
    input(">> press enter")
    print()
    print("\x1B[3mFin\x1B[23m".center(72))
    print("*"*72)


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
    print(tarot_deck[pick_card2] if pick_card2 != pick_card1 else tarot_deck[random.randint(0, 78)])
    input(">> press enter")
    print()
    print("And your third and final card is...")
    pick_card3 = random.randint(0, 78)
    print(tarot_deck[pick_card3] if pick_card3 != pick_card1 and pick_card3 != pick_card2 else tarot_deck[random.randint(0, 78)])
    input(">> press enter")
    print()
    fin()


def youve_chosen_no():
    print("Are you wise...")
    input(">> press enter")
    print("Or foolish?")
    input(">> press enter")
    print("I suppose only time will tell")
    input(">> press enter")
    fin()


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


# Introductory text
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
ch = input(">> enter Y/N: ")
print("\nInteresting...")

if ch.lower() == 'y':
    youve_chosen_yes()

elif ch.lower()=='n':
    print()
    youve_chosen_no()

else:
    print()
    youve_chosen_neither()
    
