# Collect info
# Compile info into list
# Transist the key into num str (ltr = ltr, num = (append to num cyphered list) symbol = remove)
# Cypher translate comp name into number
# multiply both numbers, compile into str
# use seed to produce a list of nums 1-4
# use seed-produced list to compile multistr into 1-4 digit values
# divide by 2 continuously until under 26
    # General Introduction
print("Welcome to my password generator!")
print("This particular generator will pull a value of your choice using the founding date, company name, and your personal key.")
print("Your personal key will be the 'seed' to all of your passwords, keep it secret as it keeps your generated password unique.")
print("")
print("PLEASE MAKE SURE COMPANY NAME AND USER KEY INCLUDES LETTERS - MAKE KEY LONGER THAN 1 DIGIT")
print("____________")
    # Initial Inputs and check for correct inputs
while True:
    CompName = input("Please type the name of the company you wish to generate a password for:   ")
    FoundDate = input("Please type the founding date of the company you wish to generate a passoword for:   ")
    UserKey = input("Please type your personal key:   ")
    print(" Company Name = "+CompName+"\n Founding Date = "+FoundDate+"\n Personal Key= "+UserKey)
    UserCheck = input("Is this correct? Type 'yes' or 'no'")
    str.lower(UserCheck)
    if UserCheck == "yes":
        break
    # Checks and simplifies all inputs
print("")
CompName = str.lower(CompName)
UserKey = str.lower(UserKey)
        # Removes any letters from FoundDate, and turns FoundDate into int (PureFoundNum)
PreFoundDateList = list(FoundDate)
PureFoundList = []
for TempVar in PreFoundDateList:
    if TempVar == "0" or TempVar == "1" or TempVar == "2" or TempVar == "3" or TempVar == "4" or TempVar == "5" or TempVar == "6" or TempVar == "7" or TempVar == "8" or TempVar == "9":
        PureFoundList.append(TempVar)
PureFoundNum = ""
for TempLtr in PureFoundList:
    PureFoundNum = PureFoundNum + TempLtr
# FLAG: if FoundDate is empty or just letters this produces an error, add failsafe
PureFoundNum = int(PureFoundNum)
    # Translation of key and compname into int
CypherDict = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13, 'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
CypherDictReverse = {1: 'a', 3: 'c', 2: 'b', 5: 'e', 4: 'd', 7: 'g', 6: 'f', 9: 'i', 8: 'h', 11: 'k', 10: 'j', 13: 'm', 12: 'l', 15: 'o', 14: 'n', 17: 'q', 16: 'p', 19: 's', 18: 'r', 21: 'u', 20: 't', 23: 'w', 22: 'v', 25: 'y', 24: 'x', 26: 'z'}
CompNameList = list(CompName)
UserKeyList = list(UserKey)
ValidCypherList = ['a', 'c', 'b', 'e', 'd', 'g', 'f', 'i', 'h', 'k', 'j', 'm', 'l', 'o', 'n', 'q', 'p', 's', 'r', 'u', 't', 'w', 'v', 'y', 'x', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # Purification of CompName into ltr + Num, and translation into cyphered numbers (NumCompList)
        # Making sure each value exists in the dictionary before appending to new list
PureCompList = []
for TempVar in CompNameList:
    if ValidCypherList.count(TempVar) != 0:
        PureCompList.append(TempVar)
        # Appending the purified list's number counterparts to a new list
NumCompList = []
for TempLtr in PureCompList:
    NumCompList.append(CypherDict[TempLtr])
    # Purification of UserKey into ltr + Num, and translation into cyphered numbers (KeyNumList)
        # Making sure each value exists in the dictionary before appending to new list
PureKeyList = []
for TempVar in UserKeyList:
    if ValidCypherList.count(TempVar) != 0:
        PureKeyList.append(TempVar)
        # Appending the purified list's number counterparts to a new list
KeyNumList = []
for TempLtr in PureKeyList:
    KeyNumList.append(CypherDict[TempLtr])
    # Now all lists are in proper form to start multiplying and generating key,
# KeyNumList
# NumCompList
# PureFoundList

    # Finding the shortest NumList to create while break with
TempList = []
TempList.append(len(KeyNumList))
TempList.append(len(NumCompList))
TempList.append(len(PureFoundList))
TempList.sort()
NumIndex = TempList[0]
    # Maths Time
MultiCypherList = []
TempVar1 = 0
# Shortest x CompName (itterator)
    # This while itterates through each index of CompName and multiplies it by each index (coupled eg. CompName[1]*List[4]*List[4]) and appends to new list.
while True:
    TempVar2 = 0
    TempVar3 = 0
    while True:
        NumCompList[TempVar1] = int(NumCompList[TempVar1])
        PureFoundList[TempVar2] = int(PureFoundList[TempVar2])
        KeyNumList[TempVar3] = int(KeyNumList[TempVar3])
        # Multiplies the first digit of the list by each other and adds to new list
        TempVar = NumCompList[TempVar1]*PureFoundList[TempVar2]*KeyNumList[TempVar3]
        # Making sure TempVar != 1
        if TempVar == 0:
            TempVar = TempVar + 1
        MultiCypherList.append(TempVar)
        TempVar2 = TempVar2 + 1
        TempVar3 = TempVar3 + 1
        if TempVar2 == (NumIndex):
            break
    TempVar1 = TempVar1 + 1
    if len(MultiCypherList) == NumIndex*len(NumCompList):
        break
MultiCypherList2 = MultiCypherList.copy()
    # Adding more random values to multicypherlist for ULTRA long passwords
UserCheck2 = input("Would you like a password which is < 50000? 'Yes' or 'No' *This is just for fun*:   ")
UserCheck2 = str.lower(UserCheck2)
if UserCheck2 == "yes":
    while True:
        for TempNum in KeyNumList:
            for TempVar in MultiCypherList2:
                MultiCypherList.append(TempNum*TempVar)
            MultiCypherList2 = MultiCypherList.copy()
        if len(MultiCypherList) > 50000:
            break
else:
    while True:
        for TempNum in KeyNumList:
            for TempVar in MultiCypherList2:
                MultiCypherList.append(TempNum*TempVar)
        if len(MultiCypherList) > 50000:
            break
    # Collecting how long user wants password to be
CypherLen = len(MultiCypherList) - 1
print("PLEASE KEEP LENGTH CONSTANT BETWEEN PASSWORDS")
print("Password length max of: "+str(CypherLen)+" digits long.")
print("10 digits long is good enough for most cases.")
PassLength = input("Please pick how long you'd like your password to be:   ")
PassLength = int(PassLength)
# Makes list of indexes to create more randomization in the eventual password
PreIndexList = []
TempIndex = 0
while True:
    TempIndex = TempIndex + 1
    PreIndexList.append(MultiCypherList[TempIndex])
    if TempIndex > 99:
        break
for TempNum in PreIndexList:
    if TempNum == 1:
        TempNum = TempNum + MultiCypherList[102]
    while TempNum > 1000:
        TempNum = TempNum / 2.435
RanIndexList = []
MemIndex = 0
TempVar = 0
for TempIndex in PreIndexList:
    TempVar3 = TempVar3 + 1
    if TempVar3 > PassLength:
        break
    TempIndex = TempIndex + MemIndex
    RanIndexList.append(MultiCypherList[TempIndex])
    MemIndex = TempIndex
if PassLength > len(RanIndexList):
    ShortList = []
            # Makes new list with only the length of PassLength wished
    for TempNum in range(104,(104 + PassLength)):
        ShortList.append(MultiCypherList[TempNum])
        # Simplififes ShortList into numbers under 27
    LowList = []
    for TempNum in ShortList:
        if TempNum <= 26:
            LowList.append(TempNum)
        while TempNum >= 27:
            TempNum = TempNum / 2
            if TempNum <= 26:
                LowList.append(TempNum)
    SimpleList = []
            # Rounds all numbers in list to whole numbers
    SimpleList = [round(x) for x in LowList]
            # Removes any 27s that may have occured by rounding up
    PureList = []
    for TempNum in SimpleList:
        if TempNum == 27:
            TempNum = TempNum - 1
        PureList.append(TempNum)
        # Runs PureList back through cypher to produce a password
    FinalList = []
    FinalStr = ""
    for TempNum in PureList:
        FinalList.append(CypherDictReverse[TempNum])
    FinalList[0] = FinalList[0].upper()
    for TempLtr in FinalList:
        FinalStr = FinalStr + TempLtr
        # Adding endings onto FinalStr
    FinalStr = FinalStr + "37_"
    print("")
    print("___________")
    print("")
    print("Your final "+str(PassLength)+" digit password is:")
    print(FinalStr)
    print("")
    print("NOTE: I added '37_' to the end and capatalised the first digit to fit password requirements.")
    print("")
    UserCheck = input("Press enter to exit.")
else:
    PassLength = int(PassLength)
    ShortList = []
        # Makes new list with only the length of PassLength wished
    for TempNum in range(14,(14 + PassLength)):
        ShortList.append(RanIndexList[TempNum])
        # Simplififes ShortList into numbers under 27
    LowList = []
    for TempNum in ShortList:
        if TempNum <= 26:
            LowList.append(TempNum)
        while TempNum >= 27:
            TempNum = TempNum / 2
            if TempNum <= 26:
                LowList.append(TempNum)
    SimpleList = []
            # Rounds all numbers in list to whole numbers
    SimpleList = [round(x) for x in LowList]
            # Removes any 27s that may have occured by rounding up
    PureList = []
    for TempNum in SimpleList:
        if TempNum == 27:
            TempNum = TempNum - 1
        PureList.append(TempNum)
            # Makes sure no number itterates too much in the final password
    for TempNum in PureList:
        TempIndex = PureList.index(TempNum)
        while PureList.count(TempNum) > 2:
            PureList[TempIndex] = PureList[TempIndex]*3.532
        while PureList[TempIndex] > 27:
            PureList[TempIndex] = PureList[TempIndex] / 2
        PureList[TempIndex] = round(PureList[TempIndex])
        if PureList[TempIndex] == 27:
            PureList[TempIndex] = PureList[TempIndex] - 1
           # Runs PureList back through cypher to produce a password
    FinalList = []
    FinalStr = ""
    for TempNum in PureList:
        FinalList.append(CypherDictReverse[TempNum])
    FinalList[0] = FinalList[0].upper()
    for TempLtr in FinalList:
        FinalStr = FinalStr + TempLtr
        # Adding endings onto FinalStr
    FinalStr = FinalStr + "37_"
    print("")
    print("___________")
    print("")
    print("Your final "+str(PassLength)+" digit password is:")
    print(FinalStr)
    print("")
    print("NOTE: I added '37_' to the end and capatalised the first digit to fit password requirements.")
    print("")
    UserCheck = input("Press enter to exit.")
