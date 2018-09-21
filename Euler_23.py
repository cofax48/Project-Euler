
######23
'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number
that can be written as the sum of two abundant numbers is 24. By mathematical analysis,
it can be shown that all integers greater than 28123 can be written as the sum of two
abundant numbers. However, this upper limit cannot be reduced any further by analysis
even though it is known that the greatest number that cannot be expressed as the sum
of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''
def divisors(num):
    num_sum = 0
    half_num = int(num / 2) + 1
    for i in range(1, num):
        if num % i == 0:
            num_sum += i
    return num_sum

def perfect_num():
    abundant_num_list = []
    for i in range(1, 281):
        num_sum = divisors(i)
        if num_sum > i:
            abundant_num_list.append(num_sum)
    non_abundant_nums = 0
    for i in range(1, 281):
        if i not in abundant_num_list:
            print(i)
            non_abundant_nums += i
    print(non_abundant_nums)
perfect_num()
########
#24
######

'''
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''
