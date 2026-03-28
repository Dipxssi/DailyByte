#sends articles to ollama

import ollama
import logging
import time

logging.basicConfig(level = logging.INFO , format = '%(asctime)s - %(levelname)s - %(message)s')

def summarise(title , summary , model = "llama3.2"):
  system_prompt = """
You are a daily learning assistant and teacher.


Your job:
1. Extract the most interesting buzzword or concept from this article
2. Write ONE line explaining what it is in simple english
3. Write 2-3 lines maximum explaining why it matters

Rules:
- Never make up information
- Keep it conversational and friendly
- Format it for WhatsApp (short, readable, no complex markdown)
- If you cannot find a clear buzzword just say so

Format your response exactly like this:
Buzzword: ???
What is it: ???
Why it matters: ???
"""
  retries = 3
  wait = 2

  for attempt in range(retries):
    try:
      response = ollama.chat(
        model = model,
        messages = [
          {"role": "system" , "content": system_prompt},
          {"role": "user" , "content":f"Title: {title}\nContent: {summary}" }
        ]
      )
      return response['message']['content']
    except Exception as e: 
      logging.warning(f"Attempt {attempt + 1} failed - {str(e)}")
      time.sleep(wait)
      wait *=2
  return None

