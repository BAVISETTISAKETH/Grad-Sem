# src/insights_generator.py
from src.llm_handler import generate_response

def generate_insight_from_visualization(visual_path, title):
    """Generate insight based on visualization."""
    prompt = (
        f"Given the visualization titled '{title}' saved at {visual_path}, "
        "provide meaningful insights about the data trends and patterns."
    )
    try:
        response = generate_response(prompt)
        if response is None:
            raise ValueError("Model returned no response.")
        return {
            "insight": response.strip(),
            "visualization_path": visual_path,
        }
    except Exception as e:
        print(f"Failed to generate insight: {e}")
        return {
            "insight": "No insight available due to an error.",
            "visualization_path": visual_path,
        }
