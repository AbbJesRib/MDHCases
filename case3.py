import requests
import os
import sys

url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"
r = requests.get(url)
celebrityDictionary = r.json()

line = "-----------------------------------"


def printartists():
    for i in celebrityDictionary["artists"]:
        print("|", i["name"])


instructions = {
    "l": printartists
}
def clear(): os.system('cls')
