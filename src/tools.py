import os
from dotenv import load_dotenv
load_dotenv()
import requests

# Simple web search using Serper API (no wrapper)
def serper_search(query: str) -> str:
    api_key = os.getenv("SERPER_API_KEY")
    if not api_key:
        return "Serper API key not set."
    url = "https://google.serper.dev/search"
    headers = {"X-API-KEY": api_key, "Content-Type": "application/json"}
    payload = {"q": query}
    try:
        resp = requests.post(url, headers=headers, json=payload)
        print(f"Serper API response status: {resp.status_code}")
        print(f"Serper API response text: {resp.text}")
        if resp.status_code != 200:
            return f"No relevant web info found (Serper API returned status {resp.status_code})."
        data = resp.json()
        results = []
        for item in data.get("organic", []):
            if item.get("snippet"):
                results.append(item["snippet"])
        return "\n".join(results[:3]) if results else "No relevant web info found."
    except Exception as e:
        print(f"Serper API error: {e}")
        return f"Serper API error: {e}"

# Simple weather lookup using Open-Meteo API (no wrapper)
def get_weather(lat: float, lon: float, days: int = 3) -> str:
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum,weathercode",
        "current_weather": True,
        "timezone": "auto"
    }
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    data = resp.json()
    daily = []
    for i in range(min(days, len(data.get("daily", {}).get("time", [])))):
        daily.append(f"{data['daily']['time'][i]}: max {data['daily']['temperature_2m_max'][i]}°C, min {data['daily']['temperature_2m_min'][i]}°C, precipitation {data['daily']['precipitation_sum'][i]}mm, code {data['daily']['weathercode'][i]}")
    return "\n".join(daily)
