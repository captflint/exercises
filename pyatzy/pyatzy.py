from random import randint

def roll(num):
    results = []
    while num > 0:
        results.append(randint(1, 6))
        num -= 1
    return(results)

def choose(listofrolls):
    print(listofrolls)
    timetochoose = True
    while timetochoose:
        keeps = input("Which dice do you want to keep: ")
        klist = []
        timetochoose = False
        for n in keeps:
            if n in '12345':
                klist.append(listofrolls[int(n) - 1])
            else:
                timetochoose = True
    return(klist + roll(5 - len(klist)))

test = choose(roll(5))
print(test)
