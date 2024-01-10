import random


def guess(x):
    random_number = random.randint(1, x)
    guessed = 0
    while random_number != guessed:
        guessed = int(input(f"Enter the number between 1 and {x}: "))
        if random_number > guessed:
            print("This is a too low value")
        elif random_number < guessed:
            print("This is a high value")
    print(f" Yeah, that is the number {guessed}.")


guess(10)
