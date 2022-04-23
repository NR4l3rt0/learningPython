in_str = input("Enter a word\n")
in_ltr = input("Enter a letter\n")

print(in_str, in_ltr)
ocurr = in_str.count(in_ltr)
length = len(in_str)
ratio = int(ocurr / length * 100)
print(ratio)
