import random, sys, math


print("Welcome to the number guessing game...")
print("Please choose your range for the numbers by entering the upper and lower limit\n")
lower_limit = input("Enter lower limit: ")

try:
    lower_limit = int(lower_limit)
except Exception as e:
    sys.exit(f"Error occurred: excepted an integer or number input")

if lower_limit < 0:
    sys.exit(f"Error occurred: excepted a positive integer or number input for the lower limit but a negative one was provided")

upper_limit = input("Enter upper limit: ")

try:
    upper_limit = int(upper_limit)
except Exception as e:
    sys.exit(f"Error occurred: excepted an integer or number input")

if upper_limit < 0:
    sys.exit(f"Error occurred: excepted a positive integer or number input for the upper limit but a negative one was provided")

if lower_limit >= upper_limit:
    sys.exit(f"Error occurred: lower limit should be a positive integer that is less than upper limit")

print(f"\nYou have provided a range of {lower_limit} to {upper_limit}\n")

minimum_number_of_guesses = math.ceil(math.log2(upper_limit - lower_limit + 1))
number_to_be_guessed = random.randint(lower_limit, upper_limit)

print(f"\t \t You have only {minimum_number_of_guesses} times to guess the number!\n")

number_of_guesses = 0
user_guessed_within_allowed_range = False

while(number_of_guesses < minimum_number_of_guesses):
    user_guess = input(f"Guess and enter a number from {lower_limit} to {upper_limit}: ")

    try:
        user_guess = int(user_guess)
    except Exception as e:
        sys.exit(f"Error occurred: excepted an integer or number input")

    # print("Try again!")
    if user_guess > number_to_be_guessed:
        print("Try Again! You guessed too high\n")
    elif(user_guess < number_to_be_guessed):
        print("Try Again! You guessed too small\n")

    number_of_guesses += 1

    if(number_to_be_guessed == user_guess):
        print("\nCongratulations!\n")
        print(f"number of guesses made: {number_of_guesses}.")
        user_guessed_within_allowed_range = True
        break

if not user_guessed_within_allowed_range:
    print("\nBetter Luck Next Time!\n")
    print(f"number of guesses made: {number_of_guesses}, correct guess: {number_to_be_guessed}")

