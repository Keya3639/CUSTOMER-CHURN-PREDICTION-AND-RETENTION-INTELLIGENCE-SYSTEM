import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

# ---------------------------------
# Page Config
# ---------------------------------
st.set_page_config(
    page_title="Customer Churn Intelligence Dashboard",
    page_icon="📉",
    layout="wide"
)

# ---------------------------------
# Load Model
# ---------------------------------
@st.cache_resource
def load_model():
    return joblib.load("model/churn_model.pkl")

model = load_model()

# ---------------------------------
# Title
# ---------------------------------
st.title("📊 Customer Churn Prediction & Retention Intelligence System")
st.caption("AI-powered churn risk analysis, segmentation & insights")

st.divider()

# =====================================================
# SINGLE CUSTOMER PREDICTION (FORM)
# =====================================================
st.sidebar.header("👤 Single Customer Prediction")

with st.sidebar.form("single_prediction_form"):
    age = st.number_input("Age", 18, 100, 30)
    gender = st.selectbox("Gender", ["Male", "Female"])
    tenure = st.number_input("Tenure (months)", 0, 100, 12)
    usage = st.number_input("Usage Frequency", 0, 100, 10)
    support_calls = st.number_input("Support Calls", 0, 50, 2)
    payment_delay = st.number_input("Payment Delay (days)", 0, 100, 0)
    subscription = st.selectbox("Subscription Type", ["Basic", "Standard", "Premium"])
    contract = st.selectbox("Contract Length", ["Monthly", "Quarterly", "Annual"])
    total_spend = st.number_input("Total Spend", 0.0, 10000.0, 500.0)
    last_interaction = st.number_input("Days Since Last Interaction", 0, 365, 10)

    predict_btn = st.form_submit_button("🔍 Predict Churn")

if predict_btn:
    input_df = pd.DataFrame([{
        "Age": age,
        "Gender": gender,
        "Tenure": tenure,
        "Usage Frequency": usage,
        "Support Calls": support_calls,
        "Payment Delay": payment_delay,
        "Subscription Type": subscription,
        "Contract Length": contract,
        "Total Spend": total_spend,
        "Last Interaction": last_interaction
    }])

    pred = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0][1]

    st.subheader("🔮 Prediction Result")

    col1, col2, col3 = st.columns(3)
    col1.metric("Churn Prediction", "YES" if pred == 1 else "NO")
    col2.metric("Churn Probability", f"{prob:.2%}")

    if prob >= 0.7:
        risk = "🔴 High Risk"
    elif prob >= 0.4:
        risk = "🟡 Medium Risk"
    else:
        risk = "🟢 Low Risk"

    col3.metric("Customer Risk Level", risk)

    st.subheader("📌 Retention Strategy")
    if risk == "🔴 High Risk":
        st.error("Immediate retention required – discounts & proactive support")
    elif risk == "🟡 Medium Risk":
        st.warning("Engagement campaigns recommended")
    else:
        st.success("Customer is stable – upsell opportunities")


# =====================================================
# BULK PREDICTION & DASHBOARD
# =====================================================
st.divider()
st.subheader("📊 Bulk Prediction & Churn Dashboard")

uploaded_file = st.file_uploader("Upload Customer Dataset (CSV)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    preds = model.predict(df)
    probs = model.predict_proba(df)[:, 1]

    df["Churn_Predicted"] = preds
    df["Churn_Probability"] = probs
    df["Risk_Level"] = pd.cut(
        probs, bins=[0, 0.4, 0.7, 1],
        labels=["Low", "Medium", "High"]
    )

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Customers", len(df))
    col2.metric("Predicted Churners", int(df["Churn_Predicted"].sum()))
    col3.metric("Churn Rate", f"{df['Churn_Predicted'].mean():.2%}")

    st.subheader("Customer Risk Distribution")
    risk_counts = df["Risk_Level"].value_counts()

    fig2, ax2 = plt.subplots()
    ax2.pie(risk_counts, labels=risk_counts.index, autopct="%1.1f%%")
    st.pyplot(fig2)

    st.dataframe(df)

    st.download_button(
        "⬇ Download Report",
        data=df.to_csv(index=False),
        file_name="churn_results.csv",
        mime="text/csv"
    )



st.markdown("---")
st.markdown("Developed by **Keya Das** | Customer Churn Prediction & Retention Intelligence System")
