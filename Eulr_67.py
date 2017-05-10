#! Euler 67

triangle = open('p067_triangle.txt')
triangle = str(triangle.read())
'''
print(triangle[0:2])
print(triangle[3:5]) #+3
print(triangle[9:11]) #+6
print(triangle[18:20]) #+9
print(triangle[30:32]) #+12
print(triangle[45:47]) #+15

(i-15)/row_counter
row 7, 63
row 8, 81
row 9, 108
'''

"""
def down_counter():
    vertical_list = []
    edge_list = []
    row_counter = 1
    i = 0
    while i <= 10000:
        b = i+2
        print(int(triangle[i:b]), 'ROW', row_counter)
        vertical_list.append(int(triangle[i:b]))
        x = i
        z = b
        x = x-3
        z = z-3
        edge_list.append(int(triangle[x:z]))
        i += (row_counter*3)
        row_counter += 1
    for row in edge_list:
        print(row)
    return {'vertical_list':vertical_list, 'edge_list':edge_list}

down_counter()
'''
print(triangle[33:35]) #origin #51 #row 5
print(triangle[45:47]) #next row, one to the left ((row_counter*3)-3):((row_counter*3)-3)  i += ((row_counter*3)-3), b += ((row_counter*3)-1)
print(triangle[48:50]) #next row, straight down (row_counter*3):(row_counter*3)
print(triangle[51:53]) #next row, one to the right ((row_counter*3)+3):((row_counter*3)+3)
'''
print(triangle[21:23])
'''
2 row 1
5 row 2
8 row 3
11 row 4
'''
def cray_counter(vertical_list, edge_list):
    row_list = [59, 73, 52, 53]
    i = 21
    while i <= 1000:
        row_counter = len(row_list) - 1
        q = i+2
        print(i, q, triangle[i:q], 'yay')
        #next row, one to the left
        a = (i + ((row_counter*3)))
        b = (q + ((row_counter*3)))
        # straight down
        c = (i + (row_counter*3)+3) 
        d = (q + (row_counter*3)+3)
        #next row, one to the right
        e = (i + ((row_counter*3)+6))
        f = (q + ((row_counter*3)+6))
        if triangle[a:b] > triangle[c:d]:
            if triangle[a:b] > triangle[e:f]:
                print('row', row_counter)
                temp_num = row_counter
                temp_num = temp_num + 1
                print('comparison', triangle[a:b], vertical_list[temp_num])
                if int(triangle[a:b]) == int(vertical_list[temp_num]):
                    if triangle[c:d] > triangle[e:f]:
                        print('aaaaaa')
                        i = (c + (row_counter*3)+3)
                        q = (d + (row_counter*3)+3)
                        row_list.append(int(triangle[i:q]))
                        print((triangle[i:q]))
                        i = i
                        row_counter += 1
                    if triangle[e:f] > triangle[c:d]:
                        print('bbbbb')
                        i = (e + (row_counter*3)+6)
                        q = (f + (row_counter*3)+6)
                        row_list.append(int(triangle[i:q]))
                        i = i
                        row_counter += 1
                if int(triangle[a:b]) != int(vertical_list[temp_num]):
                    print(triangle[a:b])
                    i = a
                    q = b
                    print((triangle[i:q]))
                    row_list.append(int(triangle[i:q]))
                    i = i
                    row_counter += 1
        if triangle[c:d] > triangle[a:b]:
            if triangle[c:d] > triangle[e:f]:
                i = c
                q = d
                row_list.append(int(triangle[i:q]))
                i = i
                row_counter += 1
        if triangle[e:f] > triangle[a:b]:
            if triangle[e:f] > triangle[c:d]:
                i = e
                q = f
                row_list.append(int(triangle[i:q]))
                i = i
                row_counter += 1
                

    print(row_list)
vertical_list = down_counter()['vertical_list']
edge_list = down_counter()['edge_list']
cray_counter(vertical_list, edge_list)
print(3**6)
"""
print(3**9)
"""
def five_rows_ahead():
    figure out which route by brute forcing which route over
    the next five rows would produce the gratst sum and then have the computr
    take that route, do this every, but hav it revaluate every route
"""
