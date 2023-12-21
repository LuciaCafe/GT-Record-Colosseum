
while True:
    userName = input("ingresa el nombre de usuario del jugador a buscar: ")
    userName = userName
    userNameFound = False

    victorys = open("victorys.txt", "r")
    victorysLine = victorys.readline()

    while victorysLine!='':
        if(victorysLine == userName + "\n"):
            print("Ya has ganado contra este jugador")
            userNameFound = True
        victorysLine = victorys.readline()
    victorys.close()

    if(userNameFound == False):
        defeats = open("defeats.txt", "r")
        defeatsLine = defeats.readline()

        while defeatsLine!='':
            if(defeatsLine == userName + "\n"):
                print("Ya has perdido contra este jugador")
                userNameFound = True
            defeatsLine = defeats.readline()
        defeats.close()

    if(userNameFound == False):
        decision = input("No has peleado contra este jugador.\n¿Deseas registrarlo?\n1) Marca tu victoria\n2) Marca tu derrota\n3) No registrar\n")

        if(decision == "1"):
            victorys = open("victorys.txt", "a")
            victorys.write(userName + "\n")
            victorys.close()

        if(decision == "2"):
            defeats = open("defeats.txt", "a")
            defeats.write(userName + "\n")
            defeats.close()


input()


