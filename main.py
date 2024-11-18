from src.data_processing import load_dataset
from src.visualization import create_visualization
from src.insights_generator import generate_insight_from_visualization
from src.history_manager import save_insight, load_insights
import pandas as pd
from transformers import AutoModelForCausalLM, AutoTokenizer

def analyze_dataset_with_llm(data):
    """Use Llama model to analyze the dataset and recommend visualizations."""
    # Load the Llama model and tokenizer (replace <path-to-model> with the actual path)
    model_path = r"C:\Users\jkaus\AppData\Roaming\Python\Python312\Scripts\.cache\huggingface\download\original"
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path)

    # Generate a prompt to describe the dataset's structure
    column_names = ", ".join(data.columns)
    prompt = (
        f"The uploaded dataset has the following columns: {column_names}.\n"
        "Analyze the dataset and suggest suitable visualization types (e.g., bar charts, line plots, scatter plots, heatmaps) "
        "based on its structure and content. Provide suggestions in a list format with a brief explanation for each."
    )

    # Tokenize the input
    inputs = tokenizer(prompt, return_tensors="pt")

    # Generate a response
    outputs = model.generate(**inputs, max_length=200, do_sample=True)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return response.strip()


def generate_visualizations_and_insights(data, selected_visualizations):
    """Generate visualizations and insights based on user's selection."""
    for viz in selected_visualizations:
        try:
            # Parse the visualization type and relevant columns from the user's choice
            viz_type = viz["type"]
            columns = viz["columns"]
            title = viz["title"]

            if viz_type == "line":
                visual_path = create_visualization(data, columns[0], columns[1], title)
            elif viz_type == "bar":
                visual_path = create_visualization(data, columns[0], columns[1], title)
            elif viz_type == "scatter":
                visual_path = create_visualization(data, columns[0], columns[1], title)
            elif viz_type == "heatmap":
                # Placeholder for heatmap visualization logic
                visual_path = "Generated Heatmap"

            # Generate insights for the visualization
            description = title
            insight_entry = generate_insight_from_visualization(visual_path, description)

            # Save the insight to history
            if insight_entry:
                save_insight(insight_entry)
                print(f"Insight for '{title}' saved successfully!")

        except Exception as e:
            print(f"Error generating visualization or insights for '{title}': {e}")

def main():
    # Step 1: Load the dataset (simulate user uploading)
    file_path = r"C:\Users\jkaus\Downloads\Grad-Sem-main\Grad-Sem-main\Data\AmazonSaleReport.csv"
    data = load_dataset(file_path)

    if data is None:
        print("Dataset could not be loaded. Exiting...")
        return

    # Step 2: Clean column names
    data.columns = data.columns.str.strip()

    # Step 3: Identify potential date columns and convert them to datetime
    for col in data.columns:
        if "date" in col.lower():  # Use heuristic to find date columns
            try:
                data[col] = pd.to_datetime(data[col], errors="coerce")
            except Exception:
                print(f"Could not convert column '{col}' to datetime.")

    # Step 4: Analyze the dataset with Llama to recommend visualizations
    print("\nAnalyzing dataset...")
    try:
        visualization_recommendations = analyze_dataset_with_llm(data)
        print("\nVisualization Recommendations:")
        print(visualization_recommendations)
    except Exception as e:
        print(f"Error generating visualization recommendations: {e}")
        return

    # Step 5: Simulate user selection of visualizations
    # In a real application, this would involve user interaction.
    # For now, we'll hardcode a sample selection based on expected input.
    selected_visualizations = [
        {"type": "line", "columns": ["Date", "Amount"], "title": "Sales Over Time"},
        {"type": "bar", "columns": ["Category", "Amount"], "title": "Sales by Category"}
    ]

    # Step 6: Generate the selected visualizations and insights
    generate_visualizations_and_insights(data, selected_visualizations)

    # Step 7: Retrieve and display historical insights
    print("\nHistorical Insights:")
    historical_insights = load_insights()
    for idx, insight in enumerate(historical_insights, 1):
        print(f"{idx}. {insight}")

if __name__ == "__main__":
    main()
