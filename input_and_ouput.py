

def get_primes():
    with open('prime_numbers_list.txt', 'r+') as file_object:
        contents = file_object.read()

        return contents

def make_primes(num_range):
    prime_num_list = []
    for num in range(1, num_range):
        div_list = []
        for div in range(1, num):
            if num % div == 0:
                div_list.append(div)
            if len(div_list) > 1:
                break
        if len(div_list) < 2:
            prime_num_list.append(num)
    return prime_num_list

def write_primes(stuff_to_add):
    with open('prime_numbers_list.txt', 'r+') as file_object:
        file_object.write(stuff_to_add)
        contents = file_object.read()

        print(contents)

def whats_your_name():
    name = input('whats your name')
    return name

def main():
    saved_data = eval(get_primes())
    print(saved_data['User_Name'])
    names = whats_your_name()
    if names == saved_data['User_Name']:
        print('your high score is ', saved_data['Total_Score'])
    else:
        data_object_to_write = {'User_Name': '{}'.format(names), 'Positions': [], 'Total_Score': 0}
        write_primes(str(data_object_to_write))

    get_primes()
main()
