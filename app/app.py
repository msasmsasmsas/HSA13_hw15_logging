from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import mysql.connector
import os
from typing import List, Dict

app = FastAPI()

db_config = {
    "host": os.getenv("DATABASE_HOST", "mysql"),
    "user": os.getenv("DATABASE_USER", "testuser"),
    "password": os.getenv("DATABASE_PASSWORD", "testpassword"),
    "database": os.getenv("DATABASE_NAME", "testdb")
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.get("/slow")
async def slow(timeout: int = Query(2, alias="timeout")):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT SLEEP(%s);"
    cursor.execute(query, (timeout,))
    conn.close()
    return JSONResponse(content={})

@app.get("/search", response_model=List[Dict])
async def search_users(name: str = Query("")):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM users WHERE name LIKE %s"
    cursor.execute(query, (name,))
    users = cursor.fetchall()
    conn.close()
    return JSONResponse(content=users)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)