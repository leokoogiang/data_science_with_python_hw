import random
x = []
y = []

for i in range(0,100):
    x_i = random.uniform(0,10)
    x.append(x_i)
    y_i = (x_i**2)/(x_i/4)
    y.append(y_i)

print(x)
print(y)