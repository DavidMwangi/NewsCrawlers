import newspaper


mpashonews = newspaper.build('https://mpasho.co.ke/', memoize_articles=False)
#memoize_articles=False parameter opts out of default cache elimination

print(mpashonews.brand.capitalize() + ': ' + mpashonews.description)


#CACHING ARTICLE NUMBER

print('\nMpasho Cached Articles\n')

print(mpashonews.size())

articles = list()


for category in mpashonews.category_urls():

    print(category)

#EXTRACTING ARTICLE URLS


for article in mpashonews.articles:

    article.download()

    article.parse()

    print(article.title + '\n')


    
#print(articles)
