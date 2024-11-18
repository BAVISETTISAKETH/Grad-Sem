import openai
import json
from datetime import datetime

openai.api_key = "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"

def generate_insight_from_visualization(visual_path, description):
    """Generate insight based on the visualization using an LLM."""
   
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Generate insights for the visualization: {description}.",
        max_tokens=50
    )
    insight_text = response.choices[0].text.strip()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    insight_entry = {
        "visualization_path": visual_path,
        "description": description,
        "insight": insight_text,
        "timestamp": timestamp
    }
    
    print(f"Generated insight: {insight_text}")
    return insight_entry
