# Customer Churn Prediction

Predict customer churn on a synthetic dataset using Python. The pipeline includes data generation, feature engineering, model training (Logistic Regression, Random Forest, Gradient Boosting), hyperparameter search, class weighting, selection by PR-AUC, and decision-threshold tuning to balance precision and recall. Outputs metrics, reports, and visualizations.

---

## Features
- Synthetic customer dataset with realistic behavior signals
- Models: Logistic Regression, Random Forest, Gradient Boosting
- Hyperparameter optimization (RandomizedSearchCV) & class weighting
- Model selection by PR-AUC (Average Precision)
- Threshold tuning (F2 focus) with precision floor
- Metrics: Accuracy, Precision, Recall, F1, ROC-AUC, PR-AUC
- Visuals: ROC, Precision-Recall, Confusion Matrix, Feature Importance
- Saved artifacts: best model (`joblib`) & metrics

---

## Project Structure
```
customer-churn-prediction/
├─ README.md
├─ LICENSE
├─ requirements.txt
├─ data/
│  └─ generate_customers.py
├─ src/
│  ├─ train_models.py
│  └─ utils.py
└─ outputs/
   └─ figures & reports
```

---

## Setup
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
```

---

## Generate Synthetic Data
```bash
python data/generate_customers.py --n 10000 --seed 42 --out data/customers.csv
```

---

## Train & Evaluate
```bash
python src/train_models.py --input data/customers.csv --outdir outputs --test-size 0.2 --val-size 0.2 --seed 42
```

**Outputs**
- `outputs/metrics.json` – model choice, tuned threshold, test metrics
- `outputs/classification_report.txt`
- `outputs/roc_curve.png`
- `outputs/pr_curve.png`
- `outputs/confusion_matrix.png`
- `outputs/feature_importance.png`
- `outputs/best_model.joblib`

---

## Final Results (Logistic Regression)

### Key Metrics
| Metric        | Value |
|---------------|-------|
| Accuracy      | **83.8%** |
| ROC-AUC       | **0.823** |
| PR-AUC (AP)   | **0.562** |
| Recall (Churn)| **0.50** |
| Precision (Churn) | **0.52** |

➡️ The model now catches ~50% of churners with precision ~0.52, balancing false positives and recall.

---

### Confusion Matrix
<img width="1120" height="1120" alt="confusion_matrix" src="https://github.com/user-attachments/assets/f9d57d15-ea26-4c95-90a7-5d5d8f9db584" />

### ROC Curve
<img width="1280" height="960" alt="roc_curve" src="https://github.com/user-attachments/assets/8af72b6f-d62e-4f5d-b9d3-e5b502a35f3b" />

### Precision-Recall Curve
<img width="1280" height="960" alt="pr_curve" src="https://github.com/user-attachments/assets/24b4145e-2a46-45e6-8ecb-499cb5a2c808" />

### Feature Importance
<img width="1600" height="960" alt="feature_importance" src="https://github.com/user-attachments/assets/d14697b0-af85-40eb-a9d0-01078996f0d8" />

---

## Data Schema
| column                    | description                          |
|---------------------------|--------------------------------------|
| customer_id               | unique customer ID                   |
| age                       | customer age                         |
| region                    | {North, South, East, West}           |
| tenure_months             | months since signup                  |
| is_premium                | premium plan (0/1)                   |
| monthly_spend             | average monthly spend                |
| avg_txn_value             | average transaction value            |
| txns_last_30d             | transactions in last 30 days         |
| days_since_last_purchase  | recency (days)                       |
| customer_service_calls    | support calls in last 90 days        |
| discounts_used_90d        | discounts used in last 90 days       |
| complaints_90d            | complaint count                      |
| churn                     | target label (0/1)                   |
