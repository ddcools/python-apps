# First Program
print("OM GANESHA")

x = 1
y = "abc"

print(type(x))
print(type(y))

a, b, c = 1, 2, 4

print(a)
print(b)
print(c)


print(a,b,c)
print(a + b + c)

xyz = 1
def printMessage():
  print("HELLO Morning")
  global xyz
  xyz = 333
  print(xyz)


printMessage()

print(xyz)

import random

print(random.randrange(1,10))

a = 1
b = float(a)
print(b)


name = "Dheeresha"

for i in name:
  print(i)
  print(len(name))
  print('eaere' in name)

if 'eere1' in name:
  print("Present!")
else:
  print("Not Present!")


if "eeee" not in name:
  print("Not present!")

print(name[:8])


b = "Hello, World!"
print(b[-5:-2])
