from pickle import TRUE
from bs4 import BeautifulSoup
import re
import pandas as pd
'''
with open('Uoft login.html', 'r') as html_file:
	content = html_file.read()
	#print(content)
	soup = BeautifulSoup(content,"lxml")
	tags = soup.find_all('p')
	for tag in tags:
		print(tag.text)
soup = BeautifulSoup(content, 'lxml')
tabs = soup.find_all('li')
for tab in tabs:
	print(tab.text)

with open("Nucor 2021 10K HTML.html", 'r') as html:
	content = html.read()
	soup = BeautifulSoup(content, 'lxml')
	#tables = soup.find_all(id="CONSOLIDATED_BALANCE_SHEETS")
	tables = soup.find_all(format="ixt:numdotdecimal")
	tags = soup.find_all(True)
	tables_2 = soup.find_all('table', border="0")
	
	for table in tables:
		print(table.text)
	for tag in tags:
		print(tag.name)
	for table in tables_2:
		print(table.text)'''

def has_span_but_no_class(tag):
	return tag.has_attr('span') and not tag.has_attr('class')
with open('Nucor Yahoo HTML.html','r') as html:
	content = html.read()
	soup = BeautifulSoup(content, 'lxml')
	#tables = soup.find_all(id = 'mrt-node-Col1-1-Financials')
	tables = soup.find_all(class_ = 'rw-expnded')
	dic = {}
	for table in tables:
		titles = table.find_all('span',class_ = 'Va(m)')
		numbers = table.find_all('span',class_ = '')
		numlist = []
		for number in numbers:
			numlist.append(number.text)
		#pattern = re.compile(r'\d\d\d?,[0-9]{3},[0-9]{3}')
		#matches = pattern.finditer(table.text)
		#for match in matches:
			#print(match)
		#print(type(table))
		#print(table.text)
		#for title in titles:
			#print(title)
		#for number in numbers:
			#print(number)
		dic[titles[0].text]=numlist
		
	#print(tables[0])
	print(dic)
	df = pd.DataFrame.from_dict(data = dic, orient = 'index')
	print(df)
	df.to_excel('Nucor Income Statement.xlsx')
	#df = (df.T)
	#print(df)
