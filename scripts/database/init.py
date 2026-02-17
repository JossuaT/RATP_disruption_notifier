import subprocess, os, psycopg2
from dotenv import load_dotenv


# Création de l'image docker
results = subprocess.run(
    ["docker", "compose", "-f", "scripts/database/compose.yaml", "up", "-d"],
    capture_output=True,
    shell=True
)
print (results.stdout, results.stderr)


# Connexion à la base de données
load_dotenv()
conn = psycopg2.connect(
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PW"),
    host=os.getenv("HOST"),
    port=os.getenv("PORT"),
    dbname=os.getenv("POSTGRES_DB")
)
conn.autocommit = True
cur = conn.cursor()

# Exécution des scripts sql
with open("./scripts/database/sql/create_db.sql", "r") as f:
    try:
        cur.execute(f.read())
    except psycopg2.errors.DuplicateDatabase:
        print ("Database already exists, skipping.")
with open("./scripts/database/sql/create_shemas.sql", "r") as f:
    cur.execute(f.read())
cur.close(), conn.close()
