# CUSTOMER-CHURN-PREDICTION-AND-RETENTION-INTELLIGENCE-SYSTEM
The **Customer Churn Prediction & Retention Intelligence System** is an AI-powered analytics application designed to identify customers who are likely to churn and provide actionable retention insights.
Instead of reacting after customers leave, this system proactively analyzes customer behavior, engagement, and transaction patterns to predict churn risk in advance and recommend suitable retention strategies.

This project is highly valuable for business analysts, data scientists, CRM teams, SaaS companies, and students working on real-world machine learning applications.
## Overview

The system is built using a trained machine learning classification model stored as a .pkl file and deployed through an interactive Streamlit dashboard.
It supports both:
- Single-customer churn prediction, and
- Bulk customer churn analysis using uploaded CSV datasets.

The application not only predicts churn probability but also segments customers by risk level and suggests retention actions, making it a complete churn intelligence solution rather than just a prediction model.
## Tools and Technologies Used

- **Python:** Core development language
  
- **Streamlit:** Interactive dashboard and UI
  
- **Scikit-learn:** Model training and inference

- **Joblib:** Model serialization and loading

- **Pandas:** Data preprocessing and feature handling

- **NumPy:** Numerical computations

- **Matplotlib:** Visual analytics (risk distribution charts)

## Why These Tools Were Selected

- Machine learning models effectively capture churn behavior patterns
- Streamlit enables rapid deployment without backend complexity
- Pandas and NumPy simplify customer data preprocessing
- Matplotlib provides clean visual insights for business users
- Joblib ensures fast and efficient model loading

Together, these tools enable a business-ready AI solution that balances predictive accuracy with interpretability.
## Features

- Single customer churn prediction
- Churn probability scoring
- Risk segmentation (Low / Medium / High)
- Retention strategy recommendations
- Bulk CSV churn prediction
- Interactive churn dashboard
- Risk distribution pie chart
- Downloadable churn prediction report
- Clean and professional UI
## How It Works

🔹 Single Customer Prediction

- User inputs customer details such as:

  - Age, gender, tenure
  - Usage frequency
  - Support calls
  - Payment delays
- Subscription type and contract length
- Model predicts:

  - Churn likelihood (Yes / No)
  - Churn probability (%)
  - Customer risk level
- System recommends an appropriate retention strategy

🔹 Bulk Prediction & Dashboard

- User uploads a customer dataset (CSV)
- Model generates churn predictions for all customers
- Customers are segmented into:

  - Low Risk
  - Medium Risk
  - High Risk
- Dashboard displays:

  - Total customers
  - Predicted churners
  - Overall churn rate
  - Risk distribution chart

- Results can be downloaded as a CSV report
## Advantages

- Proactive customer retention
- Data-driven decision support
- Scales easily for large customer datasets
- Business-friendly visual insights
- Reduces customer acquisition costs
- Supports CRM and marketing strategies
- Ideal for real-world ML demonstrations
## Limitations

- Model performance depends on training data quality
- May not generalize well to unseen customer segments
- Requires feature consistency between training and input data
- Predictions should support—not replace—business judgment
- Not suitable for fully automated decision-making without validation
## Real-Time Applications

- SaaS platforms: Reduce subscription churn
- Telecom industry: Identify high-risk users
- E-commerce: Improve customer lifetime value
- Banking & finance: Predict account attrition
- CRM analytics: Customer segmentation & retention
- Academic projects: Applied machine learning systems
## Future Enhancements

- Integration with CRM systems
- Time-series churn prediction
- Customer Lifetime Value (CLV) modeling
- Explainable AI (SHAP feature importance)
- Personalized retention offers
- Email/SMS alert system
- Cloud deployment (AWS / Azure)
- Automated retraining pipeline
## Conclusion

The Customer Churn Prediction & Retention Intelligence System showcases how machine learning can be effectively applied to solve real business problems.
By combining predictive analytics with an intuitive dashboard and retention intelligence, this system empowers organizations to retain customers proactively and strategically.
With further enhancements, this project can evolve into a production-grade customer intelligence platform.
## OUTPUT:

<img width="1868" height="782" alt="Image" src="https://github.com/user-attachments/assets/314ea4f5-c1cf-4f64-95f1-6301c55f639e" />

<img width="1876" height="837" alt="Image" src="https://github.com/user-attachments/assets/e6eb6ca8-79ce-4fb7-8138-25957caf9cad" />

<img width="1900" height="842" alt="Image" src="https://github.com/user-attachments/assets/281040c1-3c48-4889-889a-310edf4cae6e" />

<img width="300" height="435" alt="Image" src="https://github.com/user-attachments/assets/343707d0-e8aa-412e-8e7f-77d445a0e4c3" />

<img width="1832" height="786" alt="Image" src="https://github.com/user-attachments/assets/5821c5a3-a10a-4a8c-8a7d-3c640e3bad95" />
