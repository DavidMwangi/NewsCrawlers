import newspaper

tukonews = newspaper.build('https://www.tuko.co.ke/', memoize_articles=False)
#memoize_articles=False parameter opts out of default cache elimination

print(tukonews.brand.capitalize() + ': ' + tukonews.description)


#CACHING ARTICLE NUMBER

print('\nTuko Cached Articles\n')

print(tukonews.size())


#EXTRACTING ARTICLE URLS


for article in tukonews.articles:

    print(article.url)


#EXTRACTING SOURCE CATEGORIES

print('\nTuko Categories\n')

for category in tukonews.category_urls():

    print(category)

#EXTRACTING SOURCE FEEDS

print('\nTuko RSS Feeds\n')

for feed_url in tukonews.feed_urls():

    print (feed_url)
