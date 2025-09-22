from .tools import serper_search, get_weather
from dotenv import load_dotenv
load_dotenv()
import os
from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)

def generate_plan(goal: str, location: dict) -> dict:
    # Step 1: Use LLM to break goal into day-wise tasks
    prompt = PromptTemplate(
        input_variables=["goal"],
        template="""
        You are an expert planner. Break the goal into a day-by-day plan for 3 days. Goal: {goal}
        Output each day as a list of clear, confident, direct instructions (not suggestions or options).
        Do not use words like 'consider', 'could', 'might', 'suggest', 'option', 'possible', 'try', 'if you want'.
        Be decisive and specific. Use imperative sentences.
        """
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    plan_text = chain.run(goal=goal)
    print(f"LLM plan response: {plan_text}")

    # Parse LLM output into per-day tasks
    # Handle '**Day N**', 'Day N:', and similar formats
    import re
    # Split on lines that start with Day N or **Day N**
    day_pattern = re.compile(r"(?:^|\n)\s*(?:\*\*)?Day\s*(\d+)(?:\*\*)?[:\-]?", re.IGNORECASE)
    day_indices = [m.start() for m in day_pattern.finditer(plan_text)]
    day_indices.append(len(plan_text))

    enriched_days = []
    for i in range(len(day_indices)-1):
        day_content = plan_text[day_indices[i]:day_indices[i+1]].strip()
        lines = [l.strip() for l in day_content.split('\n') if l.strip()]
        tasks = [l for l in lines if not re.match(r"^(\*\*)?Day\s*\d+(\*\*)?[:\-]?", l, re.IGNORECASE)]
        search_info = serper_search(f"{goal} Day {i+1} places/events")
        weather_info = get_weather(location['lat'], location['lon'], 1)
        enriched_days.append({
            "day": i+1,
            "tasks": tasks,
            "search": search_info,
            "weather": weather_info
        })

    # Fallback: if no days parsed, show LLM output as a single day
    if not enriched_days:
        search_info = serper_search(f"{goal} places/events")
        weather_info = get_weather(location['lat'], location['lon'], 1)
        enriched_days = [{
            "day": 1,
            "tasks": [plan_text],
            "search": search_info,
            "weather": weather_info
        }]

    return {
        "goal": goal,
        "location": location,
        "days": enriched_days,
        "llm_output": plan_text
    }
