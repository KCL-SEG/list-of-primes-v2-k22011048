"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    init = 2
    list = []

    def isPrime(val):
        if val==1:
            return False
        elif num > 1:
            for i in range (2, val):
                if val%i == 0:
                    return False
        return True

    if number_of_primes<1:
        raise ValueError("Must be >0 ")
    if number_of_primes ==1:
        list.append(init)
        return  list
    else:
        list.append(init)
        while len(list)<number_of_primes:
            init +=1
            if isPrime(init):
                list.append(init)
    print(list)

    return list
