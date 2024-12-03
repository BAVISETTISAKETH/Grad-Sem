# src/history_manager.py
import json
import os
from src.config import INSIGHTS_FILE

def save_insight(insight_entry):
    """Save an insight to the insights file."""
    os.makedirs(os.path.dirname(INSIGHTS_FILE), exist_ok=True)
    try:
        with open(INSIGHTS_FILE, "r") as f:
            insights = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        insights = []

    insights.append(insight_entry)

    with open(INSIGHTS_FILE, "w") as f:
        json.dump(insights, f, indent=4)
    print("Insight saved.")

def load_insights():
    """Load historical insights."""
    try:
        with open(INSIGHTS_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
