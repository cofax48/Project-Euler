#! Euler 14
import time
time1 = time.time()
master_list = []
a = 4
while a < 1000000:
    i = a
    tmp_list = []
    while 2 < i:      
        if i % 2 == 0:
            i = i / 2
            tmp_list.append(i)
        if i % 2 != 0:
            i = (i*3 + 1)
            tmp_list.append(i)
        if i == 2:
            if len(tmp_list) != 0:
                yao = (len(tmp_list), a)
                if len(master_list) < 3:
                    master_list.append(yao)
                else:
                    longest = sorted(master_list)[-1]
                    if longest < yao:
                        master_list.append(yao)
            a += 1

longest = sorted(master_list)[-1]


print(sorted(master_list)[-1])
time2 = time.time()
print('This program took', time2- time1, 'seconds to solve')
