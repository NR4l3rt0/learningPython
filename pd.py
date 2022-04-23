import pandas as pd

data = [12, 22.2, 2999]

s = pd.Series(data)

print(s)
print(s.describe())


data_frame = {
    "names" : [ 'Peter', 'Bob', 'Sue' ],
    "ages" : [ 33, 25, 55 ],
    "other" : data
}

df = pd.DataFrame(data_frame)

print(df)

