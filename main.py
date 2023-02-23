print("Day 39 Challenge")
print()
######################################################################

# this is working as intended. It's ugly but it's my code <3
#I did not look anywhere, not even the ASCII art. It's all mine :)
# I will now peek at the solution to understand what I missed with strings


######################################################################
#create a list of about 10 words (hard mode, make a user input for word)
#pick randomly for that list random.choice(list) <- will give a word from the list.
#prompt user to give a letter. if letter exists in word, show letter but all other not guessed letters are blank (show all blank letters at the beginning btw)
#show list of letters used. count wrong letters (6 lives)
#if all letters found, user wins
#extra point for showing hangman on the screen as lives are lost :)
######################################################################
#import
import os, time, random
#lists
wordList = [
  "girafe", "cochon", "tigre", "renard", "zebre", "loup", "chat", "vache",
  "elephant", "lion"
]
usedLetters = []

#variables
yourLives = 6

#subroutine
#word selection subroutine
def choose_word():
  wordChosen = random.choice(wordList)
#  print(wordChosen) #remove when build over
  return wordChosen
#add underscore subroutine
def add_tiret(mot):
  wordSeen = []
  for i in range(0, mot):
    wordSeen.append("_")
  return wordSeen
#remaining lives subroutine
def draw_hangman(state):
  if state == 6:
    print()
    print()
    print()
    print()
    print()
    print("____")
  elif state == 5:
    print()
    print(" |")
    print(" |")
    print(" |")
    print(" |")
    print("____")
  elif state == 4:
    print("________")
    print(" |")
    print(" |")
    print(" |")
    print(" |")
    print("____")
  elif state == 3:
    print("________")
    print(" |    |")
    print(" |")
    print(" |")
    print(" |")
    print("____")
  elif state == 2:
    print("________")
    print(" |    |")
    print(" |    O")
    print(" |")
    print(" |")
    print("____")
  elif state == 1:
    print("________")
    print(" |    |")
    print(" |    O")
    print(" |   /|\ ")
    print(" |")
    print("____")
  elif state == 0:
    print("________")
    print(" |    |")
    print(" |    O")
    print(" |   /|\ ")
    print(" |   / \ ")
    print("____")
  else:
    print("this should never happen")
  

#choose_word()
#main
#preparation
print("Welcome to the Hangman")
time.sleep(1)
print("a random word will be selected")
theWord = choose_word()
longueur = len(theWord)
wordHidden = add_tiret(longueur)
for i in range(0, longueur):
  print(f"{wordHidden[i]}", end="")
print()
#game loop
while yourLives > 0 and yourLives <10:
  time.sleep(2)
  os.system("clear")
  print(f"you have {yourLives} remaining chance(s)")
  theHangman = draw_hangman(yourLives)
  print()
  print(f"These are the letters you used:\n {usedLetters}")
  print()
  for i in range(0,longueur):
      print(f"{wordHidden[i]}", end="")
  print()
  print()
  yourChoice = input("choose a letter:\n> ").lower()
  if yourChoice in theWord:
  #  print(f"{yourChoice} is in {theWord}") #for testing
    print(f"the letter {yourChoice} is in the word") #for playing
    counter = 0
    counter2 = longueur
    for i in theWord:
    #  print(i)
      if i == yourChoice:
        wordHidden[counter] = yourChoice
      counter += 1
    for i in range(0,longueur):
  #    print(f"{wordHidden[i]}", end="")
      if wordHidden[i] == "_":
        counter2 -= 1
    print()
 #   print(counter2)
    #to get out of the game if all letters found, add 10 lives
    if counter2 == longueur:
      print("You found all the letters!")
      yourLives += 10
    print()
  else:
    if yourChoice in usedLetters:
      print("you already chose this one")
    else:
    #  print(f"{yourChoice} is not in {theWord}") #for testing
      print(f"the letter {yourChoice} is not in the word") #for playing
      yourLives -= 1
      #add in the list of used letters
      usedLetters.append(yourChoice)
#end game
if yourLives == 0:
  theHangman = draw_hangman(yourLives)
  print("you have no remaining chances, game over!")
  print(f"the answer was {theWord}")
elif yourLives >= 10:
  print(f"you won! you found all the letters in {theWord.upper()}! Hangman lives!")
  print("    \o/  ")
  print("     |")
  print("    / \ ")
else:
  print("this should never happen")
