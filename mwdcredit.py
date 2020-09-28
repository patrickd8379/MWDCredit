import random

NUMBERS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"] #Constant with all valid numbers
VALIDMENUANSWERS = ["1", "2", "3", "4"] #Only answers accepted when in menu()

def menu():
    menuInput = " "
    while menuInput not in VALIDMENUANSWERS: #Ensures user will select a valid answer
         print("1: Check my card number")
         print("2: Import and check numbers")
         print("3: Generate a valid credit card number")
         print("4: Quit")
         menuInput = input()
    if menuInput == "1":
        cardNum = input("Enter your card's number")
        print(validate(cardNum))
        print(" ")
        menu()
    elif menuInput == "2":
        fileFound = False
        while fileFound == False:
            cardFile = input("Enter the fileName with the cards you want to check") #User enters the name of the file
            try:
                cardFile = open(cardFile, "r")
            except FileNotFoundError: #Does not end the program and instead prompts user to enter again
                print("That file does not exist")
            else:
                fileFound = True
        for line in cardFile.readlines(): #Checks each card number
            print("[")
            cardNum = line
            cardNum = cardNum.strip("\n") #Ensures each number is correct length
            print(cardNum, validate(cardNum), "]") #Validates the card
        print(" ")
        menu()
    elif menuInput == "3":
        cardGenerate()
        print(" ")
        menu()
    elif menuInput == "4":
        return print("Thank You!")

def cardGenerate():
    cardsFile = open("cardsFile.txt", "w+").close() #Creates empty file or clears old one
    cardsFile = open("cardsFile.txt", "w+")
    cardsGenerated = []
    numberOfCards = int(input("How many numbers do you want to genreate?"))
    while numberOfCards > 100 or numberOfCards < 1:
        numberOfCards = int(input("How many numbers do you want to genreate?"))
    for i in range(numberOfCards):
        cardNum = cardMake() #Creates a random card
        while cardNum in cardsGenerated: #Ensures no repeats in the file
            cardNum = cardMake()
        cardsGenerated.append(cardNum)
    for i in range(numberOfCards): #Writes each number into the file with a line each
        cardsFile.write("%s\n" % cardsGenerated[i])
    cardsFile.close()
    cardsFile = open("cardsFile.txt", "r")
    print(cardsFile.read())


def cardMake():
    cardNum = []
    cnDoubles = []
    while len(cardNum) < 15:
        cardNum.append(random.randint(0, 9)) #Puts 15 random numbers into cardNum
    for i in range(len(cardNum)): #Puts normal numbers and doubled numbers into a list before being added
        if i % 2 == 0:
            cnDoubles.append(cardNum[i] * 2)
        else:
            cnDoubles.append(cardNum[i])
    cardSum = sum(cnDoubles, 0)
    validCard = False
    while validCard == False: #Creates random last numbers until the last number makes the credit card number valid
        lastNum = random.randint(0, 9)
        if (cardSum + lastNum) % 10 == 0:
            cardNum.append(lastNum)
            validCard = True
    for i in range(len(cardNum)): #Turns numbers into strings
        cardNum[i] = str(cardNum[i])
    cardNum = "".join(cardNum) #Numbers joined into one string
    return cardNum

def validate(cardNum):
    cardNum = [cardNum[i:i+1] for i in range(len(cardNum))] #Splits cardNum into a list
    if len(cardNum) != 16: #Checks the length of cardNum
        return "Card is not valid, Incorrect length"
    for i in range(len(cardNum)):
        if cardNum[i] not in NUMBERS: #Checks if the character is a number
            return "Card is not valid, Invalid character"
        if i % 2 == 0: #Checks if i is even
            cardNum[i] = int(cardNum[i])*2
        else:
            cardNum[i] = int(cardNum[i])
    cardValue = sum(cardNum, 0)
    print("CardValue: ", cardValue)
    print("CardValue % 10 = ", (cardValue % 10))
    if cardValue % 10 == 0: #Checks if cardValue is divisible by 10
        return "Card is valid"
    else:
        return "Card is not valid, Not divisible by 10"

menu()
