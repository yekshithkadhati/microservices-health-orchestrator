## Microservices Health Orchestrator

A Python-based intelligent system that monitors microservices health and automatically performs healing actions like restarts, scaling, or rerouting using machine learning.

## Problem Statement

Design a container and microservices **Health Orchestrator** that:
- Monitors service metrics (CPU, memory, response time)
- Predicts failures using AI/ML
- Applies automated healing (restart, scale, reroute)
- Maintains modularity with clear architecture

## Skills Demonstrated

- **AI/ML**: Logistic Regression-based failure prediction
- **Automation**: Automated healing with scaling/restarts
- **Critical Thinking**: Handles cascading failures and dependenci

## Project Structure

```plaintext
microservices-health-orchestrator/
├── __pycache__/              # Python bytecode cache
├── config/                   # Configuration files (e.g., services.json)
├── healer/                   # Healing logic and action definitions
├── monitor/                  # Service monitoring logic
├── orchestrator/             # Orchestration logic to coordinate all modules
├── predictor/                # ML-based failure prediction models
├── health.py                 # Main script connecting all modules
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
