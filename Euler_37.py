def is_prime(whole_num):
    pandigital_list = []
    half_i = int(whole_num / 2)
    div_list = []
    for denominator in range(1, half_i):
        if whole_num % denominator == 0:
            div_list.append(denominator)
        if len(div_list) > 1:
            break
    if len(div_list) < 2:
        return 'Prime'

#3797, 797, 97, and 7
#3797, 379, 37, and 3

def left_primes():
    prime_list = []
    for i in range(1, 10):
        for i2 in range(1, 10):
            left_prime = str(i2) + str(i)
            if is_prime(int(left_prime)):
                for i3 in range(1, 10):
                    left_prime3 = str(i3) + left_prime
                    if is_prime(int(left_prime3)):
                        for i4 in range(1, 10):
                            left_prime4 = str(i4) + left_prime3
                            if is_prime(int(left_prime4)):
                                prime_list.append(left_prime4)
                                for i5 in range(1, 10):
                                    left_prime5 = str(i5) + left_prime4
                                    if is_prime(int(left_prime5)):
                                        prime_list.append(left_prime5)
                                #print(left_prime4)
    return prime_list
left_nums = left_primes()
four_primes = []
def right_primes(left_nums):
    prime_list = []
    for i in range(1, 10):
        for i2 in range(1, 10):
            right_prime = str(i) + str(i2)
            if is_prime(int(right_prime)):
                for i3 in range(1, 10):
                    right_prime3 = right_prime + str(i3)
                    if is_prime(int(right_prime3)):
                        for i4 in range(1, 10):
                            right_prime4 = right_prime3 + str(i4)
                            if is_prime(int(right_prime4)):
                                prime_list.append(right_prime4)
                                if right_prime4 in left_nums:
                                    print('3', int(right_prime4))
                                    four_primes.append(int(right_prime4))
                                    for i5 in range(1, 10):
                                        right_prime5 = right_prime4 + str(i5)
                                        if is_prime(int(right_prime5)):
                                            print('4', right_prime5)
                                            if right_prime5 in left_nums:
                                                four_primes.append(int(right_prime5))
                                                print('5', right_prime5)
    return prime_list

right_primes(left_nums)
print('sum', sum(four_primes))


def other_stuff():
    num_list = [1373, 1997, 3137, 3797, 4337, 4397, 7331]
    for num in num_list:
        for digit in range(1,10, 2):
            front_num = str(num) + str(digit)
            back_num = str(digit) + str(num)
            if is_prime(int(front_num)):
                if is_prime(int(back_num)):
                    print(num, back_num)


    crazy_prime_num = []
    for whole_num in range(100001, 1000001, 2):
        prime_list = []
        if whole_num % 3 != 0:
            if is_prime(whole_num):
                for digit in range(len(str(whole_num))):
                    neg_digit = (digit * -1)
                    front_num = str(whole_num)[:neg_digit]
                    back_num = str(whole_num)[digit:]
                    if front_num != '':
                        if is_prime(int(front_num)):
                            if is_prime(int(back_num)):
                                prime_list.append(front_num)
                                prime_list.append(back_num)
                                if len(str(whole_num)) == 2:
                                    if len(prime_list) == 2:
                                        crazy_prime_num.append(whole_num)
                                elif len(str(whole_num)) == 3:
                                    if len(prime_list) == 3:
                                        crazy_prime_num.append(whole_num)
                                elif len(str(whole_num)) == 4:
                                    if len(prime_list) == 6:
                                        crazy_prime_num.append(whole_num)
                                elif len(str(whole_num)) == 5:
                                    if len(prime_list) >= 8:
                                        crazy_prime_num.append(whole_num)



    print(crazy_prime_num)
