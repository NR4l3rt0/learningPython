my_dictionary = {
    "first" : [1,2,3],
    "second" : "second",
    "third" : True
}

print(my_dictionary)
print(my_dictionary.get("first"))
print(my_dictionary.get("second", "It's there"))
print(my_dictionary.get("333", False))
print(my_dictionary.get(333, ["it's", "not", "there"]))


print(len(my_dictionary))

