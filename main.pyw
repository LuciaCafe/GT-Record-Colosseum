import tkinter
from gtFinderColosseum import searchUser, addVictoryList, addDefeatList

def extractUser():
    battleResult = searchUser(userName.get())
    showResult(battleResult)

def showResult(battleResult):
    messageResult.place(x=120)
    addDefeatButton.place(y=300)
    addVictoryButton.place(y=300)
    if(battleResult==1):
        result.set("Victory")
        messageResult.config(fg="green")
    if(battleResult==2):
        result.set("Defeat")
        messageResult.config(fg="red")
    if(battleResult==3):
        result.set("They haven't fought")
        messageResult.config(fg="grey")
        messageResult.place(x=30)
        addDefeatButton.place(y=140)
        addVictoryButton.place(y=140)

def addVictory():
    addVictoryList(userName.get())
    addDefeatButton.place(y=300)
    addVictoryButton.place(y=300)
    messageResult.place(x=120)
    result.set("Victory")
    messageResult.config(fg="green")

def addDefeat():
    addDefeatList(userName.get())
    addDefeatButton.place(y=300)
    addVictoryButton.place(y=300)
    messageResult.place(x=120)
    result.set("Defeat")
    messageResult.config(fg="red")

windowGT = tkinter.Tk()
userName = tkinter.StringVar()
result = tkinter.StringVar()
windowGT.geometry("350x180")
windowGT.configure(background="#181d20")
windowGT.resizable(0,0)
windowGT.iconbitmap("colosseum.ico")

title = tkinter.Label(windowGT, text= "Colosseum Records", bg="#181d20", font="Titillium 14", width=20)
title.config(fg="#EFB810")
title.place(x=63, y=10)

searchBar = tkinter.Entry(windowGT, font="Titillium 8", textvariable=userName)
searchBar.place(x=60, y=50, height=20, width=150)

searchButton = tkinter.Button(windowGT, text="Search User", font="Titillium 8", background="#EFB810", command= extractUser)
searchButton.place(x=220, y=50, height=20)

messageResult = tkinter.Label(windowGT, font="Titillium 25", bg="#181d20", textvariable=result)
messageResult.place(x=120, y=80)

addVictoryButton = tkinter.Button(windowGT, font="Titillium 8", bg="green", text="Add Victory", command=addVictory)
addVictoryButton.place(x=100, y=300, height=20)

addDefeatButton = tkinter.Button(windowGT, font="Titillium 8", bg="red", text="Add Defeat", command=addDefeat)
addDefeatButton.place(x=190, y=300, height=20)


windowGT.mainloop()
