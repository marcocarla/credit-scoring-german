# Conclusions and Business Recommendations

This document summarizes the results, insights, and strategic recommendations derived from the credit scoring project based on the German Credit dataset.

---

## Project Summary

We developed a binary classification model to predict the probability of default for individual credit applicants. The objective was not only to optimize predictive performance, but also to ensure **probability calibration** and **interpretability**—two critical aspects in real-world financial decision-making.

---

## Model Performance

After testing several models, the **Logistic Regression** classifier achieved the best trade-off between interpretability and predictive power.

| Model                 | AUC-ROC | Brier Score |
|----------------------|---------|-------------|
| Logistic Regression  | 0.804   | 0.155       |
| Calibrated Logistic  | 0.805   | 0.156       |
| Random Forest        | 0.779   | 0.167       |

- **AUC-ROC** indicates how well the model separates good and bad credit risks.
- **Brier Score** measures how well the predicted probabilities are calibrated.

---

## Key Insights from SHAP

- **Credit amount** and **loan duration** are the strongest predictors of default.
- Specific account statuses (`A14`, `A11`) and savings patterns also correlate with risk.
- SHAP summary and dependence plots confirmed the influence of these variables, and provided local interpretability at the individual prediction level.

---

## Business Implications

1. **Risk Monitoring**  
   The model enables early identification of high-risk customers based on application data. This supports more informed credit decisions and risk-based pricing strategies.

2. **Actionable Interventions**  
   By quantifying individual risk with interpretable outputs, the model supports tailored actions like offering guarantees, adjusting loan terms, or requiring co-signers.

3. **Regulatory Compliance**  
   The use of calibrated probabilities and SHAP-based explanations enhances model transparency, making it more suitable for use in regulated environments (e.g., Basel III, GDPR).

---

## Limitations

- The dataset is **synthetic and limited** to 1,000 observations.
- Many categorical variables are encoded as opaque codes (`A11`, `A14`, etc.), which could reduce interpretability if not properly mapped.
- No analysis of **feature correlations**, **multicollinearity**, or **fairness across groups** was conducted in this version.

---

## Future Work

- **Extend to larger and real-world datasets** (e.g., Lending Club, FICO).
- **Test advanced models** like XGBoost with proper calibration.
- **Add fairness and bias analysis** to assess disparate impact.
- Build a simple **dashboard or API** for end-user access and decision support.

---

## Final Takeaway

This project demonstrates how a junior data scientist can develop a full-cycle credit scoring model with well-structured code, thoughtful evaluation, and a strong emphasis on transparency. The result is a deployable and explainable risk model—key for any data-driven financial institution.

[See full conclusions and business recommendations](./reports/conclusions_and_recommendations.md)

