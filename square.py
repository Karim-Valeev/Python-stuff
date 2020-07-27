import math

a = [None,None,None]

for i in range(3):
    a[i] = float(input())

d = a[1]*a[1]-4*a[0]*a[2]
if d < 0:
    print("No real solutions.")
else:
    print()
    print((-1*a[1] + math.sqrt(d)) / 2 / a[0]," ",(-1*a[1] - math.sqrt(d)) / 2 / a[0])
