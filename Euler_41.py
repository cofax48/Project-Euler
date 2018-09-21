import time
time1 = time.time()

def is_prime(whole_num):
    pandigital_list = []
    half_i = int(whole_num / 2)
    div_list = []
    for denominator in range(1, half_i):
        if whole_num % denominator == 0:
            div_list.append(denominator)
        if len(div_list) > 1:
            break
    if len(div_list) < 2:
        i_len = len(str(whole_num))
        expected_count = i_len
        num_list = []
        for digit in str(whole_num):
            num_list.append(digit)
        #print(num_list)
        counter = 0
        for num in range(1, int(len(num_list) + 1)):
            #print(whole_num, num, counter)
            if num_list.count(str(num)) == 1:
                counter += 1
                if int(counter) == int(len(num_list)):
                    #print(whole_num, num, counter)
                    pandigital_list.append(whole_num)
            else:
                break
    if len(pandigital_list) == 1:
        return pandigital_list

def get_pandigital_prime():
    pandigital_prime_list = []
    individual_digit_list = ['1', '2', '3', '4', '5', '6', '7']
    for num1 in sorted(individual_digit_list, reverse=True):
        temp_num = num1
        individual_digit_list.remove(num1)
        for num2 in sorted(individual_digit_list, reverse=True):
            temp_num2 = num2
            individual_digit_list.remove(num2)
            for num3 in sorted(individual_digit_list, reverse=True):
                temp_num3 = num3
                individual_digit_list.remove(num3)
                for num4 in sorted(individual_digit_list, reverse=True):
                    temp_num4 = num4
                    individual_digit_list.remove(num4)
                    for num5 in sorted(individual_digit_list, reverse=True):
                        temp_num5 = num5
                        individual_digit_list.remove(num5)
                        for num6 in sorted(individual_digit_list, reverse=True):
                            temp_num6 = num6
                            individual_digit_list.remove(num6)
                            for num7 in sorted(individual_digit_list, reverse=True):
                                if num7 != '2':
                                    temp_num7 = num7
                                    individual_digit_list.remove(num7)
                                    whole_num = int(str(num1) + str(num2) + str(num3) + str(num4) + str(num5) + str(num6) + str(num7))
                                    if is_prime(whole_num):
                                        pandigital_prime_list.append(whole_num)
                                        if len(pandigital_prime_list) > 1:
                                            return pandigital_prime_list
                                    individual_digit_list.append(temp_num7)
                            individual_digit_list.append(temp_num6)
                        individual_digit_list.append(temp_num5)
                    individual_digit_list.append(temp_num4)
                individual_digit_list.append(temp_num3)
            individual_digit_list.append(temp_num2)
        individual_digit_list.append(temp_num)
print('The largst pandigital number is', get_pandigital_prime())
print(time.time() - time1)
