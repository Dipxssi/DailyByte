# fetches medium articles
import feedparser
import logging
import time 
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def fetch_articles(topic):
  url = f"https://medium.com/feed/tag/{topic}"

  retries = 3
  wait = 2

  for attempt  in range(retries):
    try:
      feed = feedparser.parse(url)
      if feed.status == 200 and len(feed.entries)> 0 :
        articles = []
        for entry in feed.entries[:10]:
          articles.append({
            "title": entry.title,
            "link": entry.link,
            "summary": BeautifulSoup(entry.summary, "html.parser").get_text(),
            "id": entry.id,
            "tags": [tag['term'] for tag in entry.get('tags', [])]
          })
        return articles
      else:
        logging.warning(f"Attempt {attempt + 1} failed")
        time.sleep(wait)
        wait *=2
    except Exception as e:
      logging.warning(f"Attempt {attempt + 1} failed")
      time.sleep(wait)
      wait *=2
  return []
      

      


  
  
