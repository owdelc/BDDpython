import numpy as np
can = int(input("cancion: "))
repro = int(input("repro: "))
can2 = [repro]


nums = []
for i in can2:
    if i == 0: 
        nums.append([0 for i in range(can)])
        continue
    total = i
    temp = []
    for i in range(5):
        if total > 1:
            val = np.random.randint(1, total)
            temp.append(val)
            total -= val
            
        if total == 1:
            val = 1
            temp.append(val)
            total -= val
            
    temp.append(total)
    
    for j in temp:
        nums.append(j)

print(nums)