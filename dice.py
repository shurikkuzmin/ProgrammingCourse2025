import random
import matplotlib.pyplot as plt

num = 100000

arr = [0] * 13 

for i in range(num):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2

    arr[total] = arr[total] + 1

for i in range(2, 13):
    arr[i] = arr[i] / num
    print("Probability of rolling a", i, "is", arr[i])

plt.bar(range(13),arr)
plt.show()
#plt.bar(range(2, 13), arr[2:13])