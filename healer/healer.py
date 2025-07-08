def decide_healing_action(service_name, metrics):
    cpu = metrics["cpu_usage"]
    mem = metrics["memory_usage"]
    latency = metrics["response_time"]
    if cpu > 90:
        return "scale_up"
    elif mem > 90:
        return "restart"
    elif latency > 800:
        return "reroute_traffic"
    else:
        return "no_action"
if __name__ == "__main__":
    mock_metrics = {"cpu_usage": 95, "memory_usage": 60, "response_time": 500}
    action = decide_healing_action("auth-service", mock_metrics)
    print(f"Healing Action: {action}")
