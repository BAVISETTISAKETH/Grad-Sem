from transformers import pipeline

# Initialize Hugging Face model
generator = pipeline("text-generation", model="bigscience/bloom-560m")

def analyze_columns(data):
    """Analyze each column in the dataset and summarize its content."""
    analysis = []
    for col in data.columns:
        dtype = data[col].dtype
        unique_values = data[col].nunique()
        analysis.append(f"Column: {col} | Type: {dtype} | Unique Values: {unique_values}")
    return "\n".join(analysis)

def recommend_visualizations(data):
    """Recommend visualizations based on column analysis."""
    numerical_cols = [col for col in data.columns if pd.api.types.is_numeric_dtype(data[col])]
    categorical_cols = [col for col in data.columns if pd.api.types.is_string_dtype(data[col])]

    recommendations = []
    if numerical_cols and categorical_cols:
        recommendations.append({
            "title": "Bar Chart: Numerical vs Categorical",
            "columns": [numerical_cols[0], categorical_cols[0]],
        })
        recommendations.append({
            "title": "Scatter Plot: Numerical vs Numerical",
            "columns": numerical_cols[:2],
        })
    if len(numerical_cols) > 1:
        recommendations.append({
            "title": "Line Chart: Time Series",
            "columns": numerical_cols[:2],
        })

    return recommendations
