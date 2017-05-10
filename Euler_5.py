#! Euler 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10
# without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of
# the numbers from 1 to 20?
num_list = []
for r in range(1, 3000000000):
    if r % 1 == 0:
        if r % 2 == 0:
            if r % 3 == 0:
                if r % 4 == 0:
                    if r % 5 == 0:
                        if r % 6 == 0:
                            if r % 7 == 0:
                                if r % 8 == 0:
                                    if r % 9 == 0:
                                        if r % 10 == 0:
                                            if r % 11 == 0:
                                                if r % 12 == 0:
                                                    if r % 13 == 0:
                                                        if r % 14 == 0:
                                                            if r % 15 == 0:
                                                                if r % 16 == 0:
                                                                    if r % 17 == 0:
                                                                        if r % 18 == 0:
                                                                            if r % 19 == 0:
                                                                                print(r, '19')
                                                                                if r % 20 == 0:
                                                                                    print(r, 'is divisible by 20 and very number beneath it')



def divider():
    
    num_list = []
    i = 1
    while i < 21:
        print(i)
        for j in range(3000):
            print(j)
            if j % i == 0:
                i += 1
                if i == 20:
                    num_list.append(j)
            else:
                pass
                
            
    print(num_list)
    '''
    for i in range(10):
        for j in range(21):
            yao = i * j
            if yao not in num_list:
                num_list.append(str(yao) + ', ' + str(i) + ', ' + str(j))
    '''            
    for num in sorted(num_list):
        print(num)
'''
divider()
'''
'1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20'                                           
    


