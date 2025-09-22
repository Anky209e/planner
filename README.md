## Example Output

**Plan for: Plan a dinner date in Delhi**

	1. Wake up at 8:00 AM and attempt to book a table at Varq, a fine dining restaurant in Delhi, for 8:00 PM.
	2. Log on to the restaurant's website or a table booking platform and fill out the reservation form with your name, phone number, and the number of guests.
	3. Choose a fixed-price menu that includes a 5-course meal and a wine pairing.
	4. At 10:00 AM, call the restaurant to confirm the booking and request a table with a view of the garden.
	5. At 11:00 AM, buy a bouquet of red roses from a local florist to present to your date.
	6. At 12:00 PM, pick up your date's favorite dessert from a bakery in Delhi.
	7. At 2:00 PM, get dressed in formal attire, including a black suit and a tie for men, or a cocktail dress for women.
	8. At 6:00 PM, pick up your date from their residence and drive to the restaurant.
	9. At 7:30 PM, arrive at the restaurant and hand over the bouquet of roses to your date.
	10. At 8:00 PM, be seated at the reserved table and begin the 5-course meal.
	11. At 10:30 PM, present the dessert to your date and end the evening with a romantic walk around the garden.

**Weather:** 2025-09-22: max 24.8°C, min 24.1°C, precipitation 0.3mm, code 80

**Plan for: Plan a trip to Spain**

Here's a 2-day plan to help you plan a trip to Spain:

* **Day 1**
	* Research destinations in Spain (morning)
	* Look into popular cities like Madrid, Barcelona, Seville, and Granada
	* Consider factors like travel time, accommodation options, and activities
	* Determine travel dates and duration (afternoon)
	* Decide on the best time to visit Spain based on weather, festivals, and personal preferences
	* Choose a duration that fits your schedule and budget
	* Create a rough itinerary (evening)
	* Outline the places you want to visit and the activities you want to do
	* Consider transportation options between destinations
* **Day 2**
	* Research accommodation options (morning)
	* Look into hotels, hostels, and vacation rentals in each destination
	* Compare prices, locations, and amenities
	* Plan activities and book tickets (afternoon)
	* Research top attractions, museums, and experiences in each destination
	* Book tickets or tours in advance to avoid sold-out situations
	* Estimate budget and start making travel arrangements (evening)
	* Calculate costs for transportation, accommodation, food, and activities
	* Start booking flights, trains, or other transportation, and make reservations for accommodation

**Weather:** 2025-09-22: max 24.8°C, min 24.1°C, precipitation 0.3mm, code 80

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


## Example Output

**Plan for: Plan a dinner date in Delhi**

	1. Wake up at 8:00 AM and attempt to book a table at Varq, a fine dining restaurant in Delhi, for 8:00 PM.
	2. Log on to the restaurant's website or a table booking platform and fill out the reservation form with your name, phone number, and the number of guests.
	3. Choose a fixed-price menu that includes a 5-course meal and a wine pairing.
	4. At 10:00 AM, call the restaurant to confirm the booking and request a table with a view of the garden.
	5. At 11:00 AM, buy a bouquet of red roses from a local florist to present to your date.
	6. At 12:00 PM, pick up your date's favorite dessert from a bakery in Delhi.
	7. At 2:00 PM, get dressed in formal attire, including a black suit and a tie for men, or a cocktail dress for women.
	8. At 6:00 PM, pick up your date from their residence and drive to the restaurant.
	9. At 7:30 PM, arrive at the restaurant and hand over the bouquet of roses to your date.
	10. At 8:00 PM, be seated at the reserved table and begin the 5-course meal.
	11. At 10:30 PM, present the dessert to your date and end the evening with a romantic walk around the garden.

**Weather:** 2025-09-22: max 24.8°C, min 24.1°C, precipitation 0.3mm, code 80

## License
MIT
