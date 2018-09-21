for num in range(100):
    if num % 3 == 0:
        if num % 5 != 0:
            print('fizz')
        else:
            print('fizzbuzzzzz')
    elif num % 5 == 0:
        print('buzz')
    else:
        print(num)
"""
num = 999331
yao = []
yao_list = [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 137, 197, 199, 311, 337, 373, 379, 397, 719, 733, 797, 911, 919, 971, 991, 1091, 1109, 1117, 1193, 1931, 1933, 1973, 3119, 3701, 3779, 3911, 7013, 7393, 7793, 7937, 9001, 9311, 9377, 9719, 9733, 11177, 11701, 11939, 17011, 19391, 19937, 30197, 33911, 37199, 39119, 39971, 70039, 70079, 70111, 71191, 71993, 73019, 79139, 91193, 93719, 93911, 97003, 97007, 97301, 99371, 100391, 103391, 103997, 107119, 110039, 110339, 117701, 119107, 139079, 177011, 190097, 191071, 193939, 199933, 300193, 300739, 300973, 319993, 330019, 330097, 331999, 390791, 391103, 391939, 393007, 393919, 701117, 710399, 719009, 733009, 770111, 790003, 900037, 900971, 907913, 910711, 911003, 911033, 913907, 919393, 930073, 933001, 933199, 939193, 939391, 971039, 993319, 997103, 999331]

def reverse_num(num):
    num_list = []
    for i in range(len(str(num))):
        back_end = str(num)[i:]
        front_part = str(num)[:i]
        num_list.append(int(back_end + front_part))
    return num_list

whol_prime_list = [2]
num_l = [1, 3, 5, 7, 9]
for dig1 in num_l:
    for dig2 in num_l:
        for dig3 in num_l:
            for dig4 in num_l:
                for dig5 in num_l:
                    for dig6 in num_l:
                        div_list = []
                        num = str(dig1) + str(dig2) + str(dig3) + str(dig4) + str(dig5) + str(dig6)
                        half_num = int(int(num) / 2) + 1
                        for i in range(1, half_num):
                            if int(num) % i == 0:
                                div_list.append(i)
                                if len(div_list) > 1:
                                    break
                            if len(div_list) < 2:
                                if num not in whol_prime_list:
                                    print(num)
                                    whol_prime_list.append(num)
print(whol_prime_list)

def reverse_num(num):
    num_list = []
    for i in range(len(str(num))):
        back_end = str(num)[i:]
        front_part = str(num)[:i]
        num_list.append(int(back_end + front_part))
    return num_list
whole_circ_list = []

for i in yao_list:
    temp_list = []
    i_len = len(str(i))
    count = 0
    for letter in str(i):
        if letter != str(0):
            temp_list.append(letter)
            count += 1
        if count == i_len:
            print(temp_list)
            whole_circ_list.append(''.join(temp_list))
            count = 0
print(len(whole_circ_list))

'''
    i_length = len(str(i))
    whole_reverse = reverse_num(i)
    for q in whole_reverse:
        if len(str(q)) == i_length:
            if i not in whole_circ_list:
                whole_circ_list.append(q)
                if q not in whole_circ_list:
                    whole_circ_list.append(q)
        else:
            if i in whole_circ_list:
                whole_circ_list.remove(i)
            elif q in whole_circ_list:
                whole_circ_list.remove(q)
                print(i, q)
'''

                    #print(i, q)
print(len(whole_circ_list), whole_circ_list)




for yaoz in yao_list:
    for i in range(1, yaoz):
        if yaoz % i == 0:
            yao.append(i)
    yao = []
if len(yao) > 2:
    print(yao)


def num37():
    total_circular_prime = []
    for num in range(100000):
        num_length = len(str(num))
        prime_num_list = []

        for i in range(len(str(num))):
            back_end = str(num)[i:]
            front_part = str(num)[:i]
            temp_num = int(back_end + front_part)
            divisor_list = []
            if temp_num % 2 != 0:
                half_num = int(temp_num / 2)
                for q in range(1, temp_num):
                    if temp_num % q == 0:
                        divisor_list.append(q)
                    elif q == half_num:
                        if len(divisor_list) < 2:
                            prime_num_list.append(temp_num)
                    elif len(divisor_list) > 2:
                        break
        if len(prime_num_list) == num_length:
            for r in prime_num_list:
                if r not in total_circular_prime:
                    total_circular_prime.append(r)
    print(total_circular_prime, len(total_circular_prime))

#num37()
import time
time1 = time.time()
def reverse_num(num):
    num_list = []
    for i in range(len(str(num))):
        back_end = str(num)[i:]
        front_part = str(num)[:i]
        num_list.append(int(back_end + front_part))
    return num_list

def is_prime(num):
    divisor_list = []
    if num % 2 == 0:
        return False
    else:
        half_num = int(num / 8)
        for i in range(1, half_num, 2):
            if num % i == 0:
                divisor_list.append(i)
                if len(divisor_list) > 1:
                    return False
    return True

total_num_list = [3]
for num in range(1, 1000000, 2):
    prime_list = []
    if num % 3 != 0:
        if num % 5 != 0:
            if num % 7 != 0:
                if is_prime(num) == True:
                    total_num_list.append(num)
circ_prime_list = []
for num in total_num_list:
    temp_list = []
    for rev_num in reverse_num(num):
        if rev_num not in circ_prime_list:
            if rev_num in total_num_list:
                temp_list.append(rev_num)
                if len(temp_list) == len(str(rev_num)):
                    for circ in temp_list:
                        if circ not in circ_prime_list:
                            circ_prime_list.append(circ)

print(circ_prime_list)
print('len', len(circ_prime_list))


'''
if num % 3 != 0:
    if num % 5 != 0:
        if num % 7 != 0:
            if num not in total_num_list:
                total_circular_prime = []
                if is_prime(num) == True:
                    rev_prime_num = reverse_num(num)
                    for prime_num in rev_prime_num:
                        if is_prime(prime_num) == True:
                            total_circular_prime.append(prime_num)
                if len(total_circular_prime) == len(str(num)):
                    if num not in total_num_list:
                        total_num_list.append(num)
'''
print(len(total_num_list), time.time() - time1)
"""
