from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import xlsxwriter

ticker = 'TSLA'
url = f'http://finance.yahoo.com/quote/{ticker}/options?p={ticker}'
html_text = requests.get(url , headers={'User-Agent': 'Custom'})
#'User-Agent' is there to prevent error 404
soup = BeautifulSoup(html_text.text, 'lxml')
date_selector = soup.find_all('option')
#dropdown menu for option expiry dates
dates = []
date_codes = []
#codes to put into URL
for date in date_selector:
    date_codes.append(date['value'])
    dates.append(date.text)

pattern = re.compile(r"\?")
subbed_urls =[]
#matches = pattern.finditer(url)
for code in date_codes:
    subbed_url = re.sub(pattern, '?'+ code, url)
    subbed_urls.append(subbed_url)
#print(subbed_urls)

dataframes = []

for url in subbed_urls:
    
    html_text = requests.get(url , headers={'User-Agent': 'Custom'})
    soup = BeautifulSoup(html_text.text, 'lxml')

    table_heads = soup.find_all('thead')
    table_bodys = soup.find_all('tbody')

    for head in table_heads:
        headlist = []
        headings = head.find_all('th')
        for head in headings:
            headlist.append(head.text)
        #print(headlist)
    
    table = []
    for body in table_bodys:
        rows = body.find_all('tr')
        for row in rows:
            numlist = []
            data = row.find_all('td')
            for d in data:
                numlist.append(d.text)
            table.append(numlist)
    df = pd.DataFrame(table, columns = headlist)
    dataframes.append(df)
    print(table)
    print(df)

with pd.ExcelWriter(ticker + '.xlsx') as writer:
    i = 0
    for df in dataframes:
        df.to_excel(writer, dates[i])
        i+=1

    

            


    '''
    table_rows = soup.find_all('tr')
    for row in table_rows:
        numlist = []
        numbers = row.find_all('td')
        for number in numbers:
            numlist.append(number.text)
        print(numlist)
        #print(row.text)
        #use th or maybe <span> tag to find headings
 '''
  
#for match in matches:
    #print(match.span())


"""calls = soup.find_all('div', id="mrt-node-Col1-1-OptionContracts")
for call in calls:
    print(call.text)
    """