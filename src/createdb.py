import psycopg2
from src.connconfig import configure

def create_practice_db():
    """
    drops && creates 'practice' database
    """
    conn = psycopg2.connect(**configure())
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()

    cur.execute("drop database if exists practice;")
    cur.execute("create database practice;")
