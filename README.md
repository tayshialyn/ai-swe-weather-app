# 🌤️ Weather App

A mobile-friendly web weather app built using Python and Flask. It allows users to input a city name and get real-time temperature data using the Open-Meteo API. The app features a responsive UI built with Bootstrap 5 and simple form-based interaction.

---

## 🚀 Features

- 🔍 City-based weather search
- 📡 Real-time temperature fetched from [Open-Meteo](https://open-meteo.com/)
- ⚠️ Graceful error handling for unknown cities
- 📱 Mobile-first, responsive layout using Bootstrap 5
- 💡 Clean and minimal interface

---

## 🧠 How AI Helped

I used **ChatGPT** throughout the development process to:

- Set up a clean project folder structure for Flask
- Write the Python code for calling the Open-Meteo API
- Solve a `jinja2.exceptions.TemplateNotFound` error
- Debug import issues related to Flask blueprints
- Style the HTML page using Bootstrap for mobile responsiveness
- Compose this `README.md` and a project summary for documentation

This accelerated my learning and helped me focus on building and understanding rather than getting stuck on small issues.

---

## 💬 Reflection

### What I Learned:
- Flask application structure, blueprints, and routing
- Making HTTP requests and parsing JSON in Python
- Rendering templates dynamically with Jinja2
- Using Bootstrap for mobile-first design

### What Was Challenging:
- Understanding how Flask locates templates (resolved with help from AI)
- Connecting front-end forms to back-end logic cleanly

### 🌟 Something I'm Proud Of:
- The app works end-to-end — city input to real weather output — with a clean and responsive interface.

### 🔧 Something I Would Improve:
- Add weather condition icons and descriptions (e.g., "Cloudy", "Rainy")
- Integrate a 5-day forecast view
- Add °C/°F toggle and optional geolocation support
- Use JavaScript for dynamic updates without full page reload

---

## 🛠️ Tech Stack

- Python 3.10+
- Flask
- HTML5, CSS3
- Bootstrap 5
- Open-Meteo API
- Jinja2

---

## 📦 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/your-username/weather-app.git
cd weather-app
```

### 2. Create a virtual environment
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Flask app
```bash
python run.py
```

### Project Structure
```bash
weather_app/
├── app/                        # Core backend logic
│   ├── __init__.py             # Initialize Flask app
│   ├── routes.py               # Web routes and views
│   ├── api.py                  # Functions to call Open-Meteo API
│   ├── parser.py               # Format/parse weather data
│   └── utils.py                # Helper functions
│
├── static/                     # Frontend assets (CSS, JS, images)
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
│
├── templates/                  # HTML templates (Jinja2)
│   └── index.html
│
├── config/                     # Configuration files
│   ├── __init__.py
│   └── settings.py
│
├── tests/                      # Tests for API and logic
│   ├── test_api.py
│   └── test_parser.py
│
├── run.py                      # Entry point to run the Flask app
├── requirements.txt            # Dependencies
├── .env                        # Environment variables
├── .gitignore                  # Ignore __pycache__, .env, etc.
└── README.md
```