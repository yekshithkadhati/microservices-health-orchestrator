import random
def get_service_metrics(service_name):
    return {
        "cpu_usage": random.uniform(0, 100),
        "memory_usage": random.uniform(0, 100),
        "response_time": random.uniform(10, 1000)
    }

if __name__ == "__main__":
    service = "auth-service"
    metrics = get_service_metrics(service)
    print(f"Metrics for {service}: {metrics}")
