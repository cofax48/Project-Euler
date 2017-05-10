#! Euler 3
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers
# is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

    
def palindrome():
    winners = []
    for i in range(999):
        for j in range(999):
            number = i * j
            if len(str(number)) < 6:
                pass
            else:
                number = '{}'.format(number)
                if number[0] == number[5]:
                    if number[1] == number[4]:
                        if number[2] == number[3]:
                            if number not in winners:
                                winners.append(number)
                            else:
                                pass
    print(sorted(winners)[-1], 'is the largest palindrome')

palindrome()

