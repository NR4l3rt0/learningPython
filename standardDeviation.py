import math

data_set = [14, 18, 19, 24, 26, 33, 42, 55, 67] 

total = total2 = 0

for num in data_set:
    total = total + num

mean = total / len(data_set)

for num in data_set:
    total2 = total2 + ((  num - mean ) ** 2 )

variance = total2 / len(data_set)

#standard_deviation = variance ** (1/2)
standard_deviation = math.sqrt(variance)

print("SD is +/-{}".format(standard_deviation))

