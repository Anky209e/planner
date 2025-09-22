
# AI Agent Planner

A modern AI-powered planner web app that generates confident, actionable, day-by-day plans for any goal, enriched with real-time web search and weather info.

## Features
- Accepts a natural language goal
- Auto-detects user location
- Generates a 3-day plan with clear, direct instructions
- Enriches each step with web search (Serper API) and weather info
- Beautiful, modern UI with navbar, animations, and responsive design
- Saves plan history in a local SQLite database

## Setup Instructions

### 1. Clone the repository
```sh
git clone https://github.com/Anky209e/planner.git
cd planner
```

### 2. Install dependencies
```sh
pip install -r requirements.txt
```

### 3. Set up environment variables
Create a `.env` file in the project root with the following keys:
```
GROQ_API_KEY=your_groq_api_key
SERPER_API_KEY=your_serper_api_key
```

### 4. Run the app
```sh
python app.py
```
The app will start on `http://127.0.0.1:5000/`

## Usage
- Enter your goal in the search bar and submit.
- The app will auto-detect your location and generate a confident, actionable plan for 3 days.
- View plan details and history via the navbar.

## Project Structure
```
planner/
├── app.py                # Flask app entry point
├── src/
│   ├── planner.py        # Plan generation and enrichment logic
│   ├── db.py             # SQLite persistence
│   ├── tools.py          # Weather and web search functions
├── templates/
│   ├── index.html        # Home page
│   ├── plan.html         # Plan details page
│   ├── history.html      # Plan history page
├── requirements.txt      # Python dependencies
├── plans.db              # SQLite database (auto-created)
├── .env                  # API keys (not committed)
```

## Notes
- Only the goal is required; location is auto-detected.
- All code is validated and ready for production submission.
- Unused files and config have been removed for a clean codebase.

## License
MIT
