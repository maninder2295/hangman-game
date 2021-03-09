import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ['beautiful','collaboration','mountains','hangman','oceans','fridge','transmission','uniform','gorgeous']
select_word = random.choice(word_list)

length = len(select_word)
display = []
end_of_game = False
lives = 6
print(f"Hint for the word {select_word[0]} _ _ {select_word[3]} _ _ _ _ _")

for _ in range(length):
    display += '_'

print(f"{' '.join(display)}")

while not False:
    user = input("Guess a letter: ")
    for i in range(length):
      letter = select_word[i]
      if letter == user:
          display[i] = letter


    if user not in select_word:
        print(stages[lives])
        lives -= 1
    
    print(f"{' '.join(display)}")

    if '_' not in display:
        end_of_game = True
        print("You Win!")
    elif lives == -1:
        end_of_game = True
        print("You loose!")