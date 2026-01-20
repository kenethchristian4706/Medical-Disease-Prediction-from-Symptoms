# 🩺 Disease Prediction from Symptoms
url :https://medical-disease-prediction-from-symptoms-p72tm5x4bkgppzhcyab4t.streamlit.app/
A **Machine Learning + Streamlit** web app that predicts the most likely disease based on selected symptoms.  
The app also provides **disease descriptions** and **precautionary measures** to guide the user.

---

## 🚀 Features
- Interactive **searchable dropdown** to select symptoms  
- Encodes symptoms automatically (`1` = present, `0` = not present)  
- Predicts the **disease name** using a trained ML model  
- Displays **disease description** and **precautions**  
- Built with **Streamlit**, easy to use in a web browser  

---

## 🛠️ Tech Stack
- **Python 3.x**
- **Streamlit**
- **Pandas**
- **Scikit-learn**
- **Joblib**

---

## 📂 Project Structure
.
├── frontend.py # Streamlit app
├── Disease_prediction.joblib # Trained ML model
├── symbipredict_2022.csv # Dataset with symptoms
├── symptom_Description.csv # Disease → description mapping
├── symptom_precaution.csv # Disease → precaution mapping
├── requirements.txt # Dependencies
└── README.md # Project documentation

yaml
Copy code

---

## ⚡ Installation & Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/<your-username>/medical-disease-prediction-from-symptoms.git
   cd medical-disease-prediction-from-symptoms
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Streamlit app:

bash
Copy code
streamlit run frontend.py
Open the app in your browser:


🌐 Deployment (Streamlit Cloud)
Push this repo to GitHub

Go to Streamlit Cloud

Create a new app and connect your repo

Set frontend.py as the entry file

Done ✅ your app is live!

📊 Example Workflow
User selects symptoms (e.g., itching, skin rash, nodal skin eruptions)

Model predicts: Fungal infection

App displays:

Description: Fungal infections are caused by fungi invading the skin or body tissues.

Precautions:

Maintain good hygiene

Use antifungal medication as prescribed

Avoid sharing personal items

Keep affected area clean and dry

📈 Accuracy
The trained model achieves 95%+ accuracy on the test dataset.

