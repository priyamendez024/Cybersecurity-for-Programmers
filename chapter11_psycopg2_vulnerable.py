import psycopg2

def get_user(email):
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    query = "SELECT id, name, role FROM users WHERE email = '%s';" % email
    cur.execute(query)
    return cur.fetchone()