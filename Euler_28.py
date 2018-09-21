"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
43 44 45 46 47 48 49
42 21 22 23 24 25 26
41 20  7  8  9 10 27
40 19  6  1  2 11 28
39 18  5  4  3 12 29
38 17 16 15 14 13 30
37 36 35 34 33 32 31
It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

    1 = 1
    three = 25
    five = 101
    seven = 261
    nine
"""
#top right coner is the square of the number of rows
#bottom right is square
#import pandas as pd

def spiral():
i = 3
spiral_list = [1]
while i <= 1001:
    row_num = i
    top_right = row_num ** 2
    bottom_right = (((row_num - 2) ** 2) + 1) + (row_num - 2)
    bottom_left = bottom_right + (row_num - 1)
    top_left = bottom_left + (row_num - 1)
    spiral_sum = top_right + top_left + bottom_right + bottom_left
    spiral_list.append(spiral_sum)
    i += 2
print(sum(spiral_list))
spiral()
