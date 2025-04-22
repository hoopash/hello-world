import psycopg2

# Connect using environment variables
conn = psycopg2.connect("")  # Empty string = use PG* environment variables

# Test the connection
cursor = conn.cursor()
cursor.execute("SELECT version();")
print(cursor.fetchone())
cursor.close()
conn.close()