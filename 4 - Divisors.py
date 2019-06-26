#divisors - read a bit wrong so program does a different thing


listAfter = []
i = 0

for num in range(len(x)):
    listAfter = x[i] / 2
    try:
        
        int(listAfter)
        
    except TypeError:
        pass
    listAfter.append(x)
    i += 1
    
print(listAfter)