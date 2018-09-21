print(divmod(10, 100))
'''
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

num_list = 0
a = 0
b = 0
while a < 10:
    num = str(a)
    if num.count(str(a)) == 1:
        while b < 10:
            num = num + str(b)
            if num.count(str(b)) == 1:
                print(num)
            b += 1
            a += 1
'''
"""
num_list = []
for a in range(9):
    for b in range(9):
        for c in range(9):
            for d in range(9):
                for e in range(9):
                    for f in range(9):
                        for g in range(9):
                            for h in range(9):
                                for i in range(9):
                                    num = str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g) + str(h) + str(i)
                                    print(num_str)
                                    if num.count(str(a)) == 1:
                                        if num.count(str(b)) == 1:
                                            if num.count(str(c)) == 1:
                                                if num.count(str(d)) == 1:
                                                    if num.count(str(e)) == 1:
                                                        if num.count(str(f)) == 1:
                                                            if num.count(str(g)) == 1:
                                                                if num.count(str(h)) == 1:
                                                                    if num.count(str(i)) == 1:
                                                                        print(num)
                                                                        num_list.append(num)
print(len(num_list))
"""
