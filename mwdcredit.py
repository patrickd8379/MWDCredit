NUMBERS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

def validate(cardNum):
    cardNum = [cardNum[i:i+1] for i in range(len(cardNum))]
    print(cardNum)
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

print(validate("1234567812345678"))
