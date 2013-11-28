import sqlite3
import os
import praw

_useragent = 'Autoposter v0.1 (/u/xoran99)'

class Controller:
    _conn = None 
    _path = None
    _sessions = dict()

    def __init__(self, path='~/.reddit_autopost.db'):
        self._path = os.path.expanduser(path)

    def conn(self):
        if self._conn == None:
            self._conn = sqlite3.connect(path)
        return self._conn

    def initialize_database(self, path):
        """Create table with appropriate schema in path"""
        self.conn().executescript("""
            CREATE TABLE config
            (
                key TEXT,
                value TEXT
            );
            CREATE TABLE posts 
            (
                postid INTEGER PRIMARY KEY AUTOINCREMENT,
                poster TEXT NOT NULL,
                subreddit TEXT NOT NULL,
                datetime TEXT NOT NULL,
                selfpost INTEGER NOT NULL DEFAULT 0,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                time_posted TEXT DEFAULT NULL,
                FOREIGN KEY (poster) REFERENCES user(username)
            );
            CREATE TABLE users
            (
                username TEXT NOT NULL,
                password TEXT NOT NULL
            );
            INSERT INTO config VALUES ('Database Version', '2013112700');
            """)
        self.conn().commit()

    def makepost(self, username, password, subreddit, title, content, is_selfpost):
        if username in self._sessions:
            r = self._sessions[username]
        else:
            r = praw.Reddit(_useragent)
            r.login(username, password)
            self._sessions[username] = r
        url = content
        if is_selfpost:
            text = content
            url = None
        else:
            url = content
            text = None 
        r.submit(subreddit, title, text, url)


# vim: set sw=4 ts=4 expandtab:
