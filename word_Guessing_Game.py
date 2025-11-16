

import random 

word_list = ["python", "programming", "computer", "algorithm", "database","HTML","CSS","JavaScript","Front-end","Back-end"]
random_item = random.choice(word_list)
length_word1 = len(random_item)

underscore = '_' * (length_word1 - 1)

print(f"The word you need to Guess start with {random_item[0] + underscore}\n")

def guessing_game(max_attempts, word, length):
    display = ['_'] * length
    guessed_letters = []
    attempts_remaining = max_attempts  # Track attempts separately
    
    while attempts_remaining > 0:  # Use while loop for better control
        print(f"Attempts remaining: {attempts_remaining}")
        guess = input("Enter a letter: ").lower()
        
        if guess in word.lower():
            print(f"Match: {guess}")
            guessed_letters.append(guess)
            
            # Update display with correct positions
            for i, letter in enumerate(word.lower()):
                if letter == guess:
                    display[i] = word[i]
            
            current_display = ''.join(display)
            print(f"Word: {current_display}")
            
            # Win condition
            if '_' not in display:
                print(f"🎉 You won! The word was: {word}")
                return
        else:
            # ONLY decrease attempts on wrong guesses
            attempts_remaining -= 1
            print(f"No match! Attempts left: {attempts_remaining}")
    
    # This only runs if player lost
    print(f" Game Over! The word was: {word}")

guessing_game(10, random_item, length_word1)



         


         
