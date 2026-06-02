from collectors.hackernews import collect_hackernews
from ai.gemini import generate_posts
from publisher.telegram import send_message
import json
import asyncio


articles = collect_hackernews()

articles_text = "\n\n".join([f"{article['title']} ({article['link']})" for article in articles])
gemini_output = generate_posts(articles_text)

posts = json.loads(gemini_output)
for post in posts:
    asyncio.run(send_message(post['message']))

