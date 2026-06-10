from collectors.hackernews import collect_hackernews
from ai.gemini import generate_posts
from publisher.telegram import send_message
import json
import asyncio


articles = collect_hackernews()

# Pass the article list directly
gemini_output = generate_posts(articles)

if gemini_output is None:
    print("Failed to generate posts.")
    exit()

gemini_output = gemini_output.strip()

# Safety cleanup if Gemini still wraps JSON
if gemini_output.startswith("```"):
    gemini_output = gemini_output.replace("```json", "")
    gemini_output = gemini_output.replace("```", "")
    gemini_output = gemini_output.strip()

print("Generated Telegram posts:")
print(gemini_output)

posts = json.loads(gemini_output)

for post in posts:
    # Depends on your Gemini schema
    message = f"{post['title']}\n\n{post['summary']}"
    asyncio.run(send_message(message))