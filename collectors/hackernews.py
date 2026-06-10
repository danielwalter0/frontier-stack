import feedparser

def collect_hackernews():
    feed = feedparser.parse("https://news.ycombinator.com/rss")

    articles = []

    for entry in feed.entries[:30]:
        articles.append({
            "title": entry.title,
            "url": entry.link,
            "source": entry.link.split("/")[2]
        })

    return articles