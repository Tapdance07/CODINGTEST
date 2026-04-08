angle = list()
for i in range(3):
    angle.append(int(input()))

if sum(angle) == 180:
    if angle.count(angle[0]) == 3:
        print("Equilateral")
    elif angle.count(angle[0]) == 1 and angle.count(angle[1]) == 1:
        print("Scalene")
    else:
        print("Isosceles")


else:
    print("Error")