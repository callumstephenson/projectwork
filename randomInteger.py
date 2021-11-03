import random as rand

def randomNumber(lower,upper):
    return rand.randint(lower,upper)
#Testing function
print(randomNumber(1,10))