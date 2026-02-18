import numpy.random as rnd
import matplotlib.pyplot as plt
import math

###############################################################

#Implementierung der beiden Schätzer:

#Schätzer 1:
def MC_1(n):
    X = rnd.uniform(high=math.pi, size=n+1)
    Y = rnd.random(size=n+1)
    agg_ind = 0
    for i in range(n+1):
        if Y[i] < math.sin(X[i]):
            agg_ind = agg_ind + 1
    return((math.pi/float(n+1))*float(agg_ind))

#Schätzer 2:
def MC_2(n):
    X = rnd.uniform(high=math.pi, size=n+1)
    e_2 = 0
    for i in range(n+1):
        e_2 = e_2 + math.sin(X[i])
    return((math.pi/float(n+1))*float(e_2))

###############################################################

#Aufgabenteil a)
values_estimator_1 = []
values_estimator_2 = []
for n in range(10**3):
    values_estimator_1.append(MC_1(n+1))
    values_estimator_2.append(MC_2(n+1))

plt.plot(range(10**3), values_estimator_1, label = "Erster Schätzer")
plt.plot(range(10**3), values_estimator_2, label = "Zweiter Schätzer")
plt.xlabel("Stichprobengröße")
plt.ylabel("Erwartungswert")
plt.legend(loc = "best")
plt.show()

###############################################################

#Aufgabenteil b)
m = 10**4
emp_var_1 = 0
emp_var_2 = 0

#n = 10**4
#for n in range(m):
#    emp_var_1 = emp_var_1 + ((MC_1(n) - 2)**2)*(1/m)
#    emp_var_2 = emp_var_2 + ((MC_2(n) - 2)**2)*(1/m)

for n in range(m):
    X = rnd.uniform(high=math.pi, size=10**4)
    Y = rnd.random(size=10**4)
    agg_ind = 0
    e_2 = 0
    for i in range(10**4):
        if Y[i] < math.sin(X[i]):
            agg_ind = agg_ind + 1
        
        e_2 = e_2 + math.sin(X[i])
    emp_var_1 = emp_var_1 + (((math.pi/float(10**4))*float(agg_ind) - 2)**2)*(1/m)
    emp_var_2 = emp_var_2 + (((math.pi/float(10**4))*float(e_2) - 2)**2)*(1/m)
print(emp_var_1)
print(emp_var_2)