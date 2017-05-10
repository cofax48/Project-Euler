import math

def pythag_trip():
    square_list = []
    i = 100
    while i < 1000000:
        if len(str(math.sqrt(i))) < 6:
            square_list.append(i)
        i += 1

    results_list = []
    while len(results_list) < 1:
        for a in range(len(square_list)):
            for b in range(len(square_list)):
                for c in range(len(square_list)):
                    if square_list[a] < square_list[b] < square_list[c]:
                        if square_list[a] + square_list[b] == square_list[c]:
                            if math.sqrt(square_list[a]) + math.sqrt(square_list[b]) + math.sqrt(square_list[c]) == 1000:
                                print(square_list[a], square_list[b], square_list[c])
                                product = math.sqrt(square_list[a]) * math.sqrt(square_list[b]) * math.sqrt(square_list[c])
                                results_list.append(product)
    print(results_list)

pythag_trip()
