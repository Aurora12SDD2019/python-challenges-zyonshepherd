#list less than ten

listOfNums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
i = 0
numsList = []

for nums in range(len(listOfNums)):
    if int(listOfNums[i]) <= 5:
        numsList.append(listOfNums[i])
    i += 1
    
print(numsList)
    


