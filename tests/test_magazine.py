from lib.models.magazine import Magazine
from lib.models.article import Article
from lib.models.author import Author

def test_magazine_creation():
    mag = Magazine.create("Science Weekly", "Science")
    assert mag.id is not None
    assert mag.name == "Science Weekly"

def test_magazine_articles(author, magazine):
    Article.create("Quantum", author.id, magazine.id)
    assert len(magazine.articles()) == 1

def test_magazine_contributors(author, magazine):
    Article.create("AI", author.id, magazine.id)
    contributors = magazine.contributors()
    assert any(author.name in row for row in contributors)

def test_magazine_article_titles(author, magazine):
    Article.create("Neural Nets", author.id, magazine.id)
    assert "Neural Nets" in magazine.article_titles()

def test_magazine_contributing_authors():
    mag = Magazine.create("Dev Digest", "Programming")
    a1 = Author.create("Alice")
    a2 = Author.create("Bob")

    for _ in range(3):
        Article.create("Post", a1.id, mag.id)
    Article.create("Post", a2.id, mag.id)

    contributing = mag.contributing_authors()
    assert any("Alice" in row for row in contributing)
    assert not any("Bob" in row for row in contributing)