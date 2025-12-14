from regression_model.predict import make_prediction
from .api.validation import DataInput

def predict(input_data):
    # Validate input using Pydantic
    validated = DataInput(data=input_data)

    # Run prediction using the regression_model package
    result = make_prediction(input_data=validated.data)

    # Convert numpy arrays to Python lists for JSON serialization
    if "predictions" in result:
        result["predictions"] = result["predictions"].tolist()

    return result