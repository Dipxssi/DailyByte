# code that talks with database

import sqlite3

def init_db():
  conn = sqlite3.connect("data/dailybyte.db")
  cursor = conn.cursor()
  cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS seen_articles(
                 id  TEXT PRIMARY KEY ,
                 title TEXT,
                 seen_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                 )
""")
  conn.commit()
  conn.close()

def is_article_seen(article_id):
  conn = sqlite3.connect("data/dailybyte.db")
  cursor = conn.cursor()
  cursor.execute("SELECT id FROM seen_articles WHERE id =? " , (article_id ,))
  result = cursor.fetchone()
  conn.close()
  return result is not None

def mark_article_seen(article_id , title):
  conn = sqlite3.connect("data/dailybyte.db")

  cursor = conn.cursor()
  cursor.execute("INSERT INTO seen_articles (id , title ) VALUES(?,?)", (article_id , title ,))
  conn.commit()
  conn.close() 