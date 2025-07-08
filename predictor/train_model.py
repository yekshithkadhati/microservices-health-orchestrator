import random
import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
def generate_data(n=500):
    data = []
    for _ in range(n):
        cpu = random.uniform(0, 100)
        memory = random.uniform(0, 100)
        response = random.uniform(0, 1000)
        failure = int(cpu > 85 or memory > 90 or response > 900)
        data.append([cpu, memory, response, failure])
    return pd.DataFrame(data, columns=["cpu_usage", "memory_usage", "response_time", "failure"])
df = generate_data()
X = df[["cpu_usage", "memory_usage", "response_time"]]
y = df["failure"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LogisticRegression()
model.fit(X_train, y_train)
joblib.dump(model, "predictor/failure_model.pkl")
print("Model trained and saved as predictor/failure_model.pkl")
