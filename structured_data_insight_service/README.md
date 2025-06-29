# 📊 Structured Data Insight Generator

Upload a CSV → get profiling + AI-generated insights.

## Usage
- `POST /profile` — returns shape, columns, types, missing, stats.
- `POST /insights` — runs profiling then asks an LLM to provide trends & suggestions.

## Run locally
```bash
pip install -r requirements.txt
export OPENAI_API_KEY=your_key_here
uvicorn app.main:app --reload

