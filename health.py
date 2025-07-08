from monitor.monitor import get_service_metrics
from predictor.predictor import predict_failure
from healer.healer import decide_healing_action
from orchestrator.orchestrator import execute_action
def run_health_orchestration(service_name):
    metrics = get_service_metrics(service_name)
    print(f"Collected Metrics: {metrics}")

    if predict_failure(**metrics):
        print("Failure predicted.")
        action = decide_healing_action(service_name, metrics)
        execute_action(service_name, action)
    else:
        print("Service is healthy. No action needed.")
if __name__ == "__main__":
    run_health_orchestration("auth-service")

