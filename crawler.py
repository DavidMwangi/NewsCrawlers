import requests
from readability import Document

response = requests.get('https://www.nytimes.com/2017/02/23/us/politics/cpac-stephen-bannon-reince-priebus.html?hp&_r=0')
doc = Document(response.text)
print(doc.content())
