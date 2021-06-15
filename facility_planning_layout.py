import numpy as np
import math
import array as arr

a = [3, 8, 2, 6, 4]
b = [8, 2, 5, 4, 6]
D = [2000, 3000, 2500, 1000, 1500]
R = [0.12, 0.12, 0.2, 0.15, 0.15]

print("RECTLINEAR DISTANCE")
DR = np.multiply(D,R)
print("DiRi = ", DR)
sorted_DR = [x for _,x in sorted(zip(a,DR))]
print("Sorted DiRi a = " ,sorted_DR)
Cum_DR = np.cumsum(sorted_DR)
print("Cumulative Sum DiRi = ", Cum_DR)
half = max(Cum_DR)/2
print("Half a = ",half)
DR_res = Cum_DR[Cum_DR > half].min()
print("x* =" ,DR_res)


sorted_DRb = [x for _,x in sorted(zip(b,DR))]
print(b)
print("Sorted DiRi b = ", sorted_DRb)
Cum_DRb = np.cumsum(sorted_DRb)
print("Cumulative Sum DiRi b = ",Cum_DRb)
halfb = max(Cum_DRb)/2
print("Half b = ", halfb)
DR_resb = Cum_DRb[Cum_DRb > halfb].min()
print("x* = ", DR_resb)

print("SQUARED DISTANCE")
print("DiRi = " ,DR)
Cum_DR_unsorted = np.cumsum(DR)
print("Sum DiRi = ", Cum_DR_unsorted[4])
DRA = np.multiply(D,R)
DRAA = np.multiply(DRA,a)
print("DiRiAi = ", DRAA)
DRB = np.multiply(D,R)
DRBB = np.multiply(DRB,b)
print("DiRiBi =", DRBB)
Cum_DRAA = np.cumsum(DRAA)
Cum_DRBB = np.cumsum(DRBB)
Cum_DR = np.cumsum(DR)
print("Sum DiRiAi = ",Cum_DRAA[4])
print("Sum DiRiBi = ",Cum_DRBB[4])
AA = Cum_DRAA[4]/Cum_DR[4]
BB = Cum_DRBB[4]/Cum_DR[4]
print("x* = %.2f" % AA)
print("y* = %.2f" % BB)


print("DIRECT DISTANCE")

num_1 = []
num_2 = []
num_1_pow = []
num_2_pow = []
alpha = []
for i in range(0,5):
    num_1.append(3-a[i])
    num_2.append(5-b[i])
    num_1_pow.append(num_1[i]**2)
    num_2_pow.append(num_2[i]**2)
    alpha.append(math.sqrt(float(num_1_pow[i]) + float(num_2_pow[i])))
print("The alpha values =", alpha)

#Cum_alpha = np.cumsum(alpha)
DRA_alpha = DRAA/alpha
DR_alpha = DR/alpha
Cum_DR_alpha = np.cumsum(DR_alpha)
Cum_DRA_alpha = np.cumsum(DRA_alpha)
DRB_alpha = DRBB/alpha
Cum_DRB_alpha = np.cumsum(DRB_alpha)
xxx = Cum_DRA_alpha/Cum_DR_alpha
yyy= Cum_DRB_alpha/Cum_DR_alpha
print("x(s) = %.2f" % xxx[4])
print("y(S) = %.2f" % yyy[4])