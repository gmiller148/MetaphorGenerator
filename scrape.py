import requests
from bs4 import BeautifulSoup

url = 'https://www.basketballforcoaches.com/basketball-terms/'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

# print(soup.prettify())

terms = set()
for tag in soup.find_all('strong'):
    t = tag.get_text()
    t = t.replace(' -','')
    t = t.replace('\xa0','')
    terms.add(t)

terms.remove('-- 1, 2, 3-')
terms.remove('')
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWZ'
for letter in list(alpha):
    terms.remove(f'-- {letter}-')
print(terms)

with open('resources/terms.txt','w') as f:
    f.write(str(terms))