#Runs everything daily
import os
import logging 
from dotenv import load_dotenv
from scraper import fetch_articles
from summariser import summarise
from database import init_db , is_article_seen , mark_article_seen
from whatsapp import send_message 
from apscheduler.schedulers.blocking import BlockingScheduler 

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

scheduler = BlockingScheduler()

@scheduler.scheduled_job('cron', hour=19 , minute=0)

def job():
  topic = os.getenv("MEDIUM_TOPIC")
  articles = fetch_articles(topic)

  for article in articles:
    if not is_article_seen(article['id']):
      logging.info(f"Summarising: {article['title']}")
      result = summarise(article['title'] , article['summary'], model = "llama3.2")
      if result:
        send_message(result)
        mark_article_seen(article['id'],article['title'])
        break
    else:
        logging.warning("No new articles found today!")



if __name__ =="__main__":
  init_db()
  scheduler.start()