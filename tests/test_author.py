from lib.models.author import Author
from lib.models.article import Article

def test_author_creation():
    author = Author.create("John Smith")
    assert author.id is not None
    assert author.name == "John Smith"

def test_author_articles(author, magazine):
    Article.create("Title 1", author.id, magazine.id)
    Article.create("Title 2", author.id, magazine.id)
    articles = author.articles()
    assert len(articles) == 2

def test_author_magazines(author, magazine):
    Article.create("Sample", author.id, magazine.id)
    mags = author.magazines()
    assert len(mags) == 1
    assert mags[0][1] == "Tech Monthly"

def test_author_add_article(author, magazine):
    article = author.add_article(magazine, "New Tech")
    assert article.title == "New Tech"
    assert article.author_id == author.id
    assert article.magazine_id == magazine.id

def test_author_topic_areas(author, magazine):
    author.add_article(magazine, "Innovation")
    assert author.topic_areas() == ["Technology"]