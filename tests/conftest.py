import pytest
import os
import sqlite3
from lib.db.connection import DB_PATH
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

@pytest.fixture(autouse=True)
def setup_database():
    # Reset DB before each test
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    with open("lib/db/schema.sql") as f:
        schema = f.read()

    conn = sqlite3.connect(DB_PATH)
    conn.executescript(schema)
    conn.commit()
    conn.close()

    yield

@pytest.fixture
def author():
    return Author.create("Jane Doe")

@pytest.fixture
def magazine():
    return Magazine.create("Tech Monthly", "Technology")

@pytest.fixture
def article(author, magazine):
    return Article.create("AI and the Future", author.id, magazine.id)