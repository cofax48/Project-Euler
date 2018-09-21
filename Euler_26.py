from decimal import *
import time
time1 = time.time()
getcontext().prec = 3000
longest_repeating_fraction = 0
highest_num = 0
actual_fraction = 0
pf = 0
for denominater in range(1, 1000):
    fraction = Decimal(1) / Decimal(denominater)
    temp_fraction = ''
    previous_front = ''
    count = 0
    for indiv_digit in str(fraction):
        temp_fraction = temp_fraction + str(indiv_digit)
        frac_len = len(temp_fraction)
        half_frac_len = int(frac_len / 2)
        front_frac = temp_fraction[:int(half_frac_len + 2)]
        previous_front = front_frac[2:-1]
        back_frac = temp_fraction[int(half_frac_len + 1):]
        if str(previous_front) == str(back_frac):
            if count == 2:
                if str(temp_fraction) != '0.00':
                    if len(previous_front) > longest_repeating_fraction:
                        longest_repeating_fraction = len(previous_front)
                        highest_num = denominater
                        break
            if denominater > 99:
                if count == 3:
                    if len(previous_front) > longest_repeating_fraction:
                        longest_repeating_fraction = len(previous_front)
                        highest_num = denominater
                        pf = previous_front
                        actual_fraction = temp_fraction
            count += 1

print(highest_num, longest_repeating_fraction, pf, actual_fraction)
print(time.time() - time1)
