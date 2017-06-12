from newspaper import Article

url = str(input(">"))

article = Article(url)

article.download()

article.parse()

print(article.authors)

print(article.publish_date)

print(article.text)

"""

print(article.top_image)

print(article.movies)

article.nlp()

print(article.keywords)

print(article.summary)

"""
