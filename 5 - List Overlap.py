#List Overlap
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
x = []

num = 1

while True:
    checkA = num in a
    checkB = num in b

    if checkA and checkB == True:
        print(num)
    num += 1