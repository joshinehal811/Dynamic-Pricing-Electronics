# Retail Dynamic Pricing Prediction System

**Goal**: Predict future sales per SKU per store and optimize dynamic pricing based on inventory, competitor prices, and events.

---

## Project Structure

| Folder | Purpose |
|:---|:---|
| data_ingestion/ | Scripts to load raw data into Bronze Delta tables |
| feature_engineering/ | Scripts to create modeling-ready Silver features |
| modeling/ | Sales forecasting and price elasticity models |
| training/ | Training pipelines for ML models |
| inference/ | Batch and real-time inference scripts |
| deployment/ | FastAPI app to serve ML models |
| drift_monitoring/ | Scripts for monitoring model drift |
| notebooks/ | Exploration and analysis notebooks |
| tests/ | Unit and integration tests |
| mlflow_experiments/ | MLflow experiment tracking |
| .github/workflows/ | CI/CD pipelines (testing, linting, deployment) |

---

## Dataset
- [Kaggle Electronics Store Events Dataset](https://www.kaggle.com/datasets/mkechinov/ecommerce-events-history-in-electronics-store)

---

## Key Technologies
- Databricks (Delta Live Tables, MLflow)
- LightGBM, XGBoost
- FastAPI
- MLflow for Experiment Tracking
- Docker (for API deployment)
- GitHub Actions (for CI/CD)
- Drift Monitoring

---

## Setup
1. Clone the repository
2. Upload Kaggle dataset to DBFS `/FileStore/ecommerce_data/`
3. Install dependencies with `pip install -r requirements.txt`
4. Run ingestion, feature engineering, training notebooks
5. Start API server with `uvicorn deployment.api_server:app --reload`

---

## Authors
- Nehal Joshi 
