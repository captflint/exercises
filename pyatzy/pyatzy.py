from random import randint

def roll(num):
    results = []
    while num > 0:
        results.append(randint(1, 6))
    return(results)

def choose(listofrolls):
