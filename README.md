# LangGraph Chatbot

A conversational chatbot built with Streamlit, LangGraph, and Groq. Each Streamlit browser session gets its own conversation thread, and messages are kept in memory while the app is running.

## Requirements

- Python 3.11 or newer
- [uv](https://docs.astral.sh/uv/)
- A Groq API key

## Setup

1. Clone the repository and enter its directory:

   ```powershell
   git clone https://github.com/Juggernaut576/Lang-graph_Chatbot.git
   cd Lang-graph_Chatbot
   ```

2. Install dependencies:

   ```powershell
   uv sync
   ```

3. Create a `.env` file in the project root and add your Groq API key:

   ```dotenv
   GROQ_API_KEY=your_groq_api_key
   ```

   The default model is `openai/gpt-oss-20b`. To select another model available to your Groq account, optionally set:

   ```dotenv
   GROQ_MODEL=openai/gpt-oss-20b
   ```

## Run

```powershell
uv run streamlit run app.py
```

Open the local URL printed by Streamlit in your browser.

## Project files

- `app.py` — Streamlit chat interface and per-session conversation history.
- `langgraph_backend.py` — LangGraph chat workflow and Groq model configuration.
- `pyproject.toml` / `uv.lock` — project dependencies and locked versions.

The API key is loaded from `.env`; do not commit that file. Conversation checkpoints are stored in memory and are not retained after the app process stops.
