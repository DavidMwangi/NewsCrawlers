import newspaper

dailynews = newspaper.build('http://www.nation.co.ke/', memoize_articles=False)
#memoize_articles=False parameter opts out of default cache elimination

print(dailynews.brand.capitalize() + ': ' + dailynews.description)


#CACHING ARTICLE NUMBER

print('\nDaily Nation Cached Articles\n')

print(dailynews.size())


#EXTRACTING ARTICLE URLS


for article in dailynews.articles:

    print(article.url)


#EXTRACTING SOURCE CATEGORIES

print('\nDaily Nation Categories\n')

for category in dailynews.category_urls():

    print(category)

#EXTRACTING SOURCE FEEDS

print('\nDaily Nation RSS Feeds\n')

for feed_url in dailynews.feed_urls():

    print (feed_url)
