import csv, sys, fx

if len(sys.argv) < 2:
    print("Usage: python quizzer.py quizzes.csv")

qa = []

with open(sys.argv[1]) as QA:
    reader = csv.DictReader(QA)
    for row in reader:
        qa.append(row)

LENQA = len(qa)

qcountTRES = fx.getqcount("QUESTION COUNT: ", LENQA)
diffRES = fx.getdiff("Choose difficulty of questions (H/M/E): ", qa, LENQA, qcountTRES)

DIFF = diffRES[0]

if qcountTRES > diffRES[1]:
    QCOUNT = diffRES[1]
else:
    QCOUNT = qcountTRES

q = fx.randomQ(QCOUNT, DIFF, LENQA, qa)

fx.printq(q, QCOUNT)

# print(random.randrange(0, len(qa)))

# print(already_chosen)
