#Import required libraries
import math

print("The Python program creates polygon")
print()


n = int(input("Enter the number of sides:"))

print('\n')

#A list that stores all entered Coordinates. It´s empty at start    
x = []
y = []

#Input Coordinates
print ("Enter x and y coordinates:")

print('\n')

for i in range (n):
    
    print('Point '+str(i)+':')
    x.append(float(input(f"x[{i+1}]: ")))
    y.append(float(input(f"y[{i+1}]: ")))
    print('\n')
    
    
print('\n')
print(f"{'Point':10} {'x':10} {'y':10}")
print("-" * 30)

for i in range(n):
    print(f"{i+1:<10d} {x[i]:<10.2f} {y[i]:<10.2f}")

print ("Geometric charateristics:")

print('\n')

#Ax
Ax = 0.0
for i in range(n-1):
    Ax = Ax + ( (x[i+1] + x[i]) * (y[i+1] - y[i]) ) 
Ax = Ax/2 
print('Ax :', Ax)

#Sx
Sx = 0.0
for i in range(n-1):
    Sx = Sx + ( (x[i+1] - x[i]) * (y[i+1]**2 + y[i]* y[i+1] + y[i]**2) ) 
Sx = -Sx/6
print('Sx :', Sx)

#Sy
Sy = 0.0
for i in range(n-1):
    Sy = Sy + ( (y[i+1] - y[i]) * (x[i+1]**2 + x[i] * x[i+1] + x[i]**2))
Sy = Sy/6
print('Sy :', Sy)

#Ix
Ix = 0.0
for i in range(n-1):
    Ix = Ix + ( (x[i+1] - x[i]) * (y[i+1]**3 + y[i+1]**2 * y[i+1] * y[i]**2 + y[i]**3))
Ix = -Ix/12
print('Ix :', Ix)

#Iy
Iy = 0.0
for i in range(n-1):
    Iy = Iy + ( (y[i+1] - y[i]) * (x[i+1]**3 + x[i+1]**2 * x[i+1] * x[i]**2 + x[i]**3))
Iy = Iy/12
print('Iy :', Iy)

#Ixy
Ixy = 0.0
for i in range(n-1):
    Ixy = Ixy + (y[i+1] - y[i]) * (y[i+1] * (3* x[i+1]**2 + 2 * x[i] * x[i+1] + x[i]**2) + y[i] * (3 * x[i]**2 + 2 * x[i] * x[i+1] + x[i+1]**2))
Ixy = -Ixy/24
print('Ixy :', Ixy)

#Xt
Xt = 0.0
for i in range(n-1):
    Xt = (Sy)/(Ax)
print('Xt :', Xt)

#Yt
Yt = 0.0
for i in range(n-1):
    Yt = (Sx)/(Ax)
print('Yt :', Yt)

#Itx
Itx = 0.0
for i in range(n-1):
    Itx = Ix - Yt**2 * Ax
print('Itx :', Itx)

#Ity
Ity = 0.0
for i in range(n-1):
    Ity = Iy - Xt**2 * Ax
print('Ity :', Ity)

#Itxy
Itxy = 0.0
for i in range(n-1):
    Itxy = Ixy + Xt * Yt * Ax
print('Itxy :', Itxy)
