#! Euler 6
# The sum of the squares of the first ten natural numbers is,
#
#12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is,
#
#(1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of the
#first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#
#Find the difference between the sum of the squares of the first
#one hundred natural numbers and the square of the sum.

def square_finder():
    sum_list = []
    added_list = []
    for i in range(101):
        square = i**2
        sum_list.append(square)
        added_list.append(i)

    print(sum(added_list)**2 - sum(sum_list), 'is the sum difference')

square_finder()
