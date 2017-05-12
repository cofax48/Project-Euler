#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

#Evaluate the sum of all the amicable numbers under 10000.
import time
time1 = time.time()
amicable_pair_dict = {}
origin_num = 10000
countdown = origin_num
while countdown > 0:
    initial_num = countdown
    start_num = initial_num - 1
    num_list = []
    while start_num > 0:
        if initial_num % start_num == 0:
            num_list.append(start_num)
            start_num -= 1
        else:
            start_num -= 1
    amicable_pair_dict[countdown] = sum(num_list)
    countdown -= 1

amic_list = []
for i in range(2, origin_num):
    yao = amicable_pair_dict[i]
    if i == amicable_pair_dict[i]:
        pass
    else:         
        if yao < origin_num:
            if amicable_pair_dict[yao] == i:
                amic_list.append(yao)
t = time.time() - time1
print('The sum of all amicable numbers under {} is {} this took {} seconds to solve'.format(origin_num, sum(amic_list), t))

