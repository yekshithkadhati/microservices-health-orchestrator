Monitors microservices and applies intelligent healing actions like restart, scale-up, or reroute based on health metrics.
- **monitor/** – Collects metrics (simulated)
- **predictor/** – Predicts service failure (basic logic)
- **healer/** – Decides healing action
- **orchestrator/** – Executes the healing action
- **health.py** – Main entry point to run full orchestration
```bash
python health.py
