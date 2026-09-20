import random

print("Welcome to the die roll game!")
print("Type 'bye' to quit at any time")


def safe_input(prompt):
    user_input = input(prompt)
    if user_input.strip().lower() == "bye":
        print("Goodbye!")
        raise SystemExit
    return user_input


def printbalance():
    print(f"Your current balance is: ${balance}")

def getpurchaseamount():
    print("Each die costs $10.")

    while True:
        try:
            user_input = safe_input("Enter the number of die you would like to purchase: ")
            boughtdice = int(user_input)
            if boughtdice <= 0:
                print("Invalid input. Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    if boughtdice > balance // 10:
        print("You do not have enough balance to purchase that many die.")
        return getpurchaseamount()
    return boughtdice

def playgame(boughtdice):
    for i in range(boughtdice):

        while True:
            try:
                user_input = safe_input(f"Enter your prediction for die {i + 1} (1-6): ")
                prediction = int(user_input)
                if prediction < 1 or prediction > 6:
                    print("Invalid input. Please enter a positive integer 1-6.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a positive integer 1-6.")

        roll = random.randint(1, 6)
        print(f"Die {i + 1} rolled: {roll}")
        if prediction == roll:
            global balance
            print("Congratulations! You guessed correctly. Balance increased from $", balance, "to $", balance + 20)
            balance += 20  # Win $20 for a correct guess
        else:
            print("Sorry, you guessed incorrectly.")
            print("Balance decreased from $", balance, "to $", balance - 10)
            balance -= 10  # Lose $10 for an incorrect guess
    if balance > 0:
        playagain()
    else: 
        print("You have no more balance left. Game over.")

def playagain():
    if balance == 0:
        return

    print("Your current balance is:", balance)
    again = safe_input("Do you want to play again? (yes/no): ")
    if again.lower() == "yes":
        printbalance()
        boughtdice = getpurchaseamount()
        playgame(boughtdice)
        playagain()
    elif again.lower() == "no":
        print("Thank you for playing! Goodbye.")
        print("Your final balance is:", balance)
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        playagain()

balance = 50
printbalance()
boughtdice = getpurchaseamount()
playgame(boughtdice)
