def primality(candidate):
    divisor = 2
    half = candidate / 2 + 1
    while divisor < half:
        if candidate % divisor == 0:
            return(False)
        else:
            divisor += 1
    return(True)

can = 3
lastprime = 3
while 1 == 1:
    if primality(can):
        if can > lastprime + 10000:
            print(can)
            lastprime = can
    can += 2
