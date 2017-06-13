import newspaper

cnn_paper = newspaper.build('http://www.nation.co.ke/')

"""
for article in cnn_paper.articles:

    print(article.url)
"""


print(cnn_paper.size())
