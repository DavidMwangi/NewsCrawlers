import newspaper

allafrica = newspaper.build('http://allafrica.com/', memoize_articles=False)
#memoize_articles=False parameter opts out of default cache elimination

print(allafrica.brand.capitalize() + ': ' + allafrica.description)


#CACHING ARTICLE NUMBER

print('\nAll Africa News Cached Articles\n')

print(allafrica.size())


#EXTRACTING ARTICLE URLS


for article in allafrica.articles:

    print(article.url)


#EXTRACTING SOURCE CATEGORIES

print('\nAll Africa Categories\n')

for category in allafrica.category_urls():

    print(category)

#EXTRACTING SOURCE FEEDS

print('\nAll Africa News RSS Feeds\n')

for feed_url in allafrica.feed_urls():

    print (feed_url)
