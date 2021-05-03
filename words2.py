import csv
words = []
with open('words1.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        words.append([row[0],row[1],row[2],int(row[3])])
    for i in words:
        ans = input(i[2]+": ")
        if ans == i[1]:
            print("correct")
        else:
            print("answer: "+i[1])

