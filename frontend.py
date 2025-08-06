import streamlit as st
import requests
import pandas as pd
import pickle
from dotenv import load_dotenv
import os

load_dotenv()
my_token = os.getenv("AQI_API_TOKEN")

# Load trained model
with open("decision_tree_model.pkl", "rb") as f:
    model = pickle.load(f)

# Define risk descriptions & solutions
risk_details = {
    'Low': {
        'description': "Air quality is satisfactory, and air pollution poses little or no risk.",
        'solution': "You can continue with your regular outdoor activities."
    },
    'Medium': {
        'description': "Air quality is acceptable. However, there may be a concern for sensitive individuals.",
        'solution': "Sensitive people should reduce prolonged outdoor exertion."
    },
    'High': {
        'description': "Members of sensitive groups may experience health effects. General public is not likely to be affected.",
        'solution': "Limit outdoor activities, especially for children, elderly, and people with respiratory issues."
}
}

# Streamlit UI
st.title("🌍 Air Quality Health Risk Predictor")
st.write("Enter your city name to get real-time air quality health risk and precautions.")

# Dynamic city input
city = st.text_input("Enter City Name (e.g., Delhi, Mumbai, Patna)").strip()

if st.button("🔍 Predict Health Risk"):
    if not city:
        st.warning("Please enter a valid city name.")
    else:
        with st.spinner("Fetching air quality data..."):
            url = f"https://api.waqi.info/feed/{city}/?token={my_token}"
            response = requests.get(url)
            data = response.json()

        if data["status"] == "ok":
            iaqi = data["data"].get("iaqi", {})
            datetime = data["data"]["time"]["s"]

            features = {
                'City': city,
                'AQI': data["data"].get("aqi", 0),
                'PM2.5': iaqi.get("pm25", {}).get("v", 0),
                'PM10': iaqi.get("pm10", {}).get("v", 0),
                'CO': iaqi.get("co", {}).get("v", 0),
                'NO2': iaqi.get("no2", {}).get("v", 0),
                'SO2': iaqi.get("so2", {}).get("v", 0),
                'O3': iaqi.get("o3", {}).get("v", 0),
                'Temp': iaqi.get("t", {}).get("v", 0),
                'Humidity': iaqi.get("h", {}).get("v", 0),
                'Wind': iaqi.get("w", {}).get("v", 0),
            }

            # Convert to DataFrame
            df = pd.DataFrame([features])
            df["City"] = df["City"].astype("category").cat.codes

            # Predict
            prediction = model.predict(df)[0]

            # Display results
            st.subheader(f"🏥 Health Risk Level: **{prediction}**")

            if prediction in risk_details:
                desc = risk_details[prediction]["description"]
                solution = risk_details[prediction]["solution"]
                st.write(f"📋 **Description:** {desc}")
                st.write(f"💡 **Suggested Precaution:** {solution}")
            else:
                st.info("No additional information available for this risk level.")

        else:
            st.error("❌ Failed to fetch data. Please check the city name or try again later.")