
Val = val + '4'
Val = val*2
print(Val)
"""
import time
time1 = time.time()

def div_num_getter(input_N):
    num = 1
    input_N_1 = input_N + 1
    div_list = []
    while int(len(div_list)) < input_N:
        for i in range(1, input_N_1):
            if num % i == 0:
                div_list.append(i)
                if len(div_list) == input_N:
                    print(num, "is the lowest number")
                    print(len(div_list))
                    print("This solution took", time.time() - time1, "seconds")
            else:
                div_list = []
                num += 1
              
div_num_getter(10)

def substring(string_to_use):
    time2 = time.time()
    substring_list = []
    sub_str_len = len(string_to_use)
    for i in range(int(sub_str_len)):
        #Single Letter
        substring_list.append(string_to_use[i])
        #Two letter
        two_letter_combo = string_to_use[i:i+2]
        if two_letter_combo not in substring_list:
            substring_list.append(two_letter_combo)
        #Three letter
        three_letter_combo = string_to_use[i:i+3]
        if three_letter_combo not in substring_list:
            substring_list.append(three_letter_combo)
        #four letter
        four_letter_combo = string_to_use[i:i+4]
        if four_letter_combo not in substring_list:
            substring_list.append(four_letter_combo)
        #five letter
        five_letter_combo = string_to_use[i:i+5]
        if five_letter_combo not in substring_list:
            substring_list.append(five_letter_combo)
        #six letter
        six_letter_combo = string_to_use[i:i+6]
        if six_letter_combo not in substring_list:
            substring_list.append(six_letter_combo)
        #Seven letter
        seven_letter_combo = string_to_use[i:i+7]
        if seven_letter_combo not in substring_list:
            substring_list.append(seven_letter_combo)
        #Eight letter
        eight_letter_combo = string_to_use[i:i+8]
        if eight_letter_combo not in substring_list:
            substring_list.append(eight_letter_combo)
        #Nine letter
        nine_letter_combo = string_to_use[i:i+9]
        if nine_letter_combo not in substring_list:
            substring_list.append(nine_letter_combo)
        #Ten letter
        ten_letter_combo = string_to_use[i:i+10]
        if ten_letter_combo not in substring_list:
            substring_list.append(ten_letter_combo)
        #eleven letter
        eleven_letter_combo = string_to_use[i:i+11]
        if eleven_letter_combo not in substring_list:
            substring_list.append(eleven_letter_combo)
        #Twelve letter
        twelve_letter_combo = string_to_use[i:i+12]
        if twelve_letter_combo not in substring_list:
            substring_list.append(twelve_letter_combo)
        #Thirteen letter
        thirteen_letter_combo = string_to_use[i:i+13]
        if thirteen_letter_combo not in substring_list:
            substring_list.append(thirteen_letter_combo)
        #Fourteen letter
        fourteen_letter_combo = string_to_use[i:i+14]
        if fourteen_letter_combo not in substring_list:
            substring_list.append(fourteen_letter_combo)
        #Fifteen letter
        fifteen_letter_combo = string_to_use[i:i+15]
        if fifteen_letter_combo not in substring_list:
            substring_list.append(fifteen_letter_combo)
        #Sixteen letter
        sixteen_letter_combo = string_to_use[i:i+16]
        if sixteen_letter_combo not in substring_list:
            substring_list.append(sixteen_letter_combo)
            
    print(len(substring_list))
    print(substring_list)
    print("This solution took", time.time() - time2, "seconds")

substring("abcdefghijklmnop")


def substring(string_to_use):
    substring_list = []
    sub_str_len = len(string_to_use)
    num_iter = 1
    while num_iter <= sub_str_len:
        for i in range(int(sub_str_len)):
            print(i)
            two_letter_combo = string_to_use[i:i+num_iter]
            print(two_letter_combo)
            if two_letter_combo not in substring_list:
                substring_list.append(two_letter_combo)
                if i == string_to_use[-1]:
                    num_iter += 1
            else:
                num_iter += 1
                print(num_iter)
    print(len(substring_list))

    print(sorted(substring_list))
substring("abcdefghijklmnop")
"""
