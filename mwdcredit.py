import random

NUMBERS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
VALIDMENUANSWERS = ["1", "2", "3", "4"]

def menu():
    menuInput = " "
    while menuInput not in VALIDMENUANSWERS:
         print("1: Check my card number")
         print("2: Import and check numbers")
         print("3: Generate a valid credit card number")
         print("4: Quit")
         menuInput = input()
    if menuInput == "1":
        cardNum = input("Enter your card's number")
        validate(cardNum)
    elif menuInput == "2":
        fileFound = False
        while fileFound == False:
            cardFile = input("Enter the fileName with the cards you want to check")
            try:
                cardFile = open(cardFile, "r")
            except FileNotFoundError:
                print("That file does not exist")
            else:
                fileFound = True
        for line in cardFile.readlines():
            print(line)
            cardNum = line
            print("["cardNum, validate(cardNum)"]")
    elif menuInput == "3":
        cardGenerate()
    elif menuInput == "4":
        return "Thank You!"

def cardGenerate():
    cardNum = []
    cnDoubles = []
    while len(cardNum) < 15:
        cardNum.append(random.randint(0, 9))
    for i in range(len(cardNum)):
        if i % 2 == 0:
            cnDoubles.append(cardNum[i] * 2)
        else:
            cnDoubles.append(cardNum[i])
    cardSum = sum(cnDoubles, 0)
    validCard = False
    while validCard == False:
        lastNum = random.randint(0, 9)
        if (cardSum + lastNum) % 10 == 0:
            cardNum.append(lastNum)
            validCard = True
    for i in range(len(cardNum)):
        cardNum[i] = str(cardNum[i])
    cardNum = "".join(cardNum)
    return print(cardNum, validate(cardNum))

def validate(cardNum):
    cardNum = [cardNum[i:i+1] for i in range(len(cardNum))]
    if len(cardNum) < 16 or len(cardNum) > 16:
        return "Card is not valid"
    for i in range(len(cardNum)):
        if cardNum[i] not in NUMBERS:
            return "Card is not valid"
        if i % 2 == 0:
            cardNum[i] = int(cardNum[i])*2
        else:
            cardNum[i] = int(cardNum[i])
    cardValue = sum(cardNum, 0)
    print("CardValue: ", cardValue)
    print("CardValue % 10 = ", (cardValue % 10))
    if cardValue % 10 == 0:
        return "Card is valid"
    else:
        return "Card is not valid"

menu()
