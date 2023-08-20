#find the outlier from the list caculate z-score
import numpy as np
L1 = [7, 8, 6, 100,7 ,9]
print(L1)

avg = np.average(L1)
print("average =", avg)

std = np.std(L1)
print(std)

for i in L1:
    z = (i - avg)/ std
    print(f"z-score of {i} = ", z)


# Duplicatio data, convert list to set
L2 = [7, 8, 6,7, 100,7 ,9]
st = set(L2)
print(st)

# scaling using normalization
lis = [85, 94,26,46,47,3,5,47,50,43]
min1 = min(lis)
max1 = max(lis)
print("mminimum num: ",min1)
print("maximum um: ",max1)

for i in lis:
    x=(i-min1)/(max1-min1)
    print("Normalization of ",i,"=",x)
    
    
    
    
    