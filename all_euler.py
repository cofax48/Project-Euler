def prob1():
    num_list = []
    for i in range(1000):
        if i % 3 == 0:
            if i not in num_list:
                num_list.append(i)
        if i % 5 == 0:
            if i not in num_list:
                num_list.append(i)
    print(sum(num_list))
#233168
#prob1()
def prob2():
    even_fib_list = []
    n1 = 1
    n2 = 2
    while n2 < 4000000:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        if n1 % 2 == 0:
            even_fib_list.append(n1)
    print(sum(even_fib_list))
#4613732
#prob2()
def is_prime(num):
    half_num = int(num / 2) + 1
    factor_list = []
    for i in range(int(half_num)):
        if i % 2 != 0:
            if num % i == 0:
                factor_list.append(i)
                if len(factor_list) > 1:
                    return 'nah'
    if len(factor_list) == 1:
        return 'prime'

def prob3():
    num = 600851475143
    '''
    half_num = int(num) / 2
    prime_list = []
    for i in range(int(half_num)):
        if i % 2 != 0:
            if num % i == 0:
                temp_prime = []
                half_i = i /2
                for q in range(int(half_i)):
                    if q % 2 != 0:
                         if i % q == 0:
                             temp_prime.append(q)
                         if len(temp_prime) > 1:
                             break
                if len(temp_prime) == 1:
                    prime_list.append(i)
    print(prime_list)
    '''
    factor_list = []
    i = 0
    while i < int(num)/2:
        if is_prime(i) == 'prime':
            if num % i == 0:
                factor_list.append(i)
                print(factor_list)
        i += 1

#prob3()
def prob4():
    word = 'racecar'
    for i in range(len(word)):
        neg_i = int(i + 1) * int(-1)
        print(i, neg_i)
        print(word[i])
        print(word[neg_i])

    for i in range(100, 10):
        for q in range(1, 10):
            prod_num = str(q*i)
            for letter in range(len(prod_num)):
                neg_letter = int(letter + 1) * int(-1)
                front_num = prod_num[letter]
                back_num = prod_num[neg_letter]

                if str(front_num) == str(back_num):
                    print(prod_num)
                    #For example, for the input (5, 1000000000, 2) the solution returned a wrong answer (got 499999999 expected 499999998).

#prob4()

#edge cases:
#no first or last
#empty list
#One element in list
#Missing first o last element
#Two or more of the items missing
#small, medium, large test cases
#negatives

#empty list
#Missing first o last element
#One element in list
#Two or more of the items missing
#large test cases


For example, for the input [-1000, 1000] the solution returned a wrong answer (got 0 expected 2000).

A = [2, 3, 1, 5]
prev_num = 0
for i in sorted(A):
    prev_num += 1
    if i != prev_num:
        print(prev_num)
