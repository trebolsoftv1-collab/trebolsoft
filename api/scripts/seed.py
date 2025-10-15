
import os
import psycopg
from uuid import uuid4

url = os.getenv("DATABASE_URL").replace("+psycopg","") if "+psycopg" in os.getenv("DATABASE_URL","") else os.getenv("DATABASE_URL")

sample_customers = [
    {"id": str(uuid4()), "full_name": "Cliente Demo 1", "phone": "3000000001"},
    {"id": str(uuid4()), "full_name": "Cliente Demo 2", "phone": "3000000002"},
]

with psycopg.connect(url) as conn:
    with conn.cursor() as cur:
        for c in sample_customers:
            cur.execute("""
                insert into customers (id, full_name, phone, status)
                values (%s,%s,%s,'activo')
                on conflict (id) do nothing
            """, (c["id"], c["full_name"], c["phone"]))
    conn.commit()
print("Seed OK")
