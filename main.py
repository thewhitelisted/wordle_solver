from filtering import best_guess, filter_candidates
# from wordlists import get_word_list

def main():
    # list of words
    guesses = open('guess.txt').read().splitlines()
    answers = open('answers.txt').read().splitlines()
    while True:
        # get the guess from the user
        guess = input("Enter your guess (5-letter word): ").strip().lower()
        if len(guess) != 5 or not guess.isalpha():
            print("Invalid input. Please enter a 5-letter word.")
            continue
        # get the feedback from the user
        feedback = input("Enter feedback (G for green, Y for yellow, B for black): ").strip().upper()
        if len(feedback) != 5 or any(c not in 'GYB' for c in feedback):
            print("Invalid feedback. Please enter a 5-character string with G, Y, B.")
            continue
        answers = filter_candidates(answers, guess, feedback)
        # filter the possible words based on the guess and feedback
        best_guess_word = best_guess(guesses, answers)
        print(f"Best guess based on current information: {best_guess_word}")
        # update the possible words
        if len(possible) == 0:
            print("No possible words left. Please check your inputs.")
            break
        print(f"Remaining possible words: {len(answers)}")

if __name__ == "__main__":
    main()
