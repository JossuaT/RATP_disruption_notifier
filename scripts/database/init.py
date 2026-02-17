import subprocess, os, psycopg2
from dotenv import load_dotenv


# Création de l'image docker
subprocess.run(
    ["docker", "compose", "-f", "scripts/database/compose.yaml", "up"],
    capture_output=True,
    shell=True
)


# Connexion à la base de données
load_dotenv()
conn = psycopg2.connect(
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PW"),
    host=os.getenv("HOST"),
    port=os.getenv("PORT"),
    dbname=os.getenv("POSTGRES_DB")
)
cur = conn.cursor()


# Exécution des scripts sql
with open("sql/create_db.sql", "r") as f:
    cur.execute(f.read())
with open("sql/create_shemas.sql", "r") as f:
    cur.execute(f.read())
cur.close(), conn.close()
