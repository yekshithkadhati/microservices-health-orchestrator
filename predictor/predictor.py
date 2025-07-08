import joblib
import pandas as pd
model = joblib.load("predictor/failure_model.pkl")
def predict_failure(cpu_usage, memory_usage, response_time):
    input_data = pd.DataFrame([{
        "cpu_usage": cpu_usage,
        "memory_usage": memory_usage,
        "response_time": response_time
    }])
    
    prediction = model.predict(input_data)[0]
    return bool(prediction)
if __name__ == "__main__":
    result = predict_failure(cpu_usage=95, memory_usage=70, response_time=500)
    print("Failure Predicted." if result else "Service is Healthy.")
