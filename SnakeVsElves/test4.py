import random

x = 0
y = 0

vel = 16

for i in range(random.randint(0, 10)):
    x += vel
    print(x, y)
for i in range(random.randint(0, 10)):
    x -= vel
    print(x, y)
for j in range(random.randint(0, 10)):
    y += vel
    print(x, y)
for j in range(random.randint(0, 10)):
    y -= vel
    print(x, y)