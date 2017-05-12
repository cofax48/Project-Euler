square_list = []
for i in range(1, 1001):
    square_list.append(i**i)
print(str(sum(square_list))[-11:])
