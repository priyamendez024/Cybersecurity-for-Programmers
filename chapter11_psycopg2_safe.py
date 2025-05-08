import psycopg2

def get_user(email):
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    cur.execute("SELECT id, name, role FROM users WHERE email = %s;", (email,))
    return cur.fetchone()