'''
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''
both_palindromes = []
for num in range(1, 1000000):
    num_str = str(num)
    first_count = 0
    for letter in range(len(num_str)):
        reverse_letter = int((letter + 1)* -1)
        if num_str[letter] == num_str[reverse_letter]:
            first_count += 1
            if first_count == len(num_str):
                binary_of_palindrome = str(bin(int(num)))
                bin_num_without0b = binary_of_palindrome[2:]
                count = 0
                if bin_num_without0b[0] != 0:
                    for bin_num in range(len(bin_num_without0b)):
                        reverse_order = int((bin_num + 1) * -1)
                        if int(bin_num_without0b[bin_num]) == int(bin_num_without0b[reverse_order]):
                            count += 1
                            if count == len(bin_num_without0b):
                                print(num, bin_num_without0b)
                                both_palindromes.append(num)

print(both_palindromes)
print(sum(both_palindromes))



#print(bin(100))
1001001001
