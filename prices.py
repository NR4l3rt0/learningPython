import numpy as np


data = np.array([150000, 125000, 320000, 540000, 200000, 120000, 160000, 230000, 280000, 290000, 300000, 500000, 420000, 100000, 150000, 280000])

mean = np.mean(data)

std = np.std(data)

lower_bound = mean - std
upper_bound = mean + std
inside_price = 0

for price in data:
    if price >= lower_bound and price <= upper_bound:
        inside_price = inside_price + 1

percentage = ( inside_price / len(data) ) * 100
print(percentage)
