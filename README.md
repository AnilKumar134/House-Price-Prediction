# 🏡 Bengaluru House Price Prediction
This project uses a machine learning approach to predict house prices in Bengaluru based on features like location, square footage, number of bedrooms (BHK), and more. The goal is to develop a regression model that can accurately estimate property prices using data preprocessing, EDA, and linear regression.

# 🔍 Problem Statement
Property buyers and real estate companies often struggle to determine the correct pricing for homes. This project builds a predictive model to estimate house prices in Bengaluru using various features from the dataset.

# 📊 Dataset Summary
- Attributes:
    - location
    - size
    - total_sqft
    - bath
    - balcony
    - price

# 🔧 Technologies Used
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- Jupyter Notebook
- Pickle

# 🚀 Project Workflow
1. Data Cleaning  
    - Handling missing values
    - Converting ranges (e.g., "2100 - 2850") into numerical values
    - Outlier removal based on price per square foot

2. Feature Engineering
    - Creating new features like price_per_sqft and bhk
    - One-hot encoding for location

3. Model Building
    - Linear Regression with GridSearchCV
    - Train-test split and cross-validation

4. Model Evaluation
    - R² Score
    - Predicting prices for sample inputs

# 📌 How to Run
Run the Flask server:  
Find server.py in server folder  

# 📦 Output Files
model.pkl – Trained machine learning model  
columns.json – Stores column info for deployment  

## 📬 Contact

**Anil Kumar**  
MIS Executive | Aspiring Data Analyst | • Python • SQL • Power BI • Excel • Machine Learning  
📧 [ak26458624@gmail.com](mailto:ak26458624@gmail.com) | 
[LinkedIn](https://www.linkedin.com/in/anil-kumar-554561225/)
