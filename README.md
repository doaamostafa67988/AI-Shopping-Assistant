# 🛍️ AI Shopping Assistant

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CrewAI](https://img.shields.io/badge/CrewAI-Agentic%20AI-FF6B6B?style=for-the-badge)
![Serper](https://img.shields.io/badge/Serper-Google%20Search-4285F4?style=for-the-badge&logo=google&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)

**An intelligent multi-agent shopping assistant powered by CrewAI that finds, analyzes, and recommends the best products — so you don't have to.**

[Features](#-features) • [Architecture](#-architecture) • [Installation](#-installation) • [Usage](#-how-to-run) • [Future Plans](#-future-improvements)

</div>

---

## 📖 Project Description

**AI Shopping Assistant** is an agentic AI application built with [CrewAI](https://github.com/joaomdmoura/crewAI) that automates the product research and recommendation process. The user simply provides a product name (and optionally preferred e-commerce websites), and two specialized AI agents collaborate to search the web, collect product data, analyze options, and return the best recommendations based on **price**, **quality**, and **ratings**.

No more tab-hopping across Amazon, Noon, or eBay — let the agents do the heavy lifting.
**Try it live:** [AI Shopping Assistant](https://ai-shopping-assistant-gf.streamlit.app/)
---

## 🎬 Demo / Overview

```
User Input  →  "Find me the best wireless noise-cancelling headphones under $150"

🤖 Researcher Agent  →  Searches Google via Serper API, collects product listings
🧠 Analyst Agent     →  Ranks products by price, quality & ratings
 Final Output      →  Clean, structured recommendations with links
```

> **Example platforms supported:** Amazon, Noon, eBay, Best Buy, AliExpress, or any custom URL the user provides.

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     AI Shopping Assistant                    │
│                        (CrewAI Crew)                        │
└─────────────────────────────────────────────────────────────┘
                              │
              ┌───────────────┼───────────────┐
              ▼                               ▼
   ┌─────────────────────┐       ┌─────────────────────────┐
   │     Researcher      │       │     Analyst Agent       │
   │       Agent         │       │                         │
   │                     │       │  - Receives raw data    │
   │  - Accepts product  │──────▶│ - Scores & ranks       │
   │    name + websites  │       │    products             │
   │  - Queries Serper   │       │  - Filters by price,    │
   │    API (Google)     │       │    quality & ratings    │
   │  - Returns raw      │       │  - Returns structured   │
   │    product data     │       │    recommendations      │
   └─────────────────────┘       └─────────────────────────┘
              │                               │
              ▼                               ▼
   ┌─────────────────────┐       ┌─────────────────────────┐
   │   🌐 Serper API     │       │     Final Output        │
   │  (Google Search)    │       │                         │
   │                     │       │  Top N product picks    │
   │  Live web results   │       │  with prices, ratings,  │
   │  Product listings   │       │  links & summary        │
   └─────────────────────┘       └─────────────────────────┘
```

---

## 🤖 Agents Explanation

### 1. 🔍 Researcher Agent

| Property | Details |
|----------|---------|
| **Role** | Product Research Specialist |
| **Goal** | Search the web and collect comprehensive product data matching the user's query |
| **Tools** | Serper API (Google Search) |
| **Behavior** | Queries multiple e-commerce platforms, extracts product titles, prices, ratings, and links |

### 2. 🧠 Analyst Agent

| Property | Details |
|----------|---------|
| **Role** | Product Analysis & Recommendation Expert |
| **Goal** | Analyze the collected data and rank the best products |
| **Tools** | None (pure LLM reasoning) |
| **Behavior** | Evaluates products based on price-to-quality ratio, user ratings, and availability. Returns a ranked recommendation list with justification |

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| 🐍 **Python 3.10+** | Core programming language |
| 🤖 **CrewAI** | Multi-agent orchestration framework |
| 🔎 **Serper API** | Google Search integration for live product data |
| 🧠 **Groq** | LLM backbone for both agents |
| 📦 **python-dotenv** | Environment variable management |

---

## ⚙️ Installation

### Prerequisites

- Python 3.10 or higher
- A [Serper API key](https://serper.dev/) (free tier available)
- An [Groq API key](https://console.groq.com/keys)

### Steps

**1. Clone the repository**

```bash
git clone https://github.com/your-username/ai-shopping-assistant.git
cd ai-shopping-assistant
```

**2. Create and activate a virtual environment**

```bash
# Create virtual environment
python -m venv venv

# Activate — macOS/Linux
source venv/bin/activate

# Activate — Windows
venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:



Then fill in your keys:

```env
# .env

# Groq API Key — https://console.groq.com/keys/
GROQ_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Serper API Key — https://serper.dev/
SERPER_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# (Optional) LLM Model — defaults to Llama
llM_MODEL_NAME=llama-4-scout-17b-16e-instruct
```

> ⚠️ **Never commit your `.env` file.** It is already included in `.gitignore`.

---

## ▶️ How to Run

```bash
python app.py
```

You will be prompted to enter:

```
🛍️  Welcome to AI Shopping Assistant
────────────────────────────────────
Enter product name     : wireless noise-cancelling headphones
Enter max budget (USD) : 150
Enter preferred sites  : amazon.com, noon.com (or press Enter to search all)
```

The agents will then run sequentially and print the final recommendations to the terminal.

---

## 📌 Example Input & Output

### Input

```
Product     : wireless noise-cancelling headphones
Budget      : $150
Websites    : amazon.com, noon.com
```

### Output

```
============================================================
 🏆 AI Shopping Assistant — Top Recommendations
============================================================

1. Sony WH-1000XM4 Wireless Headphones
   💰 Price   : $148.00
   ⭐ Rating  : 4.8 / 5  (32,410 reviews)
   🔗 Link    : https://amazon.com/...
   📝 Why?    : Industry-leading noise cancellation, 30-hr battery,
                best price-to-quality ratio in this range.

2. Anker Soundcore Q45
   💰 Price   : $79.99
   ⭐ Rating  : 4.5 / 5  (12,890 reviews)
   🔗 Link    : https://amazon.com/...
   📝 Why?    : Budget-friendly with solid ANC. Ideal if you want
                to stay well under the $150 limit.

3. Jabra Evolve2 55
   💰 Price   : $149.00
   ⭐ Rating  : 4.6 / 5  (5,210 reviews)
   🔗 Link    : https://noon.com/...
   📝 Why?    : Professional-grade mic quality, great for remote work.

============================================================
✅ Research completed in 18.4s | Powered by CrewAI + Serper
============================================================
```

---

## 📁 Project Structure

## 📁 Project Structure

```text
AI-Shopping-Assistant/
│
├── .env                  # Environment variables (API keys)
├── .gitignore            # Git ignore file
├── app.py                # Main application entry point (Streamlit UI)
├── LICENSE               # License file
├── README.md             # Project documentation
│
├── crew/                 # Multi-agent configuration and logic
│   ├── __pycache__/
│   ├── agents.py         # Agent definitions
│   ├── crew_setup.py     # Crew orchestration setup
│   ├── llm.py            # LLM configuration
│   └── tasks.py          # Task definitions
│
├── tools/                # Custom tools for agents
│   ├── __pycache__/
│   └── search_tool.py    # Search integration tool
│
└── utils/                # Utility modules
    └── schemas.py        # Data models and schemas
```

---

## ✨ Features

- 🤖 **Multi-Agent Architecture** — Two specialized agents with distinct roles working in sequence
- 🔎 **Live Google Search** — Real-time product data via Serper API, not a static database
- 🛒 **Platform Flexibility** — Works with any e-commerce site the user specifies
- 💰 **Budget-Aware** — Analyst Agent filters and ranks within the user's price range
- ⭐ **Quality Scoring** — Rankings factor in price, user ratings, and review count
- 📋 **Structured Output** — Clean, readable recommendations with direct purchase links
- ⚡ **Fast Execution** — Typical query completes in under 30 seconds

---

## 🔮 Future Improvements

- [ ] 🖥️ **Web UI** — Build a Streamlit or Next.js frontend for a polished user experience
- [ ] 💱 **Multi-Currency Support** — Auto-convert prices based on user region
- [ ] 🗂️ **Product Comparison Table** — Side-by-side spec comparison for shortlisted items
- [ ] 💾 **Search History** — Save and revisit past recommendation sessions
- [ ] 🔔 **Price Drop Alerts** — Monitor a product and notify when the price falls
- [ ] 🌐 **Multi-Language Output** — Return recommendations in the user's preferred language
- [ ] 📊 **Sentiment Analysis** — Parse review text to surface common pros and cons

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---



