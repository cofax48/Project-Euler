#! Euler 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10,001st prime number?
import time
import math

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

def get_primes():
    number = 1
    num_list = []
    while number < 1000000:
        if is_prime(number):
            num_list.append(number)            
        number += 1
        if len(num_list) == 10001:
            break
        
    print('The 10,001st prime number is:', num_list[-1])

time1= time.time()
get_primes()
time2 = time.time()
print('total time', time2 - time1)
