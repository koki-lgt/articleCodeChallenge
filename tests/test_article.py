from lib.models.article import Article

def test_article_creation(author, magazine):
    article = Article.create("Tech Trends", author.id, magazine.id)
    assert article.title == "Tech Trends"
    assert article.author_id == author.id
    assert article.magazine_id == magazine.id

def test_article_find_by_id(author, magazine):
    article = Article.create("Cloud Computing", author.id, magazine.id)
    found = Article.find_by_id(article.id)
    assert found.title == "Cloud Computing"