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

triangle_numbers(100000)
