#! Euler 3
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
import time

def factorization(factored_num):
    '''
    yao = (i if factored_num % i == 0 in range(1, factored_num))
    for i in list(yao):
        print(i)
    '''
    '''
    print(list(i for i in range(1, factored_num) if factored_num % i == 0))
    '''

    '''           
    f_num = (num for num in reversed(range(2, factored_num)))
    for num in list(f_num):
        if i % num == 0:
            if i in f_list:
                strip_list.append(i)
            else:
                f_list.append(i)
                          
    for item in strip_list:
        if item in f_list:
            f_list.remove(item)
    '''
    i = 2
    while i*i <= factored_num:
        if factored_num % i == 0:
            factored_num //= i
        else:
            i = i + 1
    print(factored_num)

time1 = time.time()
'600851475143'
factored_num = 60085147514397536
factorization(factored_num)
time2 = time.time()
print('This program took', int(time2) - int(time1), 'seconds to run')

'''
def factorization(factored_num):
    p_list = []
    for i in reversed(range(int(factored_num))):
        if i % 2 == 0:
            pass
        elif i % 3 == 0:
            pass
        elif i % 5 == 0:
            pass
        elif i % 7 == 0:
            pass
        elif i % 11 == 0:
            pass
        elif i % 13 == 0:
            pass
        elif i % 17 == 0:
            pass
        elif i % 19 == 0:
            pass
        else:
            yield i
            new_list = []
            if factored_num % i == 0:
                print(i)
                p_list.append(i)
    
    if len(p_list) == 1:
    
    time2 = time.time()
    print('This program took', int(time2) - int(time1), 'seconds to run')
           
        
    
     
    reverse_f_list = sorted(f_list, reverse=True)
    for item in f_list:
        for r in reverse_f_list:
            if item % r == 0:
                strip_list.append(item)
    f_list[:] = []
    
    p_list = []
    for item in strip_list:
        if int(strip_list.count(item)) == 2:
            if item not in p_list:
                p_list.append(item)
                
    strip_list[:] = []

    for f in range(1, f_list[-1]):
        for p in f_list:
            if p % f == 0:
                print(p)
    
   
time1 = time.time()
'600851475143'
factored_num = 60085
factorization(factored_num)


def prime_numbers(limit):
    prime_list = []
    for i in range(1, limit):
        if i 

    for j in sorted(prime_list):
        print(j, prime_list.count(j))
            
limit = 100
prime_numbers(limit)

def generator(limit):
    prime_num = (limit % i for i in reversed(range(1, limit)))
    print(list(prime_num))
    
limit = 100
generator(limit)
'''
