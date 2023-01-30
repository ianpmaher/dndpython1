import random

# Rolling with Advantage
def rolld20(int):
    A = random.randint(1, 20)
    B = random.randint(1, 20)
    if A > 20:
        print("The higher of these dice is", A)
    elif B > A:
        print("The higher of these dice is", B)
    else:
        print(A)
    return A, B
print("You just rolled a", rolld20(int))