# Credit Scoring with Real-World Data

This project builds and evaluates a credit scoring model using the German Credit dataset. The goal is to predict the probability of default for individual applicants and provide explainable, calibrated risk scores—useful for decision-making in financial institutions.

---

## Project Goals

- Build a **binary classification model** to assess credit risk.
- Ensure **probability calibration** (reliable risk scores).
- Apply **explainable AI (SHAP)** to understand model decisions.
- Present a clean and reproducible **portfolio-quality project**.

---

## Dataset

- **Source**: UCI Machine Learning Repository  
  [German Credit Data](https://archive.ics.uci.edu/ml/datasets/statlog+(german+credit+data))
- **Rows**: 1,000 loan applicants  
- **Features**: Demographics, credit amount, duration, employment, etc.
- **Target**: Credit risk (0 = good, 1 = bad)

---

## Modeling Workflow

| Step | Description |
|------|-------------|
| `01_data_loading.py` | Downloads and prepares raw dataset |
| `02_eda.ipynb` | Exploratory data analysis: distributions, patterns, target relationships |
| `03_preprocessing.ipynb` | One-hot encoding, scaling, train-test split |
| `04_modeling_and_calibration.ipynb` | Logistic regression, Random Forest, calibration, AUC and Brier |
| `05_explainability_shap.ipynb` | SHAP values, global and local interpretability |
| [`reports/conclusions_and_recommendations.md`](./reports/conclusions_and_recommendations.md) | Business summary and next steps |

---

## Key Results

| Model                 | AUC-ROC | Brier Score |
|----------------------|---------|-------------|
| Logistic Regression  | 0.804   | 0.155       |
| Calibrated Logistic  | 0.805   | 0.156       |
| Random Forest        | 0.779   | 0.167       |

- **Top predictive features**: `Credit_amount`, `Duration_month`, checking account status
- **SHAP summary plots** used to explain risk drivers globally and per instance

---

## Project Structure

```bash
credit-scoring-german/
│
├── data/ # Raw and cleaned datasets
├── notebooks/ # Jupyter Notebooks (EDA, modeling, SHAP)
├── src/ # Scripts (data loading)
├── models/ # Saved models and preprocessed objects
├── reports/ # Final conclusions and business recommendations
├── requirements.txt # Python dependencies
└── README.md # Project overview (this file)
```


---

## Skills Demonstrated

- Classification, calibration, and evaluation with AUC and Brier Score
- SHAP explainability: global + local analysis
- Reproducible ML pipeline using `sklearn` and `joblib`
- Business thinking applied to risk modeling
- Clean notebook documentation for portfolio use

---

## Future Extensions

- Add real-world dataset
- Experiment with gradient boosting models (XGBoost, LightGBM)
- Build a dashboard or API for risk reporting

---

## Author

Carla Marcó Aparicio  
Mathematics graduate

📫 [LinkedIn](https://www.linkedin.com/in/marcocarla) · 📁 [Other Projects](https://github.com/marcocarla)

