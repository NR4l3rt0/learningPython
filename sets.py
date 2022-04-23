my_set = { 1, 3, 4 }
print("This is my set {}".format(my_set))

my_set.add(5)
print(my_set)

my_set.remove(1)
print(my_set)

my_set.add(5)
print(my_set)

# Operations with sets
my_other = {5, "letter", "sunshine"}
print(my_set | my_other)
print(my_set & my_other)
print(my_set - my_other)
print(my_other - my_set)
print(my_set ^ my_other)
