# shoes and athlete deals chart

from pprint import pprint
import yahoo_finance
from yahoo_finance import Share
import plotly as plotly
import plotly.plotly as py
import plotly.graph_objs as go

from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd

from pandas_datareader import data as pdr

import fix_yahoo_finance as yf


#question: do shoe deals for star NBA players increase price of stock?

#stock price needs: Nike, Adidas, Under Armor, Li-Ning

def fix():
	yf.pdr_override()
	stocks= ['NKE', 'ADDYY', 'UAA']
	events= {'NKE':'2003-05-21', 'ADDYY':'2015-08-15', 'UAA':'2015-09-15'}
	anno = {'NKE':'Lebron James- $90 million', 'ADDYY': 'James Harden- $14 million',
	'UAA':'Steph Curry- $12 million'}

	for i in stocks:
		data =yf.download(i, start="2000-01-01", end="2018-01-01")
		data ['index1'] = data.index
		point = events[i]
		#print list(data.columns.values)
		#data = [go.Scatter(x=data['index1'], y=data['Close'])]
		#url= py.plot(data, filename='basic-line')
		data.plot(x='index1', y='Close')
		plt.axvline(x=point)
		plt.xlabel('Date')
		plt.ylabel('Closing Price')
		plt.title('{} shoe deal for {}'.format(i, anno[i]))
		plt.show()
		#plt.savefig('i-fig.png')
		

def price():
	stocks= ['NKE', 'ADDYY', 'UAA']
	data_source= 'yahoo'

if __name__ == "__main__":
	#price()
	fix()
