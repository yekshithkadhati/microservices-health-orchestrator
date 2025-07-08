import joblib
import os
model_path = os.path.join(os.path.dirname(__file__), "failure_model.pkl")
model = joblib.load(model_path)
def predict_failure(cpu_usage, memory_usage, response_time):
    input_data = [[cpu_usage, memory_usage, response_time]]
    prediction = model.predict(input_data)[0]
    return bool(prediction)
if __name__ == "__main__":
    test = predict_failure(cpu_usage=91, memory_usage=50, response_time=300)
    print("Predicted Failure:" if test else "Service is Healthy")
