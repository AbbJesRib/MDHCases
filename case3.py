import requests
import os

url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"
r = requests.get(url)
celebrityDictionary = r.json()

line = "-----------------------------------\n"

artists = [i["name"] for i in celebrityDictionary["artists"]]


def errorproof():
    try:
        input("Press enter to continue.")
    except KeyboardInterrupt:
        pass


def printartists():
    print(line)
    for i in celebrityDictionary["artists"]:
        print("|", i["name"])
    print(line)
    errorproof()


def viewartist():
    artistname = ""
    while artistname.title() not in artists:
        try:
            artistname = input("Artist name > ")
        except KeyboardInterrupt:
            print("\nInvalid input")
    id = ""
    r = requests.get(url)
    celebrityDictionary = r.json()
    for i in celebrityDictionary["artists"]:
        if i["name"] == artistname.title():
            id = i["id"]
            break
    fetchedurl = url+id
    p = requests.get(fetchedurl)
    artistinfo = p.json()["artist"]
    print(line+"\n"+artistinfo["name"]+"\n"+line)
    for key, val in artistinfo.items():
        if key != "name":
            print(key.title()+"")
            for i in val:
                print("-", i)
    print(line)
    errorproof()


instructions = {
    "List": printartists,
    "View": viewartist,
    "Exit": exit,
}

while True:
    errormessage = ""
    os.system("cls")
    print(line+"List | List artists\nView | View artist profile\nExit | Exit application\n"+errormessage+line)
    try:
        whattodo = input(">> ").title()
        instructions[whattodo]()
    except (KeyError, KeyboardInterrupt, ValueError):
        errormessage = line+"\nError: Invalid input. Try again\n"
