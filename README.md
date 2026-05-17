# 📊 Customer Churn Prediction

This project is a Machine Learning application that predicts whether a customer will churn (leave the service) or stay based on their usage behavior and account details.

The goal of this project is to help businesses identify customers who are at risk of leaving so they can take preventive actions.

---

## 🚀 Project Overview

Customer churn is one of the most important problems in subscription-based businesses. In this project, I built multiple machine learning models and compared their performance to find the best one.

After testing different models, I selected the best performing model using GridSearchCV.

---

## 🧠 Machine Learning Models Used

I experimented with multiple models:

- Logistic Regression  
- K-Nearest Neighbors (KNN)  
- Decision Tree Classifier  
- Random Forest Classifier  
- Support Vector Classifier (SVC with GridSearchCV)

After comparison, **GridSearchCV with SVC** gave the best accuracy and performance, so I selected it as the final model.

---

## 🔧 Steps Performed

### 1. Data Cleaning
- Handled missing values  
- Removed unnecessary columns  
- Fixed data inconsistencies  

---

### 2. Exploratory Data Analysis (EDA)
- Used **Matplotlib, Seaborn, and Plotly**  
- Analyzed customer behavior patterns  
- Visualized churn distribution  
- Checked relationships between features  

---

### 3. Feature Engineering
- Converted categorical variables into numeric form  
- Applied One-Hot Encoding  
- Created meaningful features from raw data  

---

### 4. Feature Scaling
- Standardized numerical features  
- Improved model performance and stability  

---

### 5. Train-Test Split
- Split dataset into training and testing sets  
- Ensured fair evaluation of models  

---

### 6. Model Training & Selection
- Trained multiple machine learning models  
- Used **GridSearchCV** for hyperparameter tuning  
- Compared performance of all models  

Final model selected:
> ✅ Support Vector Classifier (SVC) with GridSearchCV

---

## 📈 Model Evaluation

Models were evaluated using:
- Accuracy Score  
- Cross Validation (CV = 5)  
- Classification Metrics  

---

## 🖥️ Deployment

The final model is deployed using **Streamlit**, allowing users to input customer details and get real-time churn predictions.

Model is saved using:
- `joblib`

---

## 📦 Libraries Used

- NumPy  
- Pandas  
- Scikit-learn  
- Matplotlib  
- Seaborn  
- Plotly  
- Streamlit  
- Joblib  

---

## 🎯 Objective

The main goal of this project is to help businesses:
- Identify customers likely to churn  
- Improve customer retention strategies  
- Make data-driven decisions  

---

## 👨‍💻 Author

Built as a Machine Learning practice project focused on real-world business problem solving.

---

## ⭐ Future Improvements

- Add more advanced models like XGBoost  
- Improve feature engineering  
- Deploy on cloud (AWS / Render)  
- Add dashboard analytics in Streamlit  