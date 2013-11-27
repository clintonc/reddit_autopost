import sqlite3
import os

def initialize_database(path):
    """Create table with appropriate schema in path"""
    sql = """
        CREATE TABLE posts 
        (
            postid INTEGER PRIMARY KEY AUTOINCREMENT,
            poster TEXT NOT NULL,
            subreddit TEXT NOT NULL,
            datetime TEXT NOT NULL,
            selfpost INTEGER NOT NULL DEFAULT 0,
            content TEXT NOT NULL,
            time_posted TEXT DEFAULT NULL,
            FOREIGN KEY (poster) REFERENCES user(username)
        );"""
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute(sql)
    sql = """
        CREATE TABLE users
        (
            username TEXT NOT NULL,
            password TEXT NOT NULL
        );"""
    c.execute(sql)
    conn.commit()

initialize_database('test.db')
            
# vim: set sw=4 ts=4 expandtab:
