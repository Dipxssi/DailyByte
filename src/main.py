from database import init_db
from scheduler import job , scheduler

if __name__ == "__main__":
  init_db()
  job()
  scheduler.start()
