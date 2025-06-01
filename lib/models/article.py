from lib.db.connection import get_connection

class Article:
    def __init__(self, id, title, author_id, magazine_id):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.magazine_id = magazine_id

    @classmethod
    def create(cls, title, author_id, magazine_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO articles (title, author_id, magazine_id)
            VALUES (?, ?, ?) RETURNING id
        """, (title, author_id, magazine_id))
        article_id = cursor.fetchone()[0]
        conn.commit()
        conn.close()
        return cls(article_id, title, author_id, magazine_id)

    @classmethod
    def find_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        return cls(*row) if row else None