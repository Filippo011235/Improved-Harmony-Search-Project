import math
x = [1.8, 0.2]
fact1a = (x[0] + x[1] + 1)**2
fact1b = 19 - 14*x[0] + 3*x[0]**2 - 14*x[1] + 6*x[0]*x[1] + 3*x[1]**2
fact1 = 1 + fact1a*fact1b

fact2a = (2*x[0] - 3*x[1])**2
fact2b = 18 - 32*x[0] + 12*x[0]**2 + 48*x[1] - 36*x[0]*x[1] + 27*x[1]**2
fact2 = 30 + fact2a*fact2b

y = fact1*fact2
wzor = str(y)
print(eval(wzor))