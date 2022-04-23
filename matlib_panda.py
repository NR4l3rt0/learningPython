import pandas as pd
import matplotlib.pyplot as plt

s = pd.Series([18, 42, 9, 32, 81, 64, 3])
s.plot(kind='bar')
plt.savefig('plot.png')
