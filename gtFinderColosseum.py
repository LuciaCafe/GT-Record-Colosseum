createTXT = open("enemyUser.txt", "a")
createTXT.close()

def searchUser(userName):
    enemy = open("enemyUser.txt", "r")
    enemyUser = enemy.readline()
    enemyVictorys = enemy.readline()
    enemyDefeats = enemy.readline()
    
    while enemyUser!='':
        if(enemyUser == userName + "\n"):
            return enemyVictorys, enemyDefeats
        enemyUser = enemy.readline()
        enemyVictorys = enemy.readline()
        enemyDefeats = enemy.readline()
    enemy.close()

    enemy = open("enemyUser.txt", "a")
    enemy.write(userName + "\n")
    enemy.write("0" + "\n")
    enemy.write("0" + "\n")
    enemy.close()

    return "0", "0"

def add(userName, id):
    enemy = open("enemyUser.txt", "r")
    enemyUser = enemy.readline()
    enemyVictorys = enemy.readline()
    enemyDefeats = enemy.readline()
    cont = 0
    cantV = 0
    cantD = 0

    while enemyUser!='':
        if(enemyUser == userName + "\n"):
            break
        enemyUser = enemy.readline()
        enemyVictorys = enemy.readline()
        cantV = enemyVictorys
        enemyDefeats = enemy.readline()
        cantD = enemyDefeats
        cont = cont + 3
    enemy.close()

    with open('enemyUser.txt') as file:
        lines = file.readlines()
    if(id == 1):
        lines[cont+1] = str(int(enemyVictorys.replace("\n", "")) + 1 ) + "\n"
    if(id == 2):
        lines[cont+2] = str(int(enemyDefeats.replace("\n", "")) + 1) + "\n"

    clear = open("enemyUser.txt", "w")
    clear.close()

    newFile = open("enemyUser.txt", "a")
    for i in lines:
        newFile.write(i)
    newFile.close()

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


""" def extractTXT():
    victorys = open("victorys.txt", "")
    victorysLine = victorys.readline()
    enemys = open("enemyUser.txt", "a")

    while victorysLine!='':
        enemys.write(victorysLine)
        enemys.write("1\n")
        enemys.write("0\n")
        victorysLine = victorys.readline()
    victorys.close()

    clear = open("victorys.txt", "w")
    clear.close()

    defeats = open("defeats.txt", "r")
    defeatsLine = defeats.readline()

    while defeatsLine!='':
        enemys.write(defeatsLine)
        enemys.write("0\n")
        enemys.write("1\n")
        defeatsLine = defeats.readline()
    defeats.close()

    clear = open("defeats.txt", "w")
    clear.close()
    
    enemys.close() """


""" def searchUser(userName):

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

    return 3 """

"""def add(userName, id):
    enemy = open("enemyUser.txt", "r")
    enemyUser = enemy.readline()
    enemyVictorys = enemy.readline()
    enemyDefeats = enemy.readline()
    cont = 0

    while enemyUser!='':
        if(enemyUser == userName + "\n"):
            if(id == 1):
                enemy = str(int(enemyVictorys) + 1)
        enemyUser = enemy.readline()
        enemyVictorys = enemy.readline()
        enemyDefeats = enemy.readline()
        cont = cont + 3
    enemy.close() """