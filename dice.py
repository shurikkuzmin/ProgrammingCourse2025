import random
import matplotlib.pyplot as plt

num = 500000
num_dices = 5

arr = [0] * (6 *num_dices + 1) 

for i in range(num):
    total = 0
    for j in range(num_dices):
        dice = random.randint(1, 6)
        total = total + dice

    arr[total] = arr[total] + 1

for i in range(num_dices, 6 * num_dices + 1):
    arr[i] = arr[i] / num
    print("Probability of rolling a", i, "is", arr[i])

plt.bar(range(6*num_dices + 1),arr)
plt.show()
