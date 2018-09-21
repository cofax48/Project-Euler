first_digit = 1
second_digit = 1
third_digit = first_digit + second_digit
num_list = [first_digit, second_digit, third_digit]
while len(str(num_list[-1])) <= 1000:
    first_digit = third_digit
    second_digit = first_digit + second_digit
    third_digit = first_digit + second_digit
    num_list.append(second_digit)
    num_list.append(third_digit)
    if len(str(num_list[-1])) == 1000:
        print('Index position is', len(num_list) -1 )
