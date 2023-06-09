n = int(input())

# tinh sc
import math
sc = 0
for i in range(1,n+1):
    sc = math.sqrt(3+sc)
print(round(sc,3))

# tinh sd
sd = 0
tich = 1
for i in range(1,n+1):
    tich *= i
    sd += tich
print(f'{sd:.3f}')
