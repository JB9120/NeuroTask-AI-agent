
import sqlite3
import os
from datetime import datetime

DB = "database.db"

def get_conn():
    return sqlite3.connect(DB)

def init_db():
    conn = get_conn()
    conn.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE,
        password_hash TEXT,
        created_at TEXT
    )
    """)
    conn.execute("""
    CREATE TABLE IF NOT EXISTS todos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        text TEXT,
        remind_time TEXT,
        priority TEXT,
        status TEXT DEFAULT 'PENDING',
        created_at TEXT
    )
    """)
    conn.commit()
    conn.close()

def create_user(email, password_hash):
    conn = get_conn()
    conn.execute(
        "INSERT INTO users (email, password_hash, created_at) VALUES (?, ?, ?)",
        (email, password_hash, str(datetime.now()))
    )
    conn.commit()
    conn.close()

def get_user(email):
    conn = get_conn()
    user = conn.execute(
        "SELECT id, password_hash FROM users WHERE email=?",
        (email,)
    ).fetchone()
    conn.close()
    return user

def add_todo(user_id, text, remind_time, priority):
    conn = get_conn()
    conn.execute(
        "INSERT INTO todos (user_id, text, remind_time, priority, created_at) VALUES (?, ?, ?, ?, ?)",
        (user_id, text, remind_time, priority, str(datetime.now()))
    )
    conn.commit()
    conn.close()

def get_pending():
    conn = get_conn()
    rows = conn.execute(
        "SELECT id, text, remind_time, priority FROM todos WHERE status='PENDING'"
    ).fetchall()
    conn.close()
    return rows
