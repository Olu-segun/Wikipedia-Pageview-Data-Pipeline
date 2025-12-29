import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os

load_dotenv()

def load_company_views(transformed_views):
    try:
        conn = psycopg2.connect(
            host=os.getenv("PGHOST"),
            dbname=os.getenv("PGDATABASE"),
            user=os.getenv("PGUSER"),
            password=os.getenv("PGPASSWORD"),
            port=os.getenv("PGPORT")
        )
        cur = conn.cursor()

        # Create table if not exists
        cur.execute("""
            CREATE TABLE IF NOT EXISTS wikipedia (
                id SERIAL PRIMARY KEY,
                page_title VARCHAR(100),
                views INTEGER
            );
        """)

        # Insert query
        insert_query = sql.SQL(
            "INSERT INTO {table} (page_title, views) VALUES (%s, %s)"
        ).format(table=sql.Identifier("wikipedia"))

        # Convert DataFrame rows into list of tuples
        records = list(transformed_views.itertuples(index=False, name=None))

        # Bulk insert
        cur.executemany(insert_query, records)

        conn.commit()
        print(f"Successfully inserted {len(records)} records.")

        cur.close()
        conn.close()

    except psycopg2.Error as e:
        print(f"Database error: {e}")
        if conn:
            conn.rollback()
            conn.close()
