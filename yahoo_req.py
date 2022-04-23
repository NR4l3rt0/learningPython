import pandas as pd
import requests

url_link = 'https://finance.yahoo.com/quote/TSLA/profile'
r = requests.get(url_link,headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})

data = pd.read_html(r.text)
print(data[0]) 


## Scrape and plot example
#import pandas as pd
#import requests
#import matplotlib.pyplot as plt
#
#url_link = 'https://finance.yahoo.com/quote/TSLA/analysis?p=TSLA'
#r = requests.get(url_link,headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
#
#data = pd.read_html(r.text)
#data = data[0]
#data = data[data['Earnings Estimate'] == 'Avg. Estimate']
#
#data.plot(kind='bar')
#
#plt.savefig('plot.png')
