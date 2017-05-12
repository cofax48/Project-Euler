#n! means n × (n − 1) × ... × 3 × 2 × 1

#For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
#and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

#Find the sum of the digits in the number 100!

initial_num = 100
start_num = initial_num
factorial = 1
while start_num > 0:
    factorial *= start_num
    start_num -= 1

fact_len = len(str(factorial))
num_list = []

for i in range(0, int(fact_len)):
    yao = str(factorial)[i]
    num_list.append(int(yao))
    
sum_num = sum(num_list)
print('The sum of each digit of {}! factorial is {}'.format(initial_num, sum_num))

