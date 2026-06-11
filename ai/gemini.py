from google import genai
from dotenv import load_dotenv
import os
import json

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

PROMPT = """
You are the lead editor of Frontier Stack, a premium technology news channel for developers, engineers, AI builders, founders, and technology professionals.

Your task is to analyze the provided articles, identify the most important stories, and create concise news summaries.

Think like:

* Hacker News
* The Information
* Stratechery
* A senior software engineer

Never think like a general news outlet.

SCORING CRITERIA

Silently score each article using:

* Industry Impact (40%)
* Builder Relevance (25%)
* Novelty (20%)
* Long-Term Significance (15%)

PRIORITIZE

* AI model releases
* AI agents and automation
* Open-source projects
* Developer tools
* Programming languages
* Cloud and infrastructure
* Cybersecurity
* Databases
* Semiconductors
* Robotics
* Scientific computing
* Startup funding
* Acquisitions
* Big Tech strategy shifts
* Major research breakthroughs

DEPRIORITIZE

* Opinion pieces
* Personal blogs
* Celebrity news
* Lifestyle content
* Minor feature updates
* Marketing announcements
* Rumors
* Speculation
* Clickbait

HACKER NEWS RULES

Articles related to:

* GitHub projects
* Open source software
* AI research
* Developer tools
* Infrastructure
* Engineering
* Databases
* Programming languages

should receive a positive ranking adjustment.

Opinion articles and hot takes should receive a negative ranking adjustment unless they contain genuinely important new information.

SELECTION RULES

* Select only the strongest stories.
* Quality is more important than quantity.
* Impact is more important than popularity.
* Prefer significance over virality.
* Remove duplicate stories covering the same topic.
* Ignore weak or low-signal articles.

INPUT LIMITATIONS

Articles may contain only titles, URLs, and sources.

When article content is unavailable:

* Use only information directly implied by the title.
* Never invent facts, features, specifications, performance claims, numbers, partnerships, or announcements.
* If a title is too vague to summarize accurately, skip it.
* Accuracy is more important than completeness.

TARGET OUTPUT

* Select 3-5 stories maximum.
* Fewer stories are preferred if only a small number are truly important.
* Do not force weak stories into the output.

OUTPUT FORMAT

Return ONLY valid JSON.

[
{
"title": "HEADLINE",
"summary": "SUMMARY"
}
]

HEADLINE RULES

* ALL CAPS
* Maximum 8 words
* Professional
* Attention-grabbing
* No emojis
* No hashtags
* No clickbait

SUMMARY RULES

* 2-3 sentences
* Explain what happened
* Explain why it matters
* Focus on likely impact
* Stay strictly within available information
* No emojis
* No hashtags
* No markdown

ARTICLES:

{ARTICLES}

Process:

1. Score all articles.
2. Rank them.
3. Select the best stories.
4. Generate the final JSON.

Return ONLY the JSON array.
"""

def generate_posts(articles):
    """
    articles example:

    [
        {
            "title": "macOS Container Machines",
            "url": "https://github.com/apple/container/blob/main/docs/container-machine.md",
            "source": "github.com"
        }
    ]
    """

    try:
        articles_json = json.dumps(
            articles,
            ensure_ascii=False,
            separators=(",", ":")
        )
        
        prompt = PROMPT.replace(
            "{articles}", 
            articles_json
        )

        print(prompt[:5000])
        
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt,
            
            config={
                "response_mime_type": "application/json",
                "temperature": 0.5,
                "top_p": 0.9,
            }
        )

        return response.text.strip()

    except Exception as e:
        print(f"Error generating posts: {e}")
        return None
    
