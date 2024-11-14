import random

test_amount = 50000
results = []

for i in range(0,test_amount):
    tries = 0
    while True:
        tries += 1
        if random.randint(1,10000) <= 83:
            results.append(tries)
            break

avg = sum(results) / len(results)
print(avg)