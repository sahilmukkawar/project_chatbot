from string import punctuation as p
from os import system as sys
from random import choice
from replit import db

sys("clear")

def clean(string):
    final = ""
    for i in p: final = string.replace(i, "")
    return final.lower()

default = {
    "hi": ["Hello", "How are you", "Greetings", "Hi there"],
    "game": ["Games are fun", "I'm a pro gamer"],
    "replit": ["Replit is awesome", "I love Replit"],
    "coding": ["I'm Coded", "Coding is fun"],
    "how are you": ["Good", "Bored, how about you?"]
}

if "memory" not in list(db.keys()): db["memory"] = default
else:
    x = input("Bot: Welcome back!\n\nWrite \"reset\" if you want to reset my memory, otherwise press [ENTER]: ")
    if x == "reset": db["memory"] = default

a = choice(db["memory"]["hi"])
b = ""
last = ""
type = ""

while True:
    sys("clear")

    print("Write \"bad answer\" if you don't like what the bot said\n")
    
    print("Bot: " + a.capitalize())
    q = clean(input("\nYou: "))
    
    '''last = q
    if type == "new": db["memory"][b] = q'''

    if q:
        '''if q == last:
            x = []
            for i in db["memory"]:
                for j in db["memory"][i]: x.append([j, i])
            new = choice(x)
            a = new[0]
            b = new[1]
            type = "new"
            continue'''
        if q == "bad answer":
            ok = clean(input("\nBot: Sorry about that\nWhat keyword did I mess up on: "))
            l = []
            nid = False
            if ok not in list(db.keys()):
                db["memory"][ok] = []
                nid = True
            for i in db["memory"]:
                if i != ok: l.append((i, db["memory"][i]))
            l.insert(0, (ok, db["memory"][ok]))
            db["memory"] = dict(l)
            if nid:
                nq = clean(input("\nBot: What should I have said?: "))
                db["memory"][ok].append(nq)
            continue
        found = False
        for i in db["memory"]:
            if i in q:
                a = choice(db["memory"][i])
                found = True
                break
        if not found:
            nk = clean(input("\nBot: I don't know what you mean\nWhat keyword should I respond to?: "))
            nr = clean(input("How should I respond to \"" + nk + "\"?: "))
            db["memory"][nk] = []
            db["memory"][nk].append(nr)