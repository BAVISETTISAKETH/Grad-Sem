import pandas as pd
from src.data_processing import load_dataset
from src.llm_handler import clean_dataset_with_llm, get_visualization_recommendations, generate_visualization_and_insights
from src.history_manager import save_insight

def main():
    # Step 1: Upload a CSV dataset
    file_path = input("Upload a CSV dataset. Enter the full path of your dataset: ").strip()
    data = load_dataset(file_path)
    if data is None:
        print("Failed to load the dataset. Exiting...")
        return

    # Step 2: Use the LLM to clean the dataset
    print("\nAnalyzing dataset for cleaning...")
    cleaning_steps = clean_dataset_with_llm(data)
    print("\nRecommended Data Cleaning Steps:")
    for idx, step in enumerate(cleaning_steps, 1):
        print(f"{idx}. {step}")

    # Step 3: Generate visualization recommendations
    print("\nGenerating visualization recommendations...")
    recommendations = get_visualization_recommendations(data)

    print("\nBased on the uploaded dataset, here are the recommended visualizations:")
    for idx, rec in enumerate(recommendations, 1):
        print(f"{idx}. {rec}")

    # Step 4: User selects a visualization
    choice = int(input("\nPlease choose the visualization you want to perform (enter the number): ").strip())
    if choice < 1 or choice > len(recommendations):
        print("Invalid choice. Exiting...")
        return

    # Step 5: Generate the visualization and insights
    selected_rec = recommendations[choice - 1]
    print(f"\nGenerating visualization: {selected_rec}...")
    visual_path, insight = generate_visualization_and_insights(data, selected_rec)

    if visual_path:
        # Save insight
        save_insight({"visualization": selected_rec, "path": visual_path, "insight": insight})
        print(f"\nVisualization saved at {visual_path}.")
        print(f"Generated Insight:\n{insight}")
    else:
        print("Visualization generation failed.")

if __name__ == "__main__":
    main()
