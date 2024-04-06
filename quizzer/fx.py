import random, colorama

colorama.init(autoreset=True)

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

def getdiff(prompt, qa, lenqa, qcount):
    diffop = ['H', 'M', 'E']
    while True:
        temp = ""
        try: 
            temp = input(prompt).upper()
            if temp not in diffop:
                raise ValueError
            alldiff = {"H": 0, "M": 0, "E": 0}
            for i in range(0, lenqa):
                cur_diff = qa[i]["diff"]
                if cur_diff in diffop:
                    alldiff[cur_diff] += 1
            if qcount > alldiff[temp]:
                print(f"Not enough questions for specified difficulty, max: {alldiff[temp]}")
            return [temp, alldiff[temp]]
        except ValueError: pass

def getans(index):
    while True:
        try:
            ans = input(f"Q{index}: ").upper()
            if ans not in ['A', 'B', 'C', 'D']:
                raise ValueError
            return ans
        except ValueError: pass

def qa(questions, qcount):
    mistaken = []
    for i in range(0, qcount):
        q = questions[i]
        print(f"{q['question']}")
        print(f"(A) {q['optionA']}")
        print(f"(B) {q['optionB']}")
        print(f"(C) {q['optionC']}")
        print(f"(D) {q['optionD']}\n")
        if q['answer'] != getans(i + 1):
            mistaken.append(i + 1)
            print(colorama.Fore.RED + "Wrong, try better next time!")
        else:
            print(colorama.Fore.GREEN + "Good job, you were right!")

    score = round(((qcount - len(mistaken)) / qcount * 100), 2)
    return [mistaken, score]

def printresults(mistaken_list, score):
    print(f"You scored {score} pts!\n")
    for i in range(0, len(mistaken_list)):
        print(f"Mistaken {i + 1}: Q{mistaken_list[i]}")