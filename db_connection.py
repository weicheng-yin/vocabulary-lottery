import psycopg2

# Update connection string information
dbname = "database"
host = "localhost"
port = "5433"
user = "postgres"
password = "password"
sslmode = "allow"

# Construct connection string
conn_string = f"host={host} user={user} dbname={dbname} password={password} sslmode={sslmode} port={port}"
conn = psycopg2.connect(conn_string)
print("Connection established")
