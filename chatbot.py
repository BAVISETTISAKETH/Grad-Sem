import pandas as pd
import gradio as gr
from src.llm_handler import analyze_columns, recommend_visualizations
from src.visualization import create_visualization
from src.history_manager import save_insight

# Global variable to store the dataset
dataset = None

def upload_dataset(file):
    global dataset
    if file is None:
        return "No file uploaded."
    try:
        # Load dataset with low_memory=False to avoid dtype inference issues
        dataset = pd.read_csv(file.name, low_memory=False)
        column_analysis = analyze_columns(dataset)
        return f"Dataset '{file.name}' loaded successfully!\n\n{column_analysis}"
    except pd.errors.DtypeWarning as dw:
        return f"Warning: Mixed data types detected in one or more columns. {dw}"
    except Exception as e:
        return f"Error loading file: {e}"


def generate_visualizations(selected_visualization):
    global dataset
    if dataset is None:
        return "Please upload a dataset first."
    try:
        # Recommend visualizations based on the dataset
        visualization_recommendations = recommend_visualizations(dataset)
        if selected_visualization < 1 or selected_visualization > len(visualization_recommendations):
            return "Invalid selection. Please select a valid visualization."
        
        # Generate the selected visualization
        recommendation = visualization_recommendations[selected_visualization - 1]
        visual_path = create_visualization(dataset, recommendation["columns"], recommendation["title"])
        
        # Save the generated visualization
        save_insight({
            "visualization": recommendation["title"],
            "path": visual_path,
            "insight": f"Generated visualization for {recommendation['columns']}."
        })
        return f"Visualization '{recommendation['title']}' saved at {visual_path}."
    except Exception as e:
        return f"Error generating visualization: {e}"

# Gradio UI
def gradio_interface():
    with gr.Blocks() as interface:
        gr.Markdown("### Dataset Visualization Chatbot")

        with gr.Row():
            upload_btn = gr.File(label="Upload CSV Dataset")
            upload_status = gr.Textbox(label="Upload Status", interactive=False)
        
        with gr.Row():
            visualization_dropdown = gr.Dropdown(choices=[], label="Choose Visualization")
            generate_btn = gr.Button("Generate Visualization")
            result = gr.Textbox(label="Result", interactive=False)
        
        # Logic for Upload Button
        upload_btn.change(
            fn=upload_dataset,
            inputs=[upload_btn],
            outputs=[upload_status],
        )

        # Logic for Generate Button
        generate_btn.click(
            fn=generate_visualizations,
            inputs=[visualization_dropdown],
            outputs=[result],
        )
    
    return interface

# Run Gradio app
if __name__ == "__main__":
    gradio_interface().launch(share=True)
