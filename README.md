# DAY BY DAY: 100 Days of Python Tracker

**Build a habit. Build something great.**

A personal study tracker built with Django to keep me accountable through 100 Days of Python. One click to clock in when I start studying, one click to clock out when I stop, and the app handles the rest: session history, durations, total hours, and a day counter that moves forward every day.

<img width="970" height="1025" alt="Screenshot 2026-10-05 023325" src="https://github.com/user-attachments/assets/a348b45a-5245-48f8-b552-e6d038e3a5b3" />


---

## Features

- **Clock in / clock out:** one click to start a study session, one click to end it. Buttons switch on and off automatically based on whether a session is running.
- **Multiple sessions per day:** study in the morning, again at night; every session is logged separately.
- **Study history:** a table of every session with its date, clock-in time, clock-out time, and duration (e.g. `1h 05m`).
- **Automatic day counter:** counts from Day 1 to Day 100 by the calendar, whether or not I studied that day.
- **Progress bar:** fills up as the 100 days pass.
- **Total study time:** all sessions added up and shown in hours.
- **Private access:** every page and action is restricted to staff users, so only I can use it.

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.14, Django 6.1 |
| Database | SQLite |
| Frontend | Django templates, HTML, CSS |
| Version control | Git, GitHub |

## How It Works

A few design decisions behind the app:

- **Store facts, calculate the rest.** The database only stores what actually happened: each session's clock-in and clock-out time. Duration, total hours, day number, and progress are all calculated when the page loads, so they can never get out of sync with the real data.
- **Every saved session is complete.** When I clock in, the start time is held in the user's Django session. A database row is created only at clock-out, with both times at once, so there are never half-finished records.
- **Time zones handled properly.** Times are stored in UTC and displayed in local time, so a session at 5 PM shows as 5 PM, not 9 PM.
- **POST-only actions.** Clock in and clock out only run on form submissions with CSRF protection, never on a simple page visit.

## Getting Started

### Prerequisites

- Python 3.12+
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/Simohjc/100days_tracker.git
cd 100days_tracker

# Create and activate a virtual environment
python -m venv cta_env
# Windows:
cta_env\Scripts\activate
# macOS / Linux:
source cta_env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up the database
python manage.py migrate

# Create your account (needed to log in)
python manage.py createsuperuser

# Run the app
python manage.py runserver
```

Then open **http://127.0.0.1:8000/** and log in with the account you created.

### Configuration

- **Start date:** set `COURSE_START` in `course_100days/views.py` to the day your challenge begins.
- **Length:** change `TOTAL_DAYS` to run a different challenge, like 30 or 60 days.
- **Time zone:** set `TIME_ZONE` in `course_tracking_main/settings.py` to your local zone (e.g. `America/New_York`).

## Project Structure

```
100days_tracker/
├── course_100days/          # The tracker app: model, views, URLs, static files
├── course_tracking_main/    # Project settings and main URL configuration
├── templates/               # HTML templates
├── manage.py
└── requirements.txt
```

## Roadmap

- [ ] Streak counter: consecutive days with at least one session
- [ ] Rows showing 0 for days without a study session
- [ ] Deploy online so it works from any device, including my phone
- [ ] Move the secret key to an environment variable before deployment

## Author

**Mohamed El Khair**
Software developer learning in public: Python, Django, SQL.

- Portfolio: [simohjc.github.io/Portfolio-dataAna](https://simohjc.github.io/Portfolio-dataAna/)
- GitHub: [@Simohjc](https://github.com/Simohjc)

---

*100 days. One day at a time.*
