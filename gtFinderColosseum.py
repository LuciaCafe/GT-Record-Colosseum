defeats = open("defeats.txt", "a")
defeats.close()
victorys = open("victorys.txt", "a")
victorys.close() 

def searchUser(userName):

    victorys = open("victorys.txt", "r")
    victorysLine = victorys.readline()

    while victorysLine!='':
        if(victorysLine == userName + "\n"):
            return 1
        victorysLine = victorys.readline()
    victorys.close()

    defeats = open("defeats.txt", "r")
    defeatsLine = defeats.readline()

    while defeatsLine!='':
        if(defeatsLine == userName + "\n"):
            return 2
        defeatsLine = defeats.readline()
    defeats.close()

    return 3

def addVictoryList(userName):
    foundUser = False
    victorys = open("victorys.txt", "r")
    victorysLine = victorys.readline()

    while victorysLine!='':
        if(victorysLine == userName + "\n"):
            foundUser = True
        victorysLine = victorys.readline()
    victorys.close()

    if(foundUser == False):
        victorys = open("victorys.txt", "a")
        victorys.write(userName + "\n")
        victorys.close()

def addDefeatList(userName):
    foundUser = False
    defeats = open("Defeats.txt", "r")
    defeatsLine = defeats.readline()

    while defeatsLine!='':
        if(defeatsLine == userName + "\n"):
            foundUser = True
        defeatsLine = defeats.readline()
    defeats.close()

    if(foundUser == False):
        defeats = open("defeats.txt", "a")
        defeats.write(userName + "\n")
        defeats.close()