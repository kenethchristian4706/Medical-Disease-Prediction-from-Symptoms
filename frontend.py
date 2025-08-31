import streamlit as st
import pandas as pd
import joblib

# Load dataset and model
df = pd.read_csv("symbipredict_2022.csv")
model = joblib.load("Disease_prediction.joblib")

# Symptoms (assuming all columns except 'Disease' are symptoms)
# symptom_columns = [col for col in df.columns if col.lower() != "disease"]
# Symptoms = all columns except label columns like 'prognosis' or 'Disease'
symptom_columns = [col for col in df.columns if col.lower() not in ["prognosis", "disease"]]


st.title("🩺 Disease Prediction App")
st.write("Select your symptoms and predict the possible disease.")

# Searchable multiselect dropdown
selected_symptoms = st.multiselect(
    "Select Symptoms:",
    options=symptom_columns,
    default=[],
    help="Start typing to search symptoms."
)

# Convert selection to input vector
input_data = [1 if symptom in selected_symptoms else 0 for symptom in symptom_columns]
input_df = pd.DataFrame([input_data], columns=symptom_columns)

if st.button("Predict Disease"):
    prediction = model.predict(input_df)[0]
    st.success(f"🔍 Predicted Disease: **{prediction}**")
# import streamlit as st
# import pandas as pd
# import joblib

# # Load model and data
# df = pd.read_csv("symbipredict_2022.csv")
# model = joblib.load("Disease_prediction.joblib")

# # Extra files for description and precautions
# desc_df = pd.read_csv("symptom_Description.csv")
# prec_df = pd.read_csv("symptom_precaution.csv")

# # Clean up column names (just in case)
# desc_df.columns = [c.strip().lower() for c in desc_df.columns]
# prec_df.columns = [c.strip().lower() for c in prec_df.columns]

# # Symptoms list (exclude target columns)
# symptom_columns = [col for col in df.columns if col.lower() not in ["prognosis", "disease"]]

# st.title("🩺 Disease Prediction App")
# st.write("Select your symptoms and predict the possible disease.")

# # User selects symptoms
# selected_symptoms = st.multiselect(
#     "Select Symptoms:",
#     options=symptom_columns,
#     default=[],
#     help="Start typing to search symptoms."
# )

# # Encode user input
# input_data = [1 if symptom in selected_symptoms else 0 for symptom in symptom_columns]
# input_df = pd.DataFrame([input_data], columns=symptom_columns)

# if st.button("Predict Disease"):
#     # Predict
#     prediction = model.predict(input_df)[0]

#     st.success(f"🔍 Predicted Disease: **{prediction}**")

#     # Get description
#     desc_row = desc_df[desc_df["disease"] == prediction]
#     if not desc_row.empty:
#         st.subheader("📖 Description")
#         st.write(desc_row["description"].values[0])
#     else:
#         st.info("No description available.")

#     # Get precautions
#     prec_row = prec_df[prec_df["disease"] == prediction]
#     if not prec_row.empty:
#         st.subheader("🛡️ Precautions")
#         precs = prec_row.iloc[0].drop("disease").dropna().tolist()
#         for i, p in enumerate(precs, 1):
#             st.write(f"{i}. {p}")
#     else:
#         st.info("No precautions available.")
