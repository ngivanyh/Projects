import random

def randomQ(max, diff, lenqa, qa):
    already_chosen = [0] * lenqa
    
    qcount = 0; test = []
    while qcount != max:
        i = random.randrange(0, lenqa)
        cur = qa[i]
        if cur["diff"] == diff and already_chosen[i] == 0:
            print(cur)
            test.append(qa[random.randrange(0, lenqa)])
            already_chosen[i] = 1
            qcount += 1
            print(f"In {qcount} max: {max}")
    return test

def getqcount(prompt, lenqa):
    while True:
        temp = 0
        try: 
            temp = int(input(prompt))
            if temp > lenqa: raise ValueError
            return temp
        except ValueError: pass

def getdiff(prompt, qa, lenqa):
    while True:
        temp = ""
        try: 
            temp = input(prompt).upper()
            if temp not in ['H', 'M', 'S']:
                raise ValueError
            alldiff = [0] * 3
            for i in range(0, lenqa):
                cur = qa[i]
            return temp
        except ValueError: pass