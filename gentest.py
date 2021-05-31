import numpy as np
from numpy.random import random
can = int(input("canciones: "))
repro = int(input("reproducciones: "))
can2 = [repro]

x = (np.random.multinomial(repro,np.ones(can)/can,size = 1)[0])
print(x)
print(x.sum())

mean = repro/can
variance = int(.25*mean)
min = mean - variance
max = mean + variance
arr = [int(min)]*can

diff = repro - (min*can)
while diff > 0:
    ran = np.random.randint(0,can-1)
    if arr[ran] >= max:
        continue
    arr[ran]+=1
    diff-=1
print(arr)

