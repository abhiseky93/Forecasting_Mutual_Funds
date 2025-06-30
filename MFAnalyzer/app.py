import streamlit as st
import requests
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def get_nav_data(scheme_code):
    url = f"https://api.mfapi.in/mf/{scheme_code}"
    res = requests.get(url).json()
    data = res['data'][:6]  # last 6 days
    df = pd.DataFrame(data)
    df['nav'] = df['nav'].astype(float)
    df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')
    df['day'] = np.arange(len(df))[::-1]
    return df[['day', 'date', 'nav']]

def predict_nav(df):
    X = df[['day']]
    y = df['nav']
    model = LinearRegression().fit(X, y)
    predicted = model.predict([[6]])  # next day (day 6)
    return predicted[0]

# Streamlit App UI
st.title("📊 Mutual Fund AI Bot (India)")
scheme_code = st.text_input("Enter Mutual Fund Scheme Code (e.g., 118550):", "118550")

if scheme_code:
    try:
        df = get_nav_data(scheme_code)
        predicted_nav = predict_nav(df)
        current_nav = df['nav'].iloc[0]

        st.subheader(f"📅 Last 6 Days NAV Data")
        st.dataframe(df[['date', 'nav']])

        st.subheader("🔮 Prediction")
        st.markdown(f"**Predicted NAV for next day:** ₹{predicted_nav:.2f}")
        st.markdown(f"**Current NAV:** ₹{current_nav:.2f}")

        diff = predicted_nav - current_nav
        pct = (diff / current_nav) * 100

        if pct > 1.5:
            st.success(f"✅ Recommendation: **BUY** (Expected ↑ {pct:.2f}%)")
        elif pct < -1.5:
            st.error(f"❌ Recommendation: **SELL** (Expected ↓ {abs(pct):.2f}%)")
        else:
            st.info(f"🟡 Recommendation: **HOLD** (Minimal change expected)")

        # Plot NAV Trend
        fig, ax = plt.subplots()
        ax.plot(df['date'], df['nav'], marker='o')
        ax.set_title("NAV Trend (Last 6 Days)")
        ax.set_xlabel("Date")
        ax.set_ylabel("NAV (₹)")
        ax.grid(True)
        st.pyplot(fig)

    except Exception as e:
        st.error(f"Error fetching data. Please check the scheme code.\n\n{e}")
