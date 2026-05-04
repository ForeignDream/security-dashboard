# Security Incident Dashboard

A beginner-level web dashboard for visualizing security incidents, built with Python, Flask, SQLite, and Plotly.

This is a personal portfolio project developed to practice web development and data visualization applied to cybersecurity concepts.

---

## Features

- **Incidents by Type** — Bar chart showing the distribution of attack types (Malware, Phishing, DDoS, Social Engineering, Unauthorized Access)
- **Incidents by Severity** — Donut chart showing the proportion of High, Medium, and Low severity incidents
- **Incidents Over Time** — Line chart displaying incident trends by month

---

## Tech Stack

- **Backend:** Python, Flask, Flask-SQLAlchemy
- **Database:** SQLite
- **Charts:** Plotly.js
- **Frontend:** HTML, JavaScript

---

## How to Run

1. Clone the repository
```bash
git clone https://github.com/ForeignDream/security-dashboard.git
cd security-dashboard
```

2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Populate the database with sample data
```bash
python3 seed.py
```

5. Run the application
```bash
python3 IncidentsDashboard.py
```

6. Open your browser and go to `http://127.0.0.1:5000`

---

## Project Structure

```
security-dashboard/
├── IncidentsDashboard.py   # Main Flask application
├── seed.py                 # Script to populate the database
├── requirements.txt        # Project dependencies
├── templates/
│   └── index.html          # Dashboard frontend
└── .gitignore
```

---

## Notes

- This is a beginner project built for learning purposes
- Incident data is simulated and does not represent real events
- The database is recreated every time `seed.py` is executed

---

## Author

**Jhonathan da Silva de Sá**  
Information Security Technologist  
[LinkedIn](https://www.linkedin.com/in/jhonathan-sa/) · [GitHub](https://github.com/ForeignDream)
