import tkinter
from gtFinderColosseum import searchUser, add

def Search():
    if(userName.get() != ''):
        cantVictorys, cantDefeats = searchUser(userName.get())
        resultVictorys.set(cantVictorys)
        resultDefeats.set(cantDefeats)
        frameVictorys.place(y=80)
        frameDefeats.place(y=80)
    else:
        frameVictorys.place(y=200)
        frameDefeats.place(y=200)

def addVictory():
    cant = resultVictorys.get()
    cant = int(cant) + 1
    resultVictorys.set(str(cant))

    add(userName.get(), 1)

def addDefeat():
    cant = resultDefeats.get()
    cant = int(cant) + 1
    resultDefeats.set(str(cant))

    add(userName.get(), 2)

windowGT = tkinter.Tk()
userName = tkinter.StringVar()
result = tkinter.StringVar()
resultVictorys = tkinter.StringVar()
resultDefeats = tkinter.StringVar()
windowGT.title("GT Collo Records")
windowGT.geometry("350x200")
windowGT.configure(background="#181d20")
windowGT.resizable(0,0)
windowGT.wm_attributes("-topmost", True)
windowGT.iconbitmap("./icon/colosseum.ico")

title = tkinter.Label(windowGT, text= "Colosseum Records", bg="#181d20", font="Titillium 14", width=20)
title.config(fg="#EFB810")
title.place(x=63, y=10)

searchBar = tkinter.Entry(windowGT, font="Titillium 8", textvariable=userName)
searchBar.place(x=60, y=50, height=20, width=150)

searchButton = tkinter.Button(windowGT, text="Search User", font="Titillium 8", background="#EFB810", command=Search)
searchButton.place(x=220, y=50, height=20)

frameVictorys = tkinter.Frame(windowGT, width=145, height=110, background="#EFB810")
frameVictorys.place(x=35, y=200)

frameVictorysContainer = tkinter.Frame(frameVictorys, width=141, height=110, background="#181d20")
frameVictorysContainer.place(x=0, y=0)

labelVictory = tkinter.Label(frameVictorysContainer, font="Titillium 20", text="Victorys", bg="#181d20", fg="#43E113")
labelVictory.place(x=30, y=0)

numberVictorys = tkinter.Label(frameVictorysContainer, font="Titillium 18", textvariable=resultVictorys, background="#181d20", fg="#43E113")
numberVictorys.place(x=70, y=41)

addVictoryButton = tkinter.Button(frameVictorysContainer, 
                                    font="Titillium 8", 
                                    text="Add 1", 
                                    background="green", 
                                    fg="#000000",
                                    command=addVictory,
                                    )
addVictoryButton.place(x=60, y=82, height=20)

frameDefeats = tkinter.Frame(windowGT, width=145, height=110)
frameDefeats.place(x=180, y=200)

frameDefeatsContainer = tkinter.Frame(frameDefeats, width=145, height=110, background="#181d20")
frameDefeatsContainer.place(x=0, y=0)

labelDefeat = tkinter.Label(frameDefeatsContainer, font="Titillium 20", bg="#181d20", text="Defeats", fg="#E91A1A")
labelDefeat.place(x=6,y=1)

numberDefeats = tkinter.Label(frameDefeatsContainer, font="Titillium 18", textvariable=resultDefeats, background="#181d20", fg="#E91A1A")
numberDefeats.place(x=45, y=41)

addDefeatsButton = tkinter.Button(frameDefeatsContainer, 
                                    font="Titillium 8", 
                                    text="Add 1", 
                                    background="#DB2838", 
                                    fg="#000000",
                                    command=addDefeat,
                                    )
addDefeatsButton.place(x=35, y=82, height=20)

windowGT.mainloop()