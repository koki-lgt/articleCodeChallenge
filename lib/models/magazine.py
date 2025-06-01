from lib.db.connection import get_connection

class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category

    @classmethod
    def create(cls, name, category):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?) RETURNING id", (name, category))
        mag_id = cursor.fetchone()[0]
        conn.commit()
        conn.close()
        return cls(mag_id, name, category)

    @classmethod
    def find_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        return cls(*row) if row else None

    def articles(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE magazine_id = ?", (self.id,))
        results = cursor.fetchall()
        conn.close()
        return results

    def contributors(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT au.* FROM authors au
            JOIN articles ar ON au.id = ar.author_id
            WHERE ar.magazine_id = ?
        """, (self.id,))
        results = cursor.fetchall()
        conn.close()
        return results

    def article_titles(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT title FROM articles WHERE magazine_id = ?", (self.id,))
        titles = [row[0] for row in cursor.fetchall()]
        conn.close()
        return titles

    def contributing_authors(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT au.* FROM authors au
            JOIN articles ar ON au.id = ar.author_id
            WHERE ar.magazine_id = ?
            GROUP BY au.id
            HAVING COUNT(ar.id) > 2
        """, (self.id,))
        results = cursor.fetchall()
        conn.close()
        return results