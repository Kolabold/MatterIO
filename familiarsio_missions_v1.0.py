import random
import tkinter as tk
import tkinter.font as font

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
printsUM = "Prints: Defeat three Familiars."
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
items = ["Potion", "BigPotion", "Oil Can", "Antidote"]
status = ["Stop", "Poison", "Jinx","Forgetful","Stench"]
field = ["Firewall","Spotlight","Manna","Plague","Fog","Brew","LateBomb","Swap"]
fieldText = ["Protect","Illuminate","Heal","Infect","Obscure","Feed","Surprise","Send out"]
missions = "temp"

#buttons wahoooo

generateList = False
generateBingo = False
window = tk.Tk()
window.title("Kolabold's familiars.io Mission Generator")
window.configure(bg='black')
window.geometry("800x200")
myFont = font.Font(family="Helvetica",size=24)
hardModeLabel = tk.Label(text="Hard Mode activated",
                        foreground="white",
                        background="black",
                        font=myFont)
def missionList():
    global generateList
    global step2
    generateList = True
    button.pack_forget()
    button2.pack_forget()
    intro.pack_forget()
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
                hardModeLabel.pack()
        if missions.isdigit():
            missions = int(missions)
            window.destroy()



    confirmButton = tk.Button(window,
                              text="Confirm",
                              foreground="white",
                              background="black",
                              font=myFont,
                              command=confirmationPrompt)
    instruct.pack()
    entry.pack()
    confirmButton.pack()

def missionBingo():
    global generateBingo
    global step2
    generateBingo = True
    button.pack_forget()
    button2.pack_forget()
    intro.pack_forget()

intro = tk.Label(text="How would you like to generate your missions?",
                        foreground="white",
                        background="black",
                        font=myFont)
intro.pack()

button = tk.Button(window,
                   text="Generate List",
                   foreground="white",
                   background="black",
                   font=myFont,
                   command=missionList)
button.pack(side=tk.TOP)
button2 = tk.Button(window,
                   text="[UNIMPLEMENTED]",
                   foreground="white",
                   background="black",
                   font=myFont,
                   command=missionBingo)
button2.pack(side=tk.TOP)

window.mainloop()


#build lists

if hardMode == True:
    familiars += ["Wyvern"]
counter = 0
while counter < missions:
    temp = random.randint(0,8)
    if hardMode == True:
        temp = random.randint(0,9)
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
    if temp == 10:
        print("Defeat "+str(random.randint(1,3))+" PVE robots")
    if temp == 11:
        print("UNUSED STRING")
    if temp == 9: print(random.choice(impossible))

input()


