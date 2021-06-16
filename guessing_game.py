secret_word = "3"
guess = ""

guess_count = 0
guess_limit = 3
out_of_guess = False

while guess != secret_word and not(out_of_guess):
    if guess_count < guess_limit:
        guess = input("Enter your guess: \n")
        guess_count += 1
    else:
        out_of_guess = True

if out_of_guess:
    print("Out of guesses, you lose. \n")

else:
    print("You guessed correctly.\n")
