# Die Roll Game

A simple command line game written in Python. You start with $50, buy some dice and try to predict what each one will roll. Guess right and you make money. Guess wrong and you lose some.

## How to Play

- You start with a balance of $50
- Each die costs $10, so your balance caps how many you can buy at once
- For every die you buy, guess a number from 1 to 6
- Guess correctly and you win $20. Guess wrong and you lose $10
- After each round you can choose to play again or cash out
- The game ends when your balance hits $0
- Type `bye` at any prompt to quit

## Requirements

- Python 3.6 or newer
- No extra libraries needed. It only uses the built-in `random` module

## Running the Game

```bash
python diegame.py
```

On some systems you may need to use `python3` instead:

```bash
python3 diegame.py
```

## Example Session

```
Welcome to the die roll game!
Type 'bye' to quit at any time
Your current balance is: $50
Each die costs $10.
Enter the number of die you would like to purchase: 2
Enter your prediction for die 1 (1-6): 4
Die 1 rolled: 4
Congratulations! You guessed correctly. Balance increased from $ 50 to $ 70
Enter your prediction for die 2 (1-6): 2
Die 2 rolled: 5
Sorry, you guessed incorrectly.
Balance decreased from $ 70 to $ 60
Your current balance is: 60
Do you want to play again? (yes/no): no
Thank you for playing! Goodbye.
Your final balance is: 60
```

## A Quick Note on the Odds

Each guess has a 1 in 6 chance of being right, so the game is stacked against you. On average you lose about $5 per die. Good luck anyway.
