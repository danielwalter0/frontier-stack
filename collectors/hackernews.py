import feedparser
def collect_hackernews():
    feed = feedparser.parse('https://news.ycombinator.com/rss')
    articles = []
    for entry in feed.entries[:10]:  # Get the top 10 articles
        article = {
            'title': entry.title,
            'link': entry.link,
            'published': entry.published
        }
        articles.append(article)

    return articles