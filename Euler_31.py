
import time
time1 = time.time()
count = 0

for p1 in range(201):
    p12 = int(201 - p1)
    for p2 in range(0, p12, 2):
        p25 = p12 - p2
        for p5 in range(0, p25, 5):
            p210 = p25 - p5
            for p10 in range(0, p210, 10):
                p220 = p210 - p10
                for p20 in range(0, p220, 20):
                    p250 = p220 - p20
                    for p50 in range(0, p250, 50):
                        p2100 = p250 - p50
                        for p100 in range(0, p2100, 100):
                            p2200 = p2100 - p100
                            for p200 in range(0, p2200, 200):
                                if p1 + p2 + p5 + p10 + p20 + p50 + p100 + p200 == 200:
                                    count += 1
print(count)
print(time.time() - time1)
