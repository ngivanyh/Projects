import csv, sys
from fx import *

if len(sys.argv) < 2:
    print("Usage: python quizzer.py quizzes.csv")

qa = []

with open(sys.argv[1]) as QA:
    reader = csv.DictReader(QA, delimiter='\t')
    for row in reader:
        qa.append(row)

LENQA = len(qa)

print("""
 ██████  ██    ██ ██ ███████ ███████ ███████ ██████  
██    ██ ██    ██ ██    ███     ███  ██      ██   ██ 
██    ██ ██    ██ ██   ███     ███   █████   ██████  
██ ▄▄ ██ ██    ██ ██  ███     ███    ██      ██   ██ 
 ██████   ██████  ██ ███████ ███████ ███████ ██   ██ 
    ▀▀                                               
""")

qcountTRES = getQCount("QUESTION COUNT: ", LENQA)
diffRES = getDiff("Choose difficulty of questions (H/M/E/N): ", qa, LENQA, qcountTRES)
TARGET = getTarget("Choose target score: ")

DIFF = diffRES[0]

if type(diffRES) is list and qcountTRES > diffRES[1]:
    QCOUNT = diffRES[1]
else:
    QCOUNT = qcountTRES

q = randomQ(QCOUNT, DIFF, LENQA, qa)

results = asker(q, QCOUNT)
printresults(results[0], results[1], TARGET)

# print(random.randrange(0, len(qa)))

# print(already_chosen)
