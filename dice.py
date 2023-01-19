import random

def roll(int):
    d20 = random.randint(1, 20)
    if d20 == 20:
        print("You just got a crit! Roll twice the dice for damage.")
    elif d20 == 1:
        print("You got a critical fail! Your character stumbles and falls down.")
    else:
        print("Wow...")
    return d20

print("You just rolled a", roll(int))