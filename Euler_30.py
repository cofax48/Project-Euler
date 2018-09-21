all_num = []
for i in range(1000000):
    if len(str(i)) == 1:
        total = int(str(i)[0])**5
        if total == i:
            print(i)
            all_num.append(total)
    elif len(str(i)) == 2:
        total = int(str(i)[0])**5 + int(str(i)[1])**5
        if total == i:
            print(i)
            all_num.append(total)
    elif len(str(i)) == 3:
        total = int(str(i)[0])**5 + int(str(i)[1])**5 + int(str(i)[2])**5
        if total == i:
            print(i)
            all_num.append(total)
    elif len(str(i)) == 4:
        total = int(str(i)[0])**5 + int(str(i)[1])**5 + int(str(i)[2])**5 + int(str(i)[3])**5
        if total == i:
            print(i)
            all_num.append(total)
    elif len(str(i)) == 5:
        total = int(str(i)[0])**5 + int(str(i)[1])**5 + int(str(i)[2])**5 + int(str(i)[3])**5 + int(str(i)[4])**5
        if total == i:
            print(i)
            all_num.append(total)
    elif len(str(i)) == 6:
        total = int(str(i)[0])**5 + int(str(i)[1])**5 + int(str(i)[2])**5 + int(str(i)[3])**5 + int(str(i)[4])**5 + int(str(i)[5])**5
        if total == i:
            print(i)
            all_num.append(total)
print(sum(all_num) - 1)
