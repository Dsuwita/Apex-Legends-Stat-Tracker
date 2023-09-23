import requests
import csv
import datetime
import pandas as pd
import os

def addProfile(player,platform,update=False):
    "'Gets player data and stores it inside a csv file.'"

    os.system('cls')
    
    today = datetime.datetime.now()
    rawData = getCurrentRank(player,platform)

    if(rawData == False):
        return()

    data = [player, rawData["rankName"], rawData["rankDiv"], rawData["rankScore"], today, platform]

    if (findprofile(player) == 0):
        with open('profiles.csv', mode ='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)

        if(update == False):
            print("Profile added successfully.")
        else:
            print("New session initialized for " + player + ".")

    else:
        print("Profile already exists please initialize a session instead.")

def compareProfile(player, platform):
    "'Shows the current statistics comparison to when the session was initialized.'"

    os.system('cls')

    today = datetime.datetime.now()
    rawData = getCurrentRank(player,platform)

    if(rawData == False):
        return()

    newData = [player, rawData["rankName"], rawData["rankDiv"], rawData["rankScore"], today, platform]

    oldData = findprofile(player)
    if (oldData == 0):
        print("Profile not found please add instead.")

    else:
        NetChange = int(newData[3]) - int(oldData[3])

        print("PLAYER STATISTICS")
        print("Username : " + player)
        print("Platform : " + platform)
        print("Rank Change: ")
        print(f"     Net Change = {NetChange}")

        print("     ", end = "")
        for i in range(1,5):
            print(oldData[i], end = " ")

        print()
        print("                  ˅")
        print("                  ˅")

        print("     ", end = "")
        for i in range(1,5):
            print(newData[i], end = " ")
        
        print("\n\n")

        games = getGameHistory(player)
        
        
        print("Games played this session:")
        if(games != None):
            for i in games:
                print(f'{i[1]} RP as {i[2]}')

            print(f'{NetChange/len(games)} RP per game on average (Current Session)')

        else:
            print("No games recorded yet.")

def findprofile(player):
    "'Checks if a profile exists in the database'"

    os.system('cls')

    with open('profiles.csv', mode ='r') as file:
        csvFile = csv.reader(file)

        profiles = []
        for lines in csvFile:
            profiles.append(lines)

    for i in range(len(profiles)):
        if (profiles[i][0] == player):
            return(profiles[i])

    return(0)

def getCurrentRank(player,platform):
    "'Requests a user's profile from server and returns it.'"

    url = "https://api.mozambiquehe.re/bridge?auth=" + auth + "&player=" + player + "&platform=" + platform

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers)

    if(response.text == "Error: API key doesn't exist !"):
        print("API key invalid, please enter a valid key")
        return(False)

    data = response.json()

    if('Error' in data):
        print("Player not found, Please try again.")
        return(False)


    output = {
                'rankScore' : data["global"]["rank"]["rankScore"], 
                'rankName'  : data["global"]["rank"]["rankName"], 
                'rankDiv'   : data["global"]["rank"]["rankDiv"],
                'legend'    : data["legends"]["selected"]["LegendName"]
             }

    return(output)

def updateProfile(player, platform):
    "'Resets a profile and clears all games related to that profile.'"

    clearGames(player)

    deleteProfile(player)

    addProfile(player,platform,True)

def deleteProfile(player):
    "'Deletes a profile from database.'"

    os.system('cls')
    if(not findprofile(player)):
        print("No such profile has been added, please try again.")
        return()
    
    clearGames(player)
    df = pd.read_csv('profiles.csv')
    df = df[~df.username.isin([player])]
    df.to_csv('profiles.csv', index=False)
    
    print("Profile " + player + " has been successfully deleted.")

def recordGame(player,platform):
    "'Records RP change and legend name in the database'"

    os.system('cls')

    oldData = findprofile(player)
    if (findprofile(player) == 0):
        print("Profile not found, please add profile first.")
        return()

    rawData = getCurrentRank(player,platform)

    if(rawData == False):
        return()

    games = getGameHistory(player)
    sumOfGames = 0

    if(games != None):
        for i in games:
            sumOfGames += int(i[1])

    data = [player,int(rawData["rankScore"]) - (int(oldData[3]) + sumOfGames), rawData["legend"]]

    with open('games.csv', mode ='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

    print("Game recorded successfully.")

def clearGames(player):
    "'Deletes all games related to a profile.'"

    df = pd.read_csv('games.csv')
    df = df[~df.username.isin([player])]
    df.to_csv('games.csv', index=False)

def getGameHistory(player):
    "'Gets all the games a profile has played from database.'"

    with open('games.csv', mode ='r') as file:
        csvFile = csv.reader(file)
        allRecords = []

        playerRecord = []

        for lines in csvFile:
            allRecords.append(lines)

        for i in range(len(allRecords)):
            if (allRecords[i][0] == player):
                playerRecord.append(allRecords[i])
    
        if(playerRecord == []):
            return(None)
        
        return(playerRecord)

def getAuth():
    "'Gets Auth key from auth.txt.'"
    
    global auth
    data = open("auth.txt", "r")
    auth = data.read()

#Gets auth key when program is initialized.
getAuth()

#testing how this works