
# 🧠 Stroke Prediction using XGBoost and SMOTE (PyCaret + Streamlit)

This project is a machine learning application that predicts the likelihood of a stroke using healthcare data. It uses **XGBoost**, **SMOTE** for handling class imbalance, **PyCaret** for model management, and **Streamlit** for easy deployment.

---

## 📌 Project Overview

- **Goal**: Predict whether a patient is likely to have a stroke based on medical history and demographic data.
- **Frameworks**:
  - PyCaret (for preprocessing, training, and model tuning)
  - Streamlit (for interactive web app deployment)
  - SMOTE (to address class imbalance)
- **Model**: XGBoost (selected based on best Recall performance)

---

## 📁 Project Structure

```
stroke-app/
├── streamlit_app.py        # Streamlit web app
├── xgb_model_final.pkl     # Trained XGBoost model saved by PyCaret
├── requirements.txt        # List of required Python packages
├── README.md               # Project documentation
```

---

## 📊 Dataset

- Dataset: `healthcare-dataset-stroke-data.csv`
- Source: [Kaggle](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)
- Target Variable: `stroke` (0 = No, 1 = Yes)

---

## ⚙️ Features Used

- `age`, `hypertension`, `heart_disease`, `avg_glucose_level`, `bmi`
- Categorical: `gender`, `ever_married`, `work_type`, `Residence_type`, `smoking_status`

---

## 🚀 How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/stroke-app.git
cd stroke-app
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App
```bash
streamlit run streamlit_app.py
```

### 4. Upload the Test Dataset
Use the file uploader in the app to upload your CSV file and get predictions.

---

## ☁️ How to Deploy on Streamlit Cloud

1. Push your project to a public GitHub repository
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Click **"Deploy an app"** and link your GitHub repo
4. Set `streamlit_app.py` as the main file
5. Deploy and share your app!

---

## ✅ Model Evaluation

- The best model was selected based on **Recall** (sensitivity), which is critical in medical diagnoses.
- SMOTE was used to balance the dataset before training.
- PyCaret's `compare_models()` helped benchmark several models easily.

---

## ✨ Future Improvements

- Add data validation on upload
- Improve UI with charts and visual explanations
- Include confidence scores and explanations for predictions

---

## 🙋‍♂️ Author

**NIWABIINE Edivina**  
Data Science Enthusiast | ML Practitioner  
Feel free to connect!

---

## 📜 License

This project is licensed under the MIT License.
