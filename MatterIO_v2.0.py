import random
import tkinter as tk
from tkinter import *
import tkinter.font
import pyglet

#locales
battleMountain = "at the hill deep within the northern mines"
cultistCave = "inside the mysterious ritual cave"
technoPyramid = "at the mechanical pyramid"
silo = "on top of the metal cylinder"
telescope = "in front of the telescope"
docks = "at the docks"
capeIsland = "on the small island in front of the waterfall"
southeastIsland = "on the hill on the southeast island"
flowerPair = "at the pair of flowers in the southernmost underground"
locales = [battleMountain, cultistCave, technoPyramid, silo, telescope, docks, capeIsland, southeastIsland, flowerPair]

#impossible
crescentPuzzle = "Solve the puzzle in the northeastern rock garden"
activateTV = "Activate every TV"
readSigns = "Read every sign"
bunionLog = "Push the log to reveal Bunion's hidden garden"
ineffectiveAttack = "Defeat a Robot-type familiar using a Hex-type attack"
impossible = [crescentPuzzle, activateTV, readSigns, bunionLog, ineffectiveAttack]

#Unique Missions
alphaUM = "Alpha: Use Ward to remove an opponent's buffs 3 times"
banditUM = "Bandit: Use Nap while inflicted with STOP"
carbonUM = "Carbon: Counter 3 attacks with Firewall"
cobbyUM = "Cobby: Use Nap while the field is foggy"
daemonUM = "Daemon: OHKO 2 wild Familiars using Burn-Back or Burn-Back 2"
garyUM = "Gary: Defeat an opponent with Plague"
gooberUM = "Goober: Defeat 2 Water-type Familiars without switching"
patchUM = "Patch: Flee from 3 Familiars that have been inflicted with STOP."
printsUM = "Prints: Defeat three Familiars owned by a Red Automaton."
sensorUM = "Sensor: Get the highest roll on a Roulette attack twice"
seekerUM = "Seeker: Fill all five team slots with Seeker"
tentUM = "Tent: Mutual KO using Crash or Wallop"
toppleUM = "Topple: Heal 9 HP with Moonbeam"
wattUM = "Watt: Use Spotlight during Fog"
wispyUM = "Wispy: Defeat 3 Plush-type Familiars using Possess"
bunionUM = "Bunion: Heal Poison using Purify"
matterUM = "Matter: Defeat 3 Robot-type Familiars"
rascalUM = "Rascal: OHKO 2 wild Familiars using Spores or Spores 2"
kettleUM = "Kettle: Defeat 3 Cobby or Bunion using only Boil or Boil 2"
buoyUM = "Buoy: Take no damage from a Water-type attack"
uniqueMissions = [alphaUM, banditUM, carbonUM, cobbyUM, daemonUM, garyUM, gooberUM, patchUM, printsUM, sensorUM]
uniqueMissions += [seekerUM, tentUM, toppleUM, wattUM, wispyUM, bunionUM, matterUM, rascalUM, kettleUM, buoyUM]

#list building
hardMode = False
familiars = ['Alpha', 'Bandit', 'Carbon', 'Cobby', 'Daemon', 'Gary', 'Goober', 'Patch', 'Prints', 'Seeker', 'Sensor', 'Tent', 'Topple', 'Watt', 'Wispy', 'Bunion', 'Matter', 'Rascal', 'Kettle','Buoy']
items = ["Potion", "BigPotion", "Antidote"]
status = ["Stop", "Poison", "Jinx","Forgetful","Stench"]
field = ["Firewall","Spotlight","Manna","Plague","Fog","Brew","LateBomb","Swap"]
fieldText = ["Protect","Illuminate","Heal","Infect","Obscure","Feed","Surprise","Send out"]
missions = "temp"

#buttons wahoooo

generateList = False
generateBingo = False
window = tk.Tk()
window.title("MatterIO - Familiars.io mission generator by Kolabold")
bg = PhotoImage(file = "assets/background.png")
bgLabel = Label(window, image = bg)
bgLabel.place(x = -2, y = -2)
window.configure(bg='black')
window.resizable(False, False)
window.geometry("800x200")
window.iconbitmap("assets/icon.ico")
pyglet.font.add_file('assets/FamIo8.ttf')
myFont = tkinter.font.Font(family="FamIo8",size=24)
hardModeLabel = tk.Label(text="Hard Mode activated",
                        foreground="white",
                        background="black",
                        font=myFont)

#Step 2: Generate Mission List

def missionList():
    global generateList
    global step2
    generateList = True
    button.place_forget()
    button2.place_forget()
    intro.place_forget()
    instruct = tk.Label(text="How many missions to generate?",
                        foreground="white",
                        background="black",
                        font=myFont)
    entry = tk.Entry(foreground="white",
                     background="black",
                     font=myFont,
                     width=6)

    def confirmationPrompt():
        global missions
        missions = entry.get()
        if missions != int:
            if missions == "Legume":
                global hardMode
                hardMode = True
                hardModeLabel.place(x=400,y=140,anchor="center")
        if missions.isdigit():
            missions = int(missions)
            window.destroy()

    confirmButton = tk.Button(window,
                              text="Confirm",
                              foreground="white",
                              background="black",
                              font=myFont,
                              command=confirmationPrompt)
    instruct.place(x=400,y=20,anchor="center")
    entry.place(x=400,y=60,anchor="center")
    confirmButton.place(x=400,y=100,anchor="center")

#Step 2 but it's Bingo

def missionBingo():
    global generateBingo
    global step2
    generateBingo = True
    button.place_forget()
    button2.place_forget()
    intro.place_forget()
    instruct = tk.Label(text="Random Seed?",
                        foreground="white",
                        background="black",
                        font=myFont)
    entry = tk.Entry(foreground="white",
                     background="black",
                     font=myFont,
                     width=6)
    def confirmationPrompt():
        global randoSeed
        randoSeed = entry.get()
        if randoSeed != int:
            if randoSeed == "Legume":
                global hardMode
                hardMode = True
                hardModeLabel.place(x=400,y=140,anchor="center")
        if randoSeed.isdigit():
            randoSeed = int(randoSeed)
            random.seed(randoSeed)
            window.destroy()

    confirmButton = tk.Button(window,
                              text="Confirm",
                              foreground="white",
                              background="black",
                              font=myFont,
                              command=confirmationPrompt)
    instruct.place(x=400,y=20,anchor="center")
    entry.place(x=400,y=60,anchor="center")
    confirmButton.place(x=400,y=100,anchor="center")

#This is step 1, I wish I knew how to make this higher in the code so it wasn't confusing to navigate haha

intro = tk.Label(text="How would you like to generate your missions?",
                        foreground="white",
                        background="black",
                        font=myFont)
intro.place(x=400,y=20,anchor="center")

button = tk.Button(window,
                   text="Generate List",
                   foreground="white",
                   background="black",
                   font=myFont,
                   command=missionList)
button.place(x=400,y=60,anchor="center")
button2 = tk.Button(window,
                   text="Bingo Card",
                   foreground="white",
                   background="black",
                   font=myFont,
                   command=missionBingo)
button2.place(x=400,y=100,anchor="center")

window.mainloop()


#build lists
if generateList == True:
    if hardMode == True:
        familiars += ["Wyvern"]
    counter = 0
    while counter < missions:
        temp = random.randint(0,11)
        if hardMode == True:
            temp = random.randint(0,12)
        tempFam = random.choice(familiars)
        tempFam2 = random.choice(familiars)
        tempStat = random.randint(0,2)
        tempItem = random.randint(0,3)
        tempField = random.randint(0,6)
        counter += 1
        if temp == 0:
            print("Catch "+tempFam)
        if temp == 1:
            if hardMode == True:
                print("Raise " + tempFam + " to level " + str(random.randint(5, 20)))
            else:
                print("Raise "+tempFam+" to level "+str(random.randint(5,15)))
        if temp == 2:
            print("Defeat "+tempFam+" "+str(random.randint(1,5))+" time(s)")
        if temp == 3:
            print("Defeat "+tempFam+" using only "+tempFam2)
        if temp == 4:
            print("Inflict "+status[tempStat]+" on "+tempFam)
        if temp == 5:
            print("Use "+items[tempItem]+" on "+tempFam)
        if temp == 6:
            print(fieldText[tempField]+" "+tempFam+" with "+field[tempField])
        if temp == 7:
            print("Howdy "+random.choice(locales))
        if temp == 8:
            print(random.choice(uniqueMissions))
        if temp == 9:
            print("Defeat a Red Automaton")
        if temp == 10:
            print("Defeat "+str(random.randint(1,5))+" Blue Automaton(s)")
        if temp == 11:
            print("Defeat "+str(random.randint(1,3))+" Green Automaton(s)")
        if temp == 12:
            print(random.choice(impossible))

#Generate Bingular My Dude

if generateBingo == True:
    bingoAmount = 0
    gridPosX = 0
    gridPosY = 0
    bingoList = []
    bingoRepeat = False
    autoGreen = False
    autoBlue = False
    autoRed = False
    window = tk.Tk()
    windowTitle = "MatterIO Bingo Card Seed: " + str(randoSeed)
    window.resizable(False, False)
    window.title(windowTitle)
    window.iconbitmap("assets/icon.ico")
    window.configure(bg='black')
    myFont = tkinter.font.Font(family="FamIo8", size=16)
    def colourChange(event):
        if event.widget['bg'] == 'black':
            event.widget['bg'] = 'blue'
            return
        if event.widget['bg'] == 'blue':
            event.widget['bg'] = 'red'
            return
        if event.widget['bg'] == 'red':
            event.widget['bg'] = 'black'
            return
    #Generate text
    while bingoAmount < 25:
        temp = random.randint(0,11)
        if hardMode == True:
            temp = random.randint(0,12)
        tempFam = random.choice(familiars)
        tempFam2 = random.choice(familiars)
        tempStat = random.randint(0,2)
        tempItem = random.randint(0,2)
        tempField = random.randint(0,6)
        if temp == 0:
            bingoText = str("Catch "+tempFam)
        if temp == 1:
            if hardMode == True:
                bingoText = str("Raise " + tempFam + " to level " + str(random.randint(5, 20)))
            else:
                bingoText = str("Raise "+tempFam+" to level "+str(random.randint(5,15)))
        if temp == 2:
            bingoText = str("Defeat "+tempFam+" "+str(random.randint(1,5))+" time(s)")
        if temp == 3:
            bingoText = str("Defeat "+tempFam+" using only "+tempFam2)
        if temp == 4:
            bingoText = str("Inflict "+status[tempStat]+" on "+tempFam)
        if temp == 5:
            bingoText = str("Use "+items[tempItem]+" on "+tempFam)
        if temp == 6:
            bingoText = str(fieldText[tempField]+" "+tempFam+" with "+field[tempField])
        if temp == 7:
            bingoText = str("Howdy "+random.choice(locales))
        if temp == 8:
            bingoText = str(random.choice(uniqueMissions))
        if temp == 9:
            if autoRed == True:
                bingoRepeat = True
            if autoRed == False:
                bingoText = str("Defeat a Red Automaton")
                autoRed = True
        if temp == 10:
            if autoBlue == True:
                bingoRepeat = True
            if autoBlue == False:
                bingoText = str("Defeat "+str(random.randint(1,5))+" Blue Automaton(s)")
                autoBlue = True
        if temp == 11:
            if autoGreen == True:
                bingoRepeat = True
            if autoGreen == False:
                bingoText = str("Defeat "+str(random.randint(1,3))+" Green Automaton(s)")
                autoGreen = True
        if temp == 12:
            bingoText = str(random.choice(impossible))
        if bingoText in bingoList:
            bingoRepeat = True
        if bingoRepeat == False:
            bingoList += [bingoText]
            bingoAmount += 1
            bingoButton = tk.Button(window,
                                    text=bingoText,
                                    foreground="white",
                                    background="black",
                                    wraplength=150,
                                    font=myFont,
                                    )
            bingoButton.bind('<Button-1>', colourChange)
            bingoButton.config(height=10, width=14)
            bingoButton.grid(column=gridPosX, row=gridPosY)
            gridPosX += 1
            if gridPosX == 5:
                gridPosX = 0
                gridPosY += 1
        if bingoRepeat == True:
            bingoRepeat = False
    for x in bingoList:
        print(x)
input()


