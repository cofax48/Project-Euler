'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''
import math
success_list = []
for num in range(200000):
    factorial_sum_list = []
    for letter in str(num):
        factorial_sum_list.append(math.factorial(int(letter)))
    if sum(factorial_sum_list) == num:
        success_list.append(num)
        print(num)
print('total sum', sum(success_list) - 3)
