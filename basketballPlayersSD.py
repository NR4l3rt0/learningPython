import math

players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]

print(players)

total = total2 = inside_std = 0

for height in players:
    total = total + height

mean = total / len(players)

print(mean)

for height in players:
    total2 = total2 + ((  height - mean ) ** 2 )

variance = total2 / len(players)

#standard_deviation = variance ** (1/2)
standard_deviation = math.sqrt(variance)

print(standard_deviation)

low_bound = mean - standard_deviation
upper_bound = mean + standard_deviation

for height in players:
    if height >= low_bound and height <= upper_bound:
        inside_std = inside_std + 1

print(inside_std)
