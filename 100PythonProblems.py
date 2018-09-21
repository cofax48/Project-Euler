def num1():
    """
    Question:
    Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
    between 2000 and 3200 (both included).
    The numbers obtained should be printed in a comma-separated sequence on a single line.
    """
    num_list = []
    for i in range(2000, 3201):
        if i % 7 == 0:
            if i % 5 != 0:
                num_list.append(str(i))
    print(','.join(num_list))

def num2(num):
    """
    Question:
    Write a program which can compute the factorial of a given numbers.
    The results should be printed in a comma-separated sequence on a single line.
    Suppose the following input is supplied to the program:
    8
    Then, the output should be:
    40320
    """
    num1 = num + 1
    factorial_list = [1]
    for i in range(1, num1):
        yao = i * sum(factorial_list)
        factorial_list = []
        factorial_list.append(yao)
    return factorial_list[0]
#print(num2(80))

def num3(num):
    """
    Question:
    With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
    Suppose the following input is supplied to the program:
    8
    Then, the output should be:
    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
    """
    num = num + 1
    dict_return = {}
    for i in range(1, num):
        dict_return[i] = i**2
    print(dict_return)
#num3(8)

def num4(yao):
    """
    Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
    Suppose the following input is supplied to the program:
    34,67,55,33,12,98
    Then, the output should be:
    ['34', '67', '55', '33', '12', '98']
    ('34', '67', '55', '33', '12', '98')
    """
    yao_list = []
    temp_list = []
    for i in yao:
        if i != ',':
            temp_list.append(str(i))
        if i == ',':
            yaoyao = ''.join(temp_list)
            yao_list.append(yaoyao)
            temp_list = []
    print(yao_list)
    print(tuple(yao_list))
#num4('34,67,55,33,12,98')

def num5():
    """
    Define a class which has at least two methods:
    getString: to get a string from console input
    printString: to print the string in upper case.
    Also please include simple test function to test the class methods.
    """
    class methodical(object):

        def __init__(self):
            self.s = ''

        def getString(self):
            self.s = input('Writ a word and hit enter ')

        def printString(self):
            print(self.s.upper())

    strObj = methodical()
    strObj.getString()
    strObj.printString()

#num5()

def num6(nums):
    """
    Question:
    Write a program that calculates and prints the value according to the given formula:
    Q = Square root of [(2 * C * D)/H]
    Following are the fixed values of C and H:
    C is 50. H is 30.
    D is the variable whose values should be input to your program in a comma-separated sequence.
    Example
    Let us assume the following comma separated input sequence is given to the program:
    100,150,180
    The output of the program should be:
    18,22,24
    """
    whol_num_list =[]
    temp_list = []
    for i in nums:
        if i != ',':
            temp_list.append(str(i))
        if i == ',':
            complete_num = ''.join(temp_list)
            whol_num_list.append(complete_num)
            temp_list = []
    complete_num = ''.join(temp_list)
    whol_num_list.append(complete_num)

    for i in whol_num_list:
        sqrt = ((2 * 50 * int(i))/30)**(.5)
        print(int(sqrt))

#nums = '100,150,180,7856,74247,16'
#num6(nums)

def num7(X,Y):
    """
    Question:
    Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
    Note: i=0,1.., X-1; j=0,1,¡­Y-1.
    Example
    Suppose the following inputs are given to the program:
    3,5
    Then, the output of the program should be:
    [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
    """
    counter = 0
    listicles = []
    for i in range(X):
        row_list = []
        for q in range(Y):
            newQ = q * counter
            row_list.append(newQ)
        listicles.append(row_list)
        counter += 1
    print(listicles)

#num7(3,5)

def num8(inputted_word):
    '''
    Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
    Suppose the following input is supplied to the program:
    without,hello,bag,world
    Then, the output should be:
    bag,hello,without,world
    '''
    whole_list_of_words = []
    temp_list = []
    for i in inputted_word:
        if i == ',':
            whole_list_of_words.append(''.join(temp_list))
            temp_list = []
        else:
            temp_list.append(i)
    whole_list_of_words.append(''.join(temp_list))
    list_to_make_csv = ''
    for i in sorted(whole_list_of_words):
        list_to_make_csv = list_to_make_csv + str(i) + ','
    list_to_make_csv = list_to_make_csv[:-1]
    print(list_to_make_csv)

#num8('without,hello,bag,world')

def num9(inputted_word):
    '''
    Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
    Suppose the following input is supplied to the program:
    Hello world
    Practice makes perfect
    Then, the output should be:
    HELLO WORLD
    PRACTICE MAKES PERFECT
    '''
    lister = []
    [lister.append(i.upper()) for i in inputted_word]
    print(''.join(lister))

#num9('Hello world \n Practice makes perfect')

def num10(inputted_word):
    '''
    Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
    Suppose the following input is supplied to the program:
    hello world and practice makes perfect and hello world again
    Then, the output should be:
    again and hello makes perfect practice world
    '''
    word_bank = []
    temp_list = []
    for i in inputted_word:
        if i == ' ':
            word = ''.join(temp_list)
            if word not in word_bank:
                word_bank.append(word)
            temp_list = []
        else:
            temp_list.append(i)
    word = ''.join(temp_list)
    if word not in word_bank:
        word_bank.append(word)
    print(' '.join(sorted(word_bank)))

#num10('hello world and practice makes perfect and hello world again')

def num9(bit_to_input):
    '''
    Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
    Example:
    0100,0011,1010,1001
    Then the output should be:
    1010
    Notes: Assume the data is input by console.
    '''

#num9('0100,0011,1010,1001')

def num12():
    '''
    Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
    The numbers obtained should be printed in a comma-separated sequence on a single line.
    '''
    even_num_digit_list = []
    for num in range(1000,3001):
        counter = 0
        for digit in str(num):
            if int(digit) != 0:
                if int(digit) % 2 == 0:
                    counter += 1
        if counter == 4:
            even_num_digit_list.append(num)
    print(even_num_digit_list)
#num12()

def num13(inputted_word):
    '''
    Write a program that accepts a sentence and calculate the number of letters and digits.
    Suppose the following input is supplied to the program:
    hello world! 123
    Then, the output should be:
    LETTERS 10
    DIGITS 3
    '''
    letter_list = []
    digit_list = []
    for i in inputted_word:
        if i.isdigit() == True:
            digit_list.append(i)
        else:
            if i != ' ':
                if i !='!':
                    letter_list.append(i)
    print('LETTERS', len(letter_list))
    print('DIGITS', len(digit_list))
#num13('hello world! 123')

def num14(inputted_word):
    '''
    Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
    Suppose the following input is supplied to the program:
    Hello world!
    Then, the output should be:
    UPPER CASE 1
    LOWER CASE 9
    '''
    upper_words = 0
    lower_words = 0
    for i in str(inputted_word):
        if i.isupper() == True:
            upper_words += 1
        if i.islower() == True:
            lower_words += 1
    print('UPPER CASE', upper_words)
    print('LOWER CASE', lower_words)

#num14('Hello world!')
def num15(num):
    '''
    Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
    Suppose the following input is supplied to the program:
    9
    Then, the output should be:
    11106
    '''
    num = str(num)
    print(int(num)+int(num*2)+int(num*3)+int(num*4))

#num15(9)

def num16(num):
    '''
    Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
    Suppose the following input is supplied to the program:
    1,2,3,4,5,6,7,8,9
    Then, the output should be:
    1,3,5,7,9
    '''
    num_list = []
    for i in num:
        if i != ',':
            if int(i) % 2 != 0:
                num_list.append(i)
    print(num_list)

#num16('1,2,3,4,5,6,7,8,9')
def num17():
    '''
    Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
    D 100
    W 200
    ¡­
    D means deposit while W means withdrawal.
    Suppose the following input is supplied to the program:
    D 300
    D 300
    W 200
    D 100
    Then, the output should be:
    500
    '''
    account_holdings = 0
    while True:
        inputted_word = input()
        if str(inputted_word)[0] == 'D':
            account_holdings += int(inputted_word[1:])
        if str(inputted_word)[0] == 'W':
            account_holdings -= int(inputted_word[1:])
        print(account_holdings)
        if inputted_word == 'stop':
            break

#num17()

def num18(password):
    '''
    A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
    Following are the criteria for checking the password:
    1. At least 1 letter between [a-z]
    2. At least 1 number between [0-9]
    1. At least 1 letter between [A-Z]
    3. At least 1 character from [$#@]
    4. Minimum length of transaction password: 6
    5. Maximum length of transaction password: 12
    Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
    Example
    If the following passwords are given as input to the program:
    ABd1234@1,a F1#,2w3E*,2We3345
    Then, the output of the program should be:
    ABd1234@1
    '''
    import re
    if 5 < len(password) < 13:
        lower_case_pattern = re.compile(r'[a-z]')
        lower_case_result = lower_case_pattern.findall(password)
        if len(lower_case_result) > 0:
            num_pattern = re.compile(r'[0-9]')
            num_result = num_pattern.findall(password)
            if len(num_result) > 0:
                upper_case_pattern = re.compile(r'[A-Z]')
                upper_case_result = upper_case_pattern.findall(password)
                if len(upper_case_result) > 0:
                    punctuation_pattern = re.compile(r'\W')
                    punctuation_result = punctuation_pattern.findall(password)
                    if len(punctuation_result) > 0:
                        return 'dis a spicy password'
                    else:
                        return 'add a wild card'
                else:
                    return "no upper case"
            else:
                return "no number"
    else:
        return "too short, make a new password"


#print(num18('2We3345'))
def num19(inputted_word):
    '''
    You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
    1: Sort based on name;
    2: Then sort based on age;
    3: Then sort by score.
    The priority is that name > age > score.
    If the following tuples are given as input to the program:
    Tom,19,80
    John,20,90
    Jony,17,91
    Jony,17,93
    Json,21,85
    Then, the output of the program should be:
    [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
    '''
    print(sorted(inputted_word))

#num19([('Tom', '19', '80'), ('John', '20', '90'), ('Jony', '17', '93'), ('Jony', '17', '91'), ('Json', '21', '85')])

def num20(num):
    '''
    Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
    '''
    num_list = []
    [num_list.append(i) for i in range(0, num) if i % 7 == 0]
    print(num_list)

#num20(853)

def num21():
    """
    A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
    UP 5
    DOWN 3
    LEFT 3
    RIGHT 2
    ¡­
    The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
    Example:
    If the following tuples are given as input to the program:
    UP 5
    DOWN 3
    LEFT 3
    RIGHT 2
    Then, the output of the program should be:
    UP 3
    Left 1
    """
    vertical = 0
    horizontal = 0
    import re
    while True:
        direction = input()
        direction_pattern = re.compile(r'[A-Za-z]')
        direction_result = direction_pattern.findall(direction)
        direction_result = ''.join(direction_result)
        if str(direction_result) == 'UP':
            print(int(str(direction)[-1]))
            vertical += int(str(direction)[-1])
        if str(direction_result) == 'DOWN':
            vertical -= int(str(direction)[-1])
        if str(direction_result) == 'LEFT':
            horizontal -= int(str(direction)[-1])
        if str(direction_result) == 'RIGHT':
            horizontal += int(str(direction)[-1])
        if direction == 'stop':
            break
        print('vertical', vertical, 'horizontal', horizontal)
#num21()

def num22(inputted_word):
    '''
    Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
    Suppose the following input is supplied to the program:
    New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
    Then, the output should be:
    2:2
    3.:1
    3?:1
    New:1
    Python:5
    Read:1
    and:1
    between:1
    choosing:1
    or:2
    to:1
    '''
    word_bank = []
    temp_list = []
    for i in inputted_word:
        if i == ' ':
            word_bank.append(''.join(temp_list))
            temp_list = []
        else:
            temp_list.append(i)
    word_bank.append(''.join(temp_list))
    #print(word_bank)
    previous_word = ''
    for word in sorted(word_bank):
        if previous_word != word:
            print(str(word) + ':', word_bank.count(word))
        previous_word = word
#num22('New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.')
def num23(num):
    ''' Write a method which can calculate square value of number'''
    print(num**2)
#num23(88)
def recursive_prog(num, count):
    new_num = num / 2
    count += 1
    if new_num > 1:
        recursive_prog(new_num, count)
        print(new_num, count)
    else:
        print(count)
#recursive_prog(100, 0)
def class_maker():
    class Josh(object):
        def __init__(self):
            self.name = name
            self.age = age
            self.loc = loc

        def ager(age):
            age = age * 2
            return age
        def namer(name):
            return name + 'z'

    print(Josh.ager(22))
    print(Josh.namer('joooosh'))
#class_maker()
def dict_fun():
    '''
    dict_to_use = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
    for i in sorted(dict_to_use):
        print(i, dict_to_use[i])
    '''
    d = {}
    for i in range(10):
        d[i] = i**2
    [print(d[q]) for q in d]
#dict_fun()
def num27(numl):
    evenNumbes = filter(lambda x: x%2==0, numl)
    for i in evenNumbes:
        q = i**2
        if q in numl:
            print(q)
    #or
    evenNumbes = map(lambda x: x**2, filter(lambda x: x%2==0, numl))
    for i in evenNumbes:
        print(i)

    yao = map(lambda x: x**2, range(1, 21))
    for i in yao:
        print(i)
#num27([1,2,3,4,5,6,7,8,9,10])
'''
r 10
d 20 2r
c 2rPI
a r**2PI
'''
def rdca(num):
    import math
    class Mathy(object):
        def __init__():
            self.radius = radius
            self.diameter = diameter
            self.circ = circ
            self.area = area

        def areas(area):
            radius = math.sqrt(area / math.pi)
            diameter = radius * 2
            circ = diameter * math.pi
            return area, radius, diameter, circ
        def diameters(diameter):
            radius = diameter / 2
            circ = diameter * math.pi
            area = (radius**2) * math.pi
            if int(area) == 7853:
                raise RuntimeError('nahhhhh')
            else:
                return area, radius, diameter, circ

    print(Mathy.areas(num))
    print(Mathy.diameters(num))

#rdca(101)
def is_palindrome(word):
    for i in range(len(word)):
        neg_i = (i + 1) * -1
        if word[neg_i] != word[i]:
            return 'Not a palindrome'
    return 'Palindrome'

#print(is_palindrome('otssto'))

def triangle_numbers(num):
    current_num = 0
    i = 0
    while i <= num:
        current_num += i
        factor_list = []
        previous_opp = 0
        for q in range(1, current_num):
            if current_num % q == 0:
                opposite_fraction = int(current_num / q)
                if q not in factor_list:
                    factor_list.append(q)
                    factor_list.append(opposite_fraction)
                if q == opposite_fraction:
                    break
                if q == previous_opp:
                    break
                previous_opp = opposite_fraction
        i += 1
        if len(factor_list) > 500:
            print(current_num, 'is the lowest triangular number, with ', len(factor_list))

#triangle_numbers(100000)

def perfect_number(given_num):
    '''
    As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

    Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
    '''
    abundent_num_list = []
    for current_num in range(1, given_num):
        factor_list = []
        previous_opp = 0
        for q in range(1, current_num):
            if current_num % q == 0:
                opposite_fraction = int(current_num / q)
                if q not in factor_list:
                    factor_list.append(q)
                    if opposite_fraction not in factor_list:
                        if opposite_fraction != current_num:
                            factor_list.append(opposite_fraction)
                if q == opposite_fraction:
                    break
                if q == previous_opp:
                    break
                previous_opp = opposite_fraction
        factored_sum = sum(factor_list)
        if current_num < factored_sum:
            #print(current_num, sum(factor_list))
            #print(current_num, abundent_num_list)
            if current_num not in abundent_num_list:
                abundent_num_list.append(current_num)
            for x in abundent_num_list:
                if x < 14112:
                    sum_and_current_num = current_num + x
                    print(current_num, sum_and_current_num)
                    if sum_and_current_num < given_num:
                        if sum_and_current_num not in abundent_num_list:
                            #print(sum_and_current_num)
                            abundent_num_list.append(sum_and_current_num)
                    else:
                        break
                else:
                    break
    print(sum(abundent_num_list) - 50)

    """
    print(abundent_num_list)
    print(sum(abundent_num_list))
    sum_count1 = 0
    sum_count2 = 12
    sum_count3 = 18
    sum_count4 = 20
    sum_count5 = 24
    sum_count6 = 30
    for num in abundent_num_list:
        sum_count1 += num
        sum_count2 += num
        sum_count3 += num
        sum_count4 += num
        sum_count5 += num
        sum_count6 += num
        if sum_count1 not in abundent_num_list:
            abundent_num_list.append(sum_count1)
        elif sum_count2 not in abundent_num_list:
            abundent_num_list.append(sum_count2)
        elif sum_count3 not in abundent_num_list:
            abundent_num_list.append(sum_count3)
        elif sum_count4 not in abundent_num_list:
            abundent_num_list.append(sum_count4)
        elif sum_count5 not in abundent_num_list:
            abundent_num_list.append(sum_count5)
        elif sum_count6 not in abundent_num_list:
            abundent_num_list.append(sum_count6)
        #print(num, sum_count1, sum_count2, sum_count3, sum_count4, sum_count5, sum_count6)
        if num > 28123:
            break

    new_abundent_list = filter(lambda a: a < 28124, abundent_num_list)
    non_abundent_nums = []
    for i in range(28124):
        if i not in new_abundent_list:
            non_abundent_nums.append(i)
    print(sum(non_abundent_nums))
    print(int(sum(non_abundent_nums)) - 50)



    sum_count1 = 0
    sum_count2 = 12
    sum_count3 = 18
    sum_count4 = 20
    sum_count5 = 24
    sum_count6 = 30
    non_abundent_nums = []
    for num in abundent_num_list:
        if num not in abundent_num_list:
            if num != sum_count1:
                if num != sum_count2:
                    if num != sum_count3:
                        if num != sum_count4:
                            if num != sum_count5:
                                if num != sum_count6:
                                    print(num, sum_count1, sum_count2, sum_count3, sum_count4, sum_count5, sum_count6)
                                    non_abundent_nums.append(num)
        else:
            if sum_count1 in non_abundent_nums:
                non_abundent_nums.remove(sum_count1)
            elif sum_count2 in non_abundent_nums:
                non_abundent_nums.remove(sum_count2)
            elif sum_count3 in non_abundent_nums:
                non_abundent_nums.remove(sum_count3)
            elif sum_count4 in non_abundent_nums:
                non_abundent_nums.remove(sum_count4)
            elif sum_count5 in non_abundent_nums:
                non_abundent_nums.remove(sum_count5)
            elif sum_count6 in non_abundent_nums:
                non_abundent_nums.remove(sum_count6)
        sum_count1 += num
        sum_count2 += num
        sum_count3 += num
        sum_count4 += num
        sum_count5 += num
        sum_count6 += num

    print(non_abundent_nums)
    print(int(sum(non_abundent_nums) - 50))

    for reg_num in range(100):
        for abund_num in abundent_num_list:
            if reg_num % abund_num == 0:
                print(reg_num, abund_num)
    """

#perfect_number(100)

def list_fun():
    lister = [12, 18, 20, 24, 24, 24, 30, 36, 40, 42, 48, 54, 56, 60, 66, 70, 72, 78, 80, 84, 88, 90, 96, 100, 102, 104]
    #for i in lister:
        #lister.extend(range(i))

    #makes the fifth index position = 3333
    #lister.insert(5, 3333)

    #remove specific item from list
    #list.remove(item)

    #remov last item in list-useful for stacks
    #lister.pop()

    #delete all items
    #lister.clear()

    #count occurences in list
    #lister.count(12)

    #sort the list_to_use
    #lister.sort(key=None, reverse=True)

    #reverse the list
    #lister.reverse()

    #copy th list
    #lister.copy()

    #LIST AS STACK ##########
    #Last in first out
    #lister.append(item) #adds to end of list
    #lister.pop() removes last item in list

    #####QUEUES######
    #Queues are first in first, first out
    #But lists arent great because every element in the array has to be shifted down one

    #collections.deque is proper manuever

    '''
    from collections import deque
    queue = deque(['Eric', 'Josh', "Joyce", 'mike'])
    queue.append('DYLAN')
    queue.append('hank')
    print(queue)
    queue.popleft() #Eric leaves the list
    print(queue)
    queue.pop() #hank the most recent addition leaves the list
    print(queue)
    '''

    ######List Compehensions ########
    '''
    for i in range(10):
        i**2 #overwrites any i varible and still exists after loop has run
    '''

    #Better way
    #squares = list(map(lambda x: x**2, range(10)))
    #or
    #squares = [x**2 for x in range(10)]
    #print(squares)

    ##### DEL STATEMENT #####
    #remove by index
    #del lister[0]

    #remove slices
    #del lister[1:3]

    #delete everything
    #del lister

    #Tuples are immutable but they can contain mutable items
    #yao = tuple([lister])
    #yao[0][0] = 100
    #print(yao)

    #Tuple packing
    #yao = 123, 456, 'yao'
    #print(yao)

    ####SETS####
    #sets are unordered collections with no duplicates, good for membership testing and eliminating duplicates
    #print(lister)
    #yao = set(lister) #automatically gets rid of duplicte entries
    #yao.add(12)
    #print(yao)
    dicter = {}
    for i in range(len(lister)):
        dicter[i] = lister[i]
    dicter[0] = 100

    #get a list of all dictionary keys
    #list(dicter.keys())

    #get a list of all dictionary values
    #print(list(dicter.values()))

    #organize an unsorted dictionary
    #print(sorted(dicter))

    #membership testing
    #print(25 in dicter) #comes up as true because 25 the key is in there
    #print(104 in dicter) #coms up as false because 104 as a value is not considered

    #create a dictionary k,v dynamically
    #yao = {x: x**2 for x in range(10)}

    #get key and value pairs from a dict
    #for k,v in yao.items():
    #    print(k,v)

    #Enumerate allows for getting index position at the same time
    #for index, value in enumerate(lister):
    #    print(index, value)

    #loop through a sequence in reverse
    #for i in reversed(range(1, 10)):
    #    print(i)

    #loop through a sequence in reverse, very second number
    for i in reversed(range(1, 10, 2)):
        print(i)

#list_fun()

def coderbyte1(sen):
    temp_list = []
    word_bank = []
    for i in sen:
        if i != ' ':
            if i.isalpha() == True:
                temp_list.append(i)
        else:
            yao = ''.join(temp_list)
            temp_list.clear()
            word_bank.append(yao)
    yao = ''.join(temp_list)
    temp_list.clear()
    word_bank.append(yao)

    w = ''
    length = 0

    for word in word_bank:
        w_len = len(word)
        if w_len > length:
            length = w_len
            w = word
    return w

#print(coderbyte1("fun&!! time underbomb"))

class DoMath:

    """
    def __init__(self, object):
        self.base_salary = object
        self.taxes = taxes
        #self.monthly_pay = monthly_pay
        #self.take_home_pay = take_home_pay
        #self.hourly_wage = hourly_wage
    """

    def base(self, base_salary):
        print('total salary is $', base_salary)

    def tax(self, base_salary):
        taxes = int(base_salary) * .6666666
        print('total taxes ', taxes)
        return taxes

#salary = DoMath()
#print(DoMath.tax(100))
def yao(word):
    word_bank = []
    for i in str(word):
        #print(i)
        i = i.lower()
        if i == 'a':
            word_bank.append('b')
        elif i == 'b':
            word_bank.append('c')
        elif i == 'c':
            word_bank.append('d')
        elif i == 'd':
            word_bank.append('E')
        elif i == 'e':
            word_bank.append('f')
        elif i == 'f':
            word_bank.append('g')
        elif i == 'g':
            word_bank.append('h')
        elif i == 'h':
            word_bank.append('I')
        elif i == 'i':
            word_bank.append('j')
        elif i == 'j':
            word_bank.append('k')
        elif i == 'k':
            word_bank.append('l')
        elif i == 'l':
            word_bank.append('m')
        elif i == 'm':
            word_bank.append('n')
        elif i == 'n':
            word_bank.append('O')
        elif i == 'o':
            word_bank.append('p')
        elif i == 'p':
            word_bank.append('q')
        elif i == 'q':
            word_bank.append('r')
        elif i == 'r':
            word_bank.append('s')
        elif i == 's':
            word_bank.append('t')
        elif i == 't':
            word_bank.append('U')
        elif i == 'u':
            word_bank.append('v')
        elif i == 'v':
            word_bank.append('w')
        elif i == 'w':
            word_bank.append('x')
        elif i == 'x':
            word_bank.append('y')
        elif i == 'y':
            word_bank.append('z')
        elif i == 'z':
            word_bank.append('A')
        else:
            word_bank.append(i)
    # code goes here
    whole_word = ''.join(word_bank)
    return whole_word
print(yao('arrangement goes here'))
