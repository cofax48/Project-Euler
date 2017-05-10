#! Euler 16
#215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

#What is the sum of the digits of the number 21000?

two_string = str(2**1000)
num_list = []
i = 0
while i < len(two_string):
    num_list.append(int(two_string[i:i+1]))
    i += 1
print(sum(num_list))
