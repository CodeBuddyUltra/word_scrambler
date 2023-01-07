#randomizing so we do not have any idea of which word we are choosing
import random
# We are making a word game today
#It is called scramble
# I will give you a scrambled word and you have to guess the word
# We will be coding it using python
# SO lets get started!
#I have already chosen a list of words for level 1 and 2 of our game so that we do not waste any time choosing them!
print("Welcome to the game! This game is known as scramble. There are two levels. Level 2 is more difficult than level 1. You will be provided word meanings so that you can guess them more easily. But this game definitely will make you rack your brains!")

level_1 = {
  "Advantage": "To have a superior position", 
  "Inherent": "Firmly established by nature or habit",
  "Obsolete": "No longer practiced or accepted"
}
level_2 = {
  "Persuade": "To convince",
  "Regenerate": "Restore",
  "Remembrance": "A keepsake"
}

for key in level_1:
  keys = []
  keys.append(key)

for key in level_2:
  keys_2 = []
  keys_2.append(key)

word_1 = random.choice(keys)
word_2 = random.choice(keys_2)

print(str(len(word_1)) + " " + word_1 + "\n" + str(len(word_2)) + " " + word_2)

#So our randomizer is working!
#Now to scramble the letters

len_1 = len(word_1)
len_2 = len(word_2)

characters = []
characters_2 = []

jumbled_word_1 = []
jumbled_word_2 = []
for letter in word_1:
  characters.append(letter)

for letter in word_2:
  characters_2.append(letter)

while len(characters) < 0:
  jumbled_word_1.append(random.choice(characters))
  characters.remove(letters)

while len(characters_2) < 0:
  jumbled_word_2.append(random.choice(characters_2))
  characters.remove(letters_2)

#now adding up the letters
finished_word_1 = ''.join(jumbled_word_1)
finished_word_2 = ''.join(jumbled_word_2)


print(finished_word_1 + finished_word_2)
