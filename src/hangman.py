import random

HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']
words = '''ant baboon badger bat bear beaver camel cat clam cobra cougar
  coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
  lion lizard llama mole monkey moose mouse mule newt otter owl panda
  parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
  skunk sloth snake spider stork swan tiger toad trout turkey turtle
  weasel whale wolf wombat zebra'''.split()
  
def main():
    restart = True
    
    while restart:
        answer_guessed = False
        failed_to_guess = False
        answer = words[random.randint(0, len(words) - 1)]
        answer_display = ('_ ' * len(answer)).split()
        incorrect_guesses = ''
        full_guess = ''

        while not answer_guessed and not failed_to_guess:
            update_game_screen(answer_display, incorrect_guesses)
            guess = input("Guess a letter.\n")
            
            if guess in answer:
                full_guess += guess
                answer_guessed = set(full_guess) == set(answer)
                
                if answer_guessed:
                    print(f"Yes! The secret word was {answer}. You've won!")
                else:
                    for i in range(len(answer)):
                        if answer[i] == guess:
                            answer_display[i] = guess
            elif guess in incorrect_guesses:
                print("You have already guessed that letter.")
            else:
                incorrect_guesses += guess
                failed_to_guess = len(incorrect_guesses) == len(HANGMAN_PICS) - 1
                
                if failed_to_guess:
                    print(f"Oh no! The secret word was {answer}. You've lost!")
            
        restart = input("Play again? Y/N\n") in {'Y', 'y'}
    
def update_game_screen(answer_display, incorrect_guesses):
    print(' '.join(answer_display))
    print(HANGMAN_PICS[len(incorrect_guesses)])
    print(f"Incorrect guesses: {incorrect_guesses}")

if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    