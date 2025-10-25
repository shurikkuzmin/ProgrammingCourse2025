import random
count = 0
total = 10000000
for i in range(total):
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    if x**2 + y**2 <= 1:
        count = count + 1
pi_estimate = (count / total) * 4
print("Estimated value of Pi:", pi_estimate)
