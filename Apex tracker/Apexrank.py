import requests
import csv
import datetime
import pandas as pd
import os

def addProfile(player,platform,auth,update=False):
    if(checkAuth(auth) == False):
        print("API key invalid, please enter a valid key")
        return()
    
    os.system('cls')
    today = datetime.datetime.now()
    rawData = getCurrentRank(player,platform,auth)
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

def compareProfile(player, platform,auth):
    if(checkAuth(auth) == False):
        print("API key invalid, please enter a valid key")
        return()

    os.system('cls')
    today = datetime.datetime.now()
    rawData = getCurrentRank(player,platform,auth)
    newData = [player, rawData["rankName"], rawData["rankDiv"], rawData["rankScore"], today, platform]

    oldData = findprofile(player)
    if (oldData == 0):
        print("Profile not found please add instead.")

    else:
        print("PLAYER STATISTICS")
        print("Username : " + player)
        print("Platform : " + platform)
        print("Rank Change: ")
        print(f"     Net Change = {int(newData[3]) - int(oldData[3])}")

        print("     ", end = "")
        for i in range(1,5):
            print(oldData[i], end = " ")

        print()
        print("                  ˅")
        print("                  ˅")

        print("     ", end = "")
        for i in range(1,5):
            print(newData[i], end = " ")

        print("\n\n\n")

def findprofile(player):
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

def getCurrentRank(player,platform,auth):
    url = "https://api.mozambiquehe.re/bridge?auth=" + auth + "&player=" + player + "&platform=" + platform

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers)

    data = response.json()

    output = {
                'rankScore' : data["global"]["rank"]["rankScore"], 
                'rankName'  : data["global"]["rank"]["rankName"], 
                'rankDiv'   : data["global"]["rank"]["rankDiv"]
             }


    return(output)

def updateProfile(player, platform,auth):
    deleteProfile(player)

    addProfile(player,platform,auth,True)

def deleteProfile(player):
    df = pd.read_csv('profiles.csv')
    df = df[~df.username.isin([player])]
    df.to_csv('profiles.csv', index=False)

def checkAuth(auth):
    url = "https://api.mozambiquehe.re/predator?auth=" + auth

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers)

    if(response.text == "Error: API key doesn't exist !"):
        return(False)

    return(True)
