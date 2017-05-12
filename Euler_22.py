import time
time1 = time.time()
import string
file_to_open = open('names_Euler22.txt')
names = file_to_open.read()
name_list = ['ALONSO'] #This is the last name and no comma follows it
temp_list = []
for char in names:
    if char != '"':
        temp_list.append(char)
        if char == ',':
            yao = ''.join(temp_list[:-1])
            name_list.append(yao)
            temp_list = []
    

whole_name_val_list = []
index = 1
for i in sorted(name_list):
    name_len = str(i)
    temp_let_num_list = []
    for q in name_len:
        letter_as_number = string.ascii_uppercase.index(q)
        temp_let_num_list.append(letter_as_number + 1)
    name_sum = sum(temp_let_num_list)
    whole_name_val = name_sum * index
    whole_name_val_list.append(whole_name_val)
    index += 1

print('The total sum is ', sum(whole_name_val_list), 'and it took ', time.time()-time1, 'seconds')

    

