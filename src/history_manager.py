import json
import os

INSIGHTS_FILE = "history/insights.json"

def save_insight(insight_entry):
    """Save an insight to the insights history file."""
    if not os.path.exists(INSIGHTS_FILE):
        with open(INSIGHTS_FILE, 'w') as f:
            json.dump([], f)

    with open(INSIGHTS_FILE, 'r+') as f:
        insights = json.load(f)
        insights.append(insight_entry)
        f.seek(0)
        json.dump(insights, f, indent=4)

    print("Insight saved to history.")

def load_insights():
    """Load all insights from the insights history file."""
    if os.path.exists(INSIGHTS_FILE):
        with open(INSIGHTS_FILE, 'r') as f:
            return json.load(f)
    else:
        print("No insights history found.")
        return []
