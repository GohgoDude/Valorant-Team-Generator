from tkinter import *
from tkinter import ttk
import random
import json

# Defining Functions

def randomTeam(playerNames):
    random.shuffle(playerNames)
    length = len(playerNames)
    middle_index = length//2
    teamA = playerNames[:middle_index]
    teamB = playerNames[middle_index:]
    return teamA, teamB

def jsonConvert(names, info):
    ids = []
    for name in names:
        ids.append(info[name])
    return ids

def teamWeight(values):
    total = 0
    for number in values:
        total += number
    length = len(values)
    return round(total/length, 2)

def displayResult(players1, players2, weight1, weight2):
    showResultsA.config(text = "Team A consists of " + ", ".join(players1) + ". " + "Weight: " + str(weight1))
    showResultsB.config(text = "Team B consists of " + ", ".join(players2) + ". " + "Weight: " + str(weight2))

def makeResult():
    playerList = []
    for player in playerObject:
        playerList.append(player.get())
    teamA, teamB = randomTeam(playerList)

    idsA = jsonConvert(teamA, players)
    idsB = jsonConvert(teamB, players)

    weightA = teamWeight(idsA)
    weightB = teamWeight(idsB)

    displayResult(teamA, teamB, weightA, weightB)

def closeWindow(window):
    window.destroy()

# Base Variables

itemCount = 10
maxRow = itemCount//2

playerObject = []
dropObject = []
players = {}

# Initializing GUI

root = Tk()
root.title("Valorant Team Generator")
root.geometry('800x450')

notebook = ttk.Notebook(root)
notebook.pack()

general = Frame(notebook, width=800, height=450)
settings = Frame(notebook, width=800, height=450)

general.pack(fill="both", expand=1)
settings.pack(fill="both", expand=1)

notebook.add(general, text="General")
notebook.add(settings, text="Settings")

# Generating GUI elements
# General

showResultsA = Label(general, text="Team A consists of N/A", width=70, height=1)
showResultsA.grid(row=maxRow+1, column=0)
showResultsB = Label(general, text="Team B consists of N/A", width=70, height=1)
showResultsB.grid(row=maxRow+2, column=0)

with open('database.json','r') as f:
    players = json.load(f)

OptionList = list(players.keys())

for i in range(itemCount):
    playerObject.append(StringVar(root))

    dropObject.append(OptionMenu(general, playerObject[i], *OptionList))
    dropObject[i].config(width=20, height=1)
    dropObject[i].grid(row=i%maxRow, column=i//maxRow)

generateResults = Button(general, text="Generate Teams", command=makeResult)
generateResults.grid(row=maxRow, column=0)

closeProgram = Button(general, text="Quit", command=lambda: closeWindow(root))
closeProgram.grid(row=maxRow, column=1)

# Settings

root.mainloop()
