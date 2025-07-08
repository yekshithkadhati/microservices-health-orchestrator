def predict_failure(cpu_usage, memory_usage, response_time):
    if cpu_usage > 85 or memory_usage > 90 or response_time > 900:
        return True
    return False

if __name__ == "__main__":
    test = predict_failure(cpu_usage=91, memory_usage=50, response_time=300)
    print("Predicted Failure:" if test else "Service is Healthy")
