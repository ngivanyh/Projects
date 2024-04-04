import csv, sys, fx

if len(sys.argv) < 2:
    print("Usage: python quizzer.py quizzes.csv")

qa = []

with open(sys.argv[1]) as QA:
    reader = csv.DictReader(QA)
    for row in reader:
        qa.append(row)

LENQA = len(qa)

QCOUNT = fx.getqcount("QUESTION COUNT: ", LENQA)
DIFF = input("Choose difficulty of questions (H/M/S/AH/AM/AS): ")


# fx.randomQ(qcount, DIFF, LENQA, qa)

# print(random.randrange(0, len(qa)))

# print(already_chosen)
