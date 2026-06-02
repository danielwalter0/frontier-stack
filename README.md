# Frontier Stack

An AI-powered news intelligence pipeline that automatically discovers, evaluates, and publishes high-signal technology news.

Frontier Stack collects stories from trusted sources, uses Google's Gemini to assess relevance against a defined editorial focus, and publishes curated content directly to Telegram.

The goal is to eliminate information overload by filtering out noise and surfacing only the most important developments in technology, AI, privacy, infrastructure, and the future of the internet.

---

## Features

- Automated news collection from Hacker News
- AI-powered relevance evaluation using Gemini
- Configurable editorial filtering
- Automated Telegram publishing
- Modular architecture for easy expansion
- Lightweight and easy to deploy
- Environment-variable based configuration

---

## Architecture

```text
Hacker News
     │
     ▼
 News Collector
     │
     ▼
 Gemini Relevance Analysis
     │
     ▼
 Content Selection
     │
     ▼
 Telegram Publisher
     │
     ▼
 Telegram Channel
```

---

## Project Structure

```text
frontier-stack/
│
├── ai/
│   └── gemini.py
│
├── collectors/
│   └── hackernews.py
│
├── publisher/
│   └── telegram.py
│
├── main.py
├── .env
├── .gitignore
└── README.md
```

---

## Tech Stack

- Python
- Google Gemini API
- Telegram Bot API
- Hacker News API

---

## Installation

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/frontier-stack.git

cd frontier-stack
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key

TELEGRAM_BOT_TOKEN=your_telegram_bot_token

TELEGRAM_CHAT_ID=your_channel_or_chat_id
```

---

## Usage

Run the pipeline:

```bash
python main.py
```

The workflow:

1. Fetch stories from Hacker News
2. Send stories to Gemini for evaluation
3. Filter based on relevance criteria
4. Publish selected content to Telegram

---

## Current Capabilities

- Hacker News ingestion
- AI-based relevance scoring
- Automated Telegram delivery

---

## Roadmap

### Near Term

- Better relevance prompts
- Improved article ranking
- Duplicate detection
- Multiple news sources
- Rich Telegram formatting

### Future

- Multi-channel publishing
- Scheduled posting
- Web dashboard
- Analytics and performance tracking
- Human review mode
- Personalized editorial profiles

---

## Why Frontier Stack?

Modern technology news is overwhelmed by hype, clickbait, and repetitive coverage.

Frontier Stack is designed to function as an intelligent editorial layer that identifies meaningful developments in technology and delivers only high-value information to readers.

Instead of consuming everything, readers receive only what matters.

---

## Contributing

Contributions, ideas, and improvements are welcome.

Feel free to open an issue or submit a pull request.

---

## License

MIT License

Feel free to use, modify, and distribute this project.

---

## Disclaimer

This project is an experimental AI-assisted content curation system. All generated content should be reviewed before being relied upon as factual reporting.
