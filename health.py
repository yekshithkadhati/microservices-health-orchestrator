import json
from monitor.monitor import get_service_metrics
from predictor.predictor import predict_failure
from healer.healer import decide_healing_action
from orchestrator.orchestrator import execute_action
def load_services():
    with open("config/services.json") as f:
        data = json.load(f)
    return data["services"]
if __name__ == "__main__":
    services = load_services()
    for service_name in services:
        print(f"\n Checking: {service_name}")
        metrics = get_service_metrics(service_name)
        print(f" Collected Metrics: {metrics}")
        failure = predict_failure(
            cpu_usage=metrics["cpu_usage"],
            memory_usage=metrics["memory_usage"],
            response_time=metrics["response_time"]
        )
        if failure:
            print("Failure predicted.")
            action = decide_healing_action(metrics)
            print(f"Executing '{action}' for service: {service_name}")
            execute_action(service_name, action)
        else:
            print("Service is healthy. No action needed.")


