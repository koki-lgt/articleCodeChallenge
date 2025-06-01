from lib.db.connection import get_connection

def authors_for_magazine(magazine_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT DISTINCT au.* FROM authors au
        JOIN articles ar ON au.id = ar.author_id
        WHERE ar.magazine_id = ?
    """, (magazine_id,))
    return cursor.fetchall()

def magazines_with_multiple_authors():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT m.id, m.name FROM magazines m
        JOIN articles a ON a.magazine_id = m.id
        GROUP BY m.id
        HAVING COUNT(DISTINCT a.author_id) >= 2
    """)
    return cursor.fetchall()

def article_counts_per_magazine():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT m.name, COUNT(a.id) as article_count
        FROM magazines m
        LEFT JOIN articles a ON m.id = a.magazine_id
        GROUP BY m.id
    """)
    return cursor.fetchall()

def most_prolific_author():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT au.name, COUNT(a.id) as count FROM authors au
        JOIN articles a ON au.id = a.author_id
        GROUP BY au.id
        ORDER BY count DESC LIMIT 1
    """)
    return cursor.fetchone()