listicles = []
for a in range(2,101):
    for b in range(2, 101):
        ab = a**b
        if ab not in listicles:
            listicles.append(ab)
        ba = b**a
        if ba not in listicles:
            listicles.append(ba)
print("There are ", len(sorted(listicles)), "distinct items")
