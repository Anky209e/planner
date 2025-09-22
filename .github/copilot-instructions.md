# Copilot Instructions for AI Coding Agents

## Project Overview
This is an AI agent planner for generating structured, multi-day plans based on user goals and location. The system uses multiple agents, external APIs, and a database for persistence.

## Architecture & Key Components
- **src/planner.py**: Main orchestration logic. Defines agents (Planner, Enricher) and their tasks. Uses CrewAI for agent/task management.
- **src/tools.py**: Provides wrappers for external APIs:
  - `serper_search`: Uses GoogleSerperAPIWrapper for web search (requires `SERPER_API_KEY`).
  - `get_weather`: Fetches weather data from OpenWeatherMap (requires `WEATHER_API_KEY`).
- **src/db.py**: Handles SQLite persistence for plans. Defines the `Plan` model and CRUD functions (`save_plan`, `get_plan`, `get_history`).
- **src/config/**: Reserved for agent/task configuration (currently empty, but may be used for YAML-based agent/task definitions).

## Data Flow
1. User provides a goal and location.
2. Planner agent breaks the goal into day-wise tasks.
3. Enricher agent augments each day with web search and weather info.
4. Final plan is saved to the database.

## Developer Workflows
- **Run the app**: Entry point is `app.py`. Flask application for handling requests.
- **Database**: Uses SQLite (`plans.db`). Schema auto-created via `init_db()` in `db.py`.
- **API Keys**: Set `SERPER_API_KEY` and `WEATHER_API_KEY` as environment variables for external API access.
- **Testing**: No explicit test files found. Add tests in a `tests/` directory and document test commands if/when available.

## Project-Specific Patterns
- **Agent Roles**: Agents are defined with clear roles and goals. See `planner.py` for examples.
- **Tool Mapping**: Tools are mapped in a dictionary and passed to agents.
- **Plan Storage**: Plans are stored as JSON in the database.

## Integration Points
- **CrewAI**: Used for agent/task orchestration.
- **LangChain**: Used for search API wrapper.
- **OpenWeatherMap**: For weather data.
- **Google Serper**: For web search.

## Example: Adding a New Agent
- Define agent role, goal, and tools in `planner.py`.
- Add any new tool wrappers to `tools.py`.
- Update data persistence logic in `db.py` if needed.

## References
- `src/planner.py`: Agent/task orchestration
- `src/tools.py`: API wrappers
- `src/db.py`: Persistence
- `src/config/`: (future) YAML config

---
**Update this file if you add new agents, tools, or workflows.**
