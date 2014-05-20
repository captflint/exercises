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
while can < 1000000:
    if primality(can):
        print(can)
    can += 2
