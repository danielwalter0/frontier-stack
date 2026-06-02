from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)
def generate_posts(articles_text):
    genai_response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
    You are the editor of Frontier Stack.

    Frontier Stack focuses on:
    - open-source AI
    - decentralized systems
    - privacy technology
    - developer tools
    - future internet infrastructure

    Ignore:
    - generic startup news
    - funding announcements
    - influencer news
    - marketing content
    - low-signal AI hype

    Articles:

    {articles_text}

    Select the 3 most relevant stories.

    For each story create a concise Telegram post explaining:
    - what happened
    - why it matters

    Return ONLY valid JSON.

    Format:

    [
    {{
        "message": "..."
    }}
    ]

    Rules:
    - Return exactly 3 objects.
    - No markdown.
    - No code fences.
    - No explanations.
    - No text outside JSON.
    - Keep each message under 500 characters.
    """
    )
    return genai_response.text
