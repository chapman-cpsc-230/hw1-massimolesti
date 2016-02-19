import math
x = math.pi/4.0
y = math.sin(x)**2 + math.cos(x)**2
print y

v0 = 3 #m/s
t = 1 #s
a = 2 #m/s**2
s = v0*t + 0.5*a*t**2
print s

a = 3
b = 5
a2 = a**2
b2 = b**2

eq1_sum = a2 + 2*a*b + b2
eq2_sum = a2 - 2*a*b + b2

eq1_pow = (a + b)**2
eq2_pow = (a - b)**2

print 'first equation %g = %g' %(eq1_sum, eq1_pow)
print 'first equation %g = %g' %(eq2_sum, eq2_pow)
