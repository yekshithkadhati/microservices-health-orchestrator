def execute_action(service_name, action):
    print(f"Executing '{action}' for service: {service_name}")
    if action == "restart":
        print(f"Restarting {service_name}...")
    elif action == "scale_up":
        print(f"Scaling up {service_name}...")
    elif action == "reroute_traffic":
        print(f"Rerouting traffic away from {service_name}...")
    else:
        print("No action required.")
if __name__ == "__main__":
    execute_action("auth-service", "scale_up")
