# Travel Planner X

Travel Planner X is an intelligent, interactive travel planning application designed to help users plan custom travel itineraries with ease. It features an AI-powered chat interface, interactive map, personalized attraction recommendations, and dynamic itinerary and budget generation.

---

## Features

- **Conversational Planning:** Chat with the AI assistant to describe your preferences and receive tailored travel suggestions.
- **Interactive Map:** Visualize recommended attractions and your itinerary on an interactive map (powered by Leaflet & OpenStreetMap).
- **Personalized Recommendations:** Get attraction suggestions based on your selected city and interests, with details and paginated browsing.
- **Itinerary Generation:** Automatically build a day-by-day itinerary and estimated budget based on your choices.
- **Nearby Places Info:** See restaurants and points of interest near each attraction.
- **Seamless UX:** Reset your session, auto-scroll through popular places, and navigate easily with step indicators.

---

## Technologies Used

- **Backend:** Python (likely Flask/FastAPI), serving as the main API.
- **Frontend:** JavaScript, HTML, CSS (Bootstrap, custom styles).
- **Mapping:** Leaflet.js with OpenStreetMap tiles.
- **Data Visualization:** Dynamic display of attractions, itinerary, and route.
- **Other:** Marked.js for Markdown rendering, MutationObserver for UI enhancements.

---

## Getting Started

### Prerequisites

- Python 3.8+
- Node.js & npm (for frontend asset builds, if needed)
- (Recommended) Virtualenv for Python dependencies

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/A-janjan/travel_planner_x.git
   cd travel_planner_x
   ```

2. **Install backend dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Frontend setup (if applicable):**
   - If there's a `package.json` in `frontend/`, run:
     ```bash
     cd frontend
     npm install
     # Build assets if needed
     npm run build
     cd ..
     ```

4. **Run the application:**
   ```bash
   # Example for Flask
   export FLASK_APP=main.py
   flask run
   # Or, python main.py
   ```

5. **Access the app:**
   - Open [http://localhost:5000](http://localhost:5000) in your browser.

---

## Usage

1. **Start a conversation:** Use the chat interface to describe your trip (destination, interests, dates, budget).
2. **Explore recommendations:** Browse and select from recommended attractions, view details, and see their map locations.
3. **Generate itinerary:** Confirm your selection to receive an optimized itinerary and budget estimate.
4. **Review & refine:** Ask for adjustments, reset your plan, or explore nearby places for each attraction.

---

## Project Structure

```
main.py                      # Backend API and logic
/frontend
  /static
    /js/main.js              # Main frontend logic (UI, chat, map, recommendations)
/templates                   # HTML templates
README.md                    # Project documentation
requirements.txt             # Python dependencies
```

---

## Contributing

Pull requests and suggestions are welcome! Please fork the repo and submit your ideas.

---

## License

**Proprietary** – This project is currently private.

---

## Author

- [A-janjan](https://github.com/A-janjan)

---

*Travel Planner X – Plan smarter, travel better!*
