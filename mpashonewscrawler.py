import newspaper

mpashonews = newspaper.build('https://mpasho.co.ke/', memoize_articles=False)
#memoize_articles=False parameter opts out of default cache elimination

print(mpashonews.brand.capitalize() + ': ' + mpashonews.description)


#CACHING ARTICLE NUMBER

print('\nMpasho Cached Articles\n')

print(mpashonews.size())


#EXTRACTING ARTICLE URLS


for article in mpashonews.articles:

    print(article.url)


#EXTRACTING SOURCE CATEGORIES

print('\nMpasho Categories\n')

for category in mpashonews.category_urls():

    print(category)

#EXTRACTING SOURCE FEEDS

print('\nMpasho RSS Feeds\n')

for feed_url in mpashonews.feed_urls():

    print (feed_url)
