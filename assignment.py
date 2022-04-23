# It is a multiple assingment not a reference (at least with primitives)
job1 = job2 = job3 = 'super job'
job2 = 'new job'
print(job1) # super
print(job2) # new
print(job3) # super

# multiple assignment different values but one line
name, height, is_funny = 'Bob', 1.77, False

print(name)
print(height)
print(is_funny)

