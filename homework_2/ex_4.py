import random
n = int(input('Please enter the number of times of generating randomly number: '))
list = []
for i in range(n):  
    x = random.randint(0,11)
    list.append(x)
print(list)
print('The number of number in the list:', len(list))
print('The max value is: ', max(list))
print('The min value is: ', min(list))
mean = sum(list)/len(list)
print('Mean is: ', mean)

