"""
    Word Guess Game (2 players)
"""

# Data
words = {"Fruit": ("pineapple", "pumpkin"),
         "Vegetable": ("cucumber", "potato", "beats"),
         "Animal": ("karakul", "penguin", "jiraffe")}
for cat in words.keys():
    print(cat, end=", ")  # print categories
print()
categoryIndex = int(input("Please choose index of a word category (0 to " + str(len(words.keys()) - 1) + "): "))
categoryKey = list(words).pop(categoryIndex)
for w in words[categoryKey]:
    print(str(len(w)) + " symbols", end=", ")  # print words to choose from
print()
wordIndex = int(input("Please choose index of a word (0 to " + str(len(words[categoryKey]) - 1) + "): "))
print("---------------------------------------------------------------------------------------------------------------")
word = words[categoryKey][wordIndex]  # get a playing word
print("----------------Game----------------")
guessedCharacters = set()
userPoints = [0, 0]
playing = True
while playing:
    # Print a word
    print("\t\t", end="")
    playing = False
    for c in word:
        if c in guessedCharacters:
            print(c, end="")
        else:
            playing = True
            print("_", end="")
    print()
    if not playing: break
    # User plays
    letter = chr(0)
    userPlaying = len(guessedCharacters) % 2 + 1  # 1 if user 1 and 2 if user 2
    while True:
        letter = input("User " + str(userPlaying) + " guesses a character: ").lower()[0] #get letter from user
        if 'z' < letter < 'a': # check letter ASCII
            print("This is not a letter! Try again")
            continue
        if letter not in guessedCharacters: # if letter was not used
            guessedCharacters.add(letter)
            break
        else:
            print("You've already used this letter! Try again") # letter already used
            continue
    points = 0
    if letter in word:  # if word has this symbol we should count points
        for l in word:
            if l == letter:
                points += 1
    print("User {0} gets {1} point(s)!".format(userPlaying, points))
    userPoints[userPlaying-1] += points

if userPoints[0]>userPoints[1]:
    print("User 1 WON!")
elif userPoints[0]<userPoints[1]:
    print("User 2 WON!")
else:
    print("\n=======================DRAW=======================")
print("#######################################")
print("----------------Results----------------")
print("#######################################")
for i in range(0,len(userPoints)):
    print("User {0} has {1} points".format(i+1,userPoints[i]))