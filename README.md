# event-intelligence-ai

An autonomous, multi-agent AI system designed to discover, scrape, parse, and validate upcoming event information from the web.

## 📂 Project Structure

```text
event-intelligence-ai/
├── agents/                  # Multi-agent orchestration layer
│   ├── __init__.py
│   └── discovery.py         # Coordinates search, scraping, and parsing workflows
│
├── core/                    # Core project configurations and types
│   ├── __init__.py
│   └── models.py            # Pydantic data schemas for strict type validation
│
├── tools/                   # Modular utility toolkit
│   ├── __init__.py
│   ├── search.py            # Web search utility (DuckDuckGo / LLM Search)
│   ├── browser.py           # Headless browser automation for data retrieval
│   ├── parser.py            # Text extraction and HTML cleaning engine
│   └── validator.py         # Schema checking and data cleansing tool
│
├── tests/                   # Test suite
│   └── test_search.py       # Unit tests for search components
│
├── logs/                    # Execution and error tracking logs
├── data/                    # Local storage for extracted event files
│
├── requirements.txt         # Project dependencies
├── main.py                  # Project entry point
└── .env                     # Local environment variables
```

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have **Python 3.10+** installed on your system.

### 2. Installation
Clone the repository and install the required dependencies:

```bash
# Clone the repository
git clone https://github.com
cd event-intelligence-ai

# Install Python dependencies
pip install -r requirements.txt

# Install Playwright browser binaries (if using browser automation)
playwright install chromium
```

### 3. Configuration
Create a `.env` file in the root directory and add your secret API keys:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### 4. Running the Application
Execute the main script to start the discovery pipeline:

```bash
python main.py
```

### 5. Running Tests
Run your test suite using `pytest`:

```bash
pytest
```

## 🛠️ Tech Stack
* **Framework:** Pydantic (Data Validation), Loguru (Logging)
* **Scraping & Automation:** Playwright, BeautifulSoup4, HTTPX
* **Data Processing:** Pandas
* **Search:** DuckDuckGo Search API
