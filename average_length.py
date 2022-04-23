text = input()
split_txt = text.split()
total = blanks = 0

for length in split_txt:
    total += len(length)

print(total/len(split_txt))
