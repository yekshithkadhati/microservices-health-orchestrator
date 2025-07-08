def decide_healing_action(metrics):
    if metrics["cpu_usage"] > 90:
        return "restart_service"
    elif metrics["memory_usage"] > 85:
        return "scale_up"
    elif metrics["response_time"] > 800:
        return "reroute_traffic"
    else:
        return "no_action"
