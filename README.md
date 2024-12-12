# Python-Flask---Heart-Attack-Predictor

## Overview
This project is a web-based tool built with Flask to help doctors predict the likelihood of patients suffering from heart attacks. By leveraging patient medical history and logistic regression, the application provides a predictive score to assist in early diagnosis and intervention.

---

## Features
1. **User Authentication:**
   - Doctors can log in using their credentials to access the prediction tool.

2. **Data Input:**
   - Doctors can input patient medical details, such as age, cholesterol levels, blood pressure, and other relevant health metrics.

3. **Prediction Model:**
   - The tool uses a Logistic Regression model trained on a heart disease dataset from Kaggle to predict the likelihood of a heart attack.

4. **Database Integration:**
   - Patient information is stored and retrieved using MySQL.

---

## Technologies Used
- **Backend:** Python, Flask
- **Frontend:** HTML, CSS
- **Database:** MySQL
- **Libraries:** `sklearn`, `pandas`, `numpy`, `flask-mysql-connector`
