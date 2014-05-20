def primality(candidate):
    divisor = 2
    half = candidate / 2 + 1
    while divisor < half:
        if candidate % divisor == 0:
            return(False)
        else:
            divisor += 1
    return(True)

def mersenne(expo):
    print('testing M' + str(expo))
    if primality(2 ** expo - 1):
        print('M' + str(expo), 'is prime!!!')

can = 3
while can < 1000000:
    if primality(can):
        mersenne(can)
    can += 2
