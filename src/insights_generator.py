# src/insights_generator.py
import openai
import json
from datetime import datetime
from config import OPENAI_API_KEY

# Configure OpenAI API key
openai.api_key = OPENAI_API_KEY

def generate_insight_from_visualization(visual_path, description):
    """Generate insight based on the visualization using an LLM."""
    # Placeholder LLM interaction
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Generate insights for the visualization: {description}.",
        max_tokens=50
    )
    insight_text = response.choices[0].text.strip()

    # Log the insight
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    insight_entry = {
        "visualization_path": visual_path,
        "description": description,
        "insight": insight_text,
        "timestamp": timestamp
    }
    
    print(f"Generated insight: {insight_text}")
    return insight_entry
