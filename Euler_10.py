#! Euler 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
import time
import math
time1 = time.time()
def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return number
    return False

def prime_counter():
    prime_list = []
    for number in range(2000000):
        if is_prime(number) != False:
            prime_list.append(number)
    print(sum(prime_list), 'is the sum of all prime numbers beneath 2 million')
    time2 = time.time()
    print('This solution took', time2 - time1, 'seconds to solve')
prime_counter()
