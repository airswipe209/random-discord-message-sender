import time
import requests
import random
from tkinter import *
from tkinter import filedialog

Tk().withdraw()

print("RANDOM CHOICE + RANDOM TIME MESSAGE BOT")
print("--------------------------------------")
print("you'll be asked for your access token, path containing the log of messages you want to automate")
print("and the channel/guild you wan't this to work with")
print("as well as a time interval (in seconds) that you must enter, your messages will be sent at a random")
print("time within the given lapse. If you type 60, all your messages will randomly have sending delays of no more than")
print("1 minute. Could be 30 secs, 5 secs, and so on. You can put it to work for days or weeks even.")
print("--------------------------------------")
print("have fun!")

tkn = input("token: ")

channel = input("channel link: ")

interval = input("time interval -in seconds- to randomly choose from: ")

interval2 = int(interval)

filepath = filedialog.askopenfilename()

with open(filepath, "r") as fa:
    qts = fa.read().split(',')

for qt in qts:
    x = random.randint(0,interval2)
    qtnum = random.randint(0, len(qts) - 1)
    dawg = (qts[qtnum])

    payload = {
        'content': dawg
    }

    header = {
        'authorization': tkn
    }

    r = requests.post(channel,
     data=payload, headers=header)
    time.sleep(x)
