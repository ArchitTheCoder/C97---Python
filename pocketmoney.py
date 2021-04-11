intro = input("Introduce yourself: ")
count = 0
wordCount = 1

for word in intro:
    if (word == " "):
        wordCount = wordCount + 1

# Hi hello my name is archit

print("Your introduction was " + str(wordCount)  + " words long")