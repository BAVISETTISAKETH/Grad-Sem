# Load datasets
file_paths = [r"C:\Users\jkaus\Downloads\Grad-Sem-main\Grad-Sem-main\Data\AmazonSaleReport.csv", r"C:\Users\jkaus\Downloads\Grad-Sem-main\Grad-Sem-main\Data\InternationalsaleReport.csv"]
datasets = load_and_link_datasets(file_paths)

# Create visualizations
create_and_save_visualizations(datasets)

# Manage insights
insight_manager = InsightsManager()
insight_manager.store_insight("sales", "bar_chart", "Revenue has a seasonal trend.")

# Generate insights using LLMs
api_key = "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"
orchestrator = LLMOrchestrator(api_key)
orchestrator.generate_and_store_insights(datasets, insight_manager)

# Retrieve historical insights
print(insight_manager.retrieve_insights())
