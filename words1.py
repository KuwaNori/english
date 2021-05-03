import csv
import random

# create hollow list for words quiz
words = []

# open the csv file which contain words
with open('words1.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    number = int(input("How many words for quiz: "))

    for row in spamreader:
        words.append([row[0],row[1],row[2]])

quizs = random.sample(words, number)
good = 0
for i in quizs:
    ans = input(i[1]+": ")
    if ans == i[2]:
        print("correct")
        good+=1
    else:
        print("answer: "+i[2])
print("\nFinal result: "+str(good) + "/" +str(number))
