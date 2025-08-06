# 🌍 Air Quality & Health Risk Prediction System

A smart data science web application that predicts **health risks** based on real-time air quality data using **Decision Tree Classifier**. Built with **Python**, **Streamlit**, and powered by **WAQI API** for fetching live environmental data. The system accepts user input (City name), fetches real-time AQI & weather metrics, and delivers risk prediction with actionable health recommendations.

---

## 🚀 Features

- 🌐 Real-time air quality & weather data using WAQI API
- 🌳 Decision Tree-based health risk classification
- 🧠 Machine Learning model trained on environmental indicators (PM2.5, PM10, CO, NO2, SO2, O3, Temp, Humidity, Wind)
- 🖥️ Streamlit frontend with easy-to-use UI
- ✅ Displays predicted health risk and relevant health advisory

---

## 🛠️ Tech Stack

- **Language**: Python
- **Libraries**: Pandas, NumPy, Scikit-learn, Requests, Joblib
- **ML Model**: Decision Tree Classifier
- **API**: WAQI (World Air Quality Index)
- **Frontend**: Streamlit
- **Deployment**: Localhost / Streamlit Cloud

---

## 📁 Project Structure

```bash
.
├── fetch.py              # Fetches real-time AQI data from WAQI API
├── model.pkl             # Saved Decision Tree model
├── frontend.py           # Streamlit frontend app
├── requirements.txt      # All dependencies
└── README.md             # This file
```

## 🧪 Model Input Features
```
| Feature   | Description                          |
|-----------|--------------------------------------|
| City      | User-selected city (dropdown)        |
| PM2.5     | Fine particulate matter              |
| PM10      | Coarse particulate matter            |
| CO        | Carbon Monoxide level                |
| NO2       | Nitrogen Dioxide level               |
| SO2       | Sulfur Dioxide level                 |
| O3        | Ozone level                          |
| Temp      | Temperature                          |
| Humidity  | Relative Humidity                    |
| Wind      | Wind Speed                           |

🧾 Target Column: Health_Risk (Low, Medium, High)
```

🖥️ How to Run

1️⃣ Clone the Repo

```bash
git clone https://github.com/yourusername/air-quality-health-risk.git
cd air-quality-health-risk
```
2️⃣ Install Requirements

```bash
pip install -r requirements.txt
```
3️⃣ Train and Save the Model (Optional)

```bash
python train_model.py
```
4️⃣ Run the Streamlit App

```bash
streamlit run frontend.py
```
# 📌 How It Works

User type City.

The app fetches real-time AQI + weather data using fetch.py.

Fetched data is preprocessed and passed to the saved decision tree model.

Prediction (Health Risk Level) is displayed along with health advice.

# 📦 Requirements

Python 3.7+

Streamlit

Scikit-learn

Pandas

Requests

Joblib

## 💡 Example Use Case

👤 User type Delhi → App fetches current air quality → Model predicts Severe health risk → 🩺 Health suggestion shown: "Avoid outdoor activity. Use masks and stay hydrated."



## 📬 Contact
Made with ❤️ by Sarthak Arsul

## 📝 License
This project is licensed under the MIT License.
