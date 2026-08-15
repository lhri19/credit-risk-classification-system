# Credit Risk Classification System

#Project Overview

This project develops a Machine Learning-based Credit Risk Classification System that analyzes an applicant's personal and financial information and classifies the applicant into Low Credit Risk or High Credit Risk.

The system uses a Random Forest Classifier to predict the credit-risk category.

Problem Statement

Credit assessment involves several factors such as age, employment, housing, bank accounts, credit amount, loan duration, and loan purpose.

Manually analyzing these factors can be time-consuming. This project provides a computerized system that processes applicant information and provides a credit-risk classification.

Dataset

Dataset: German Credit Risk Dataset

Target Variable: Risk

Important Features:

- Age
- Sex
- Job
- Housing
- Saving Account
- Checking Account
- Credit Amount
- Duration
- Purpose

Project Workflow

- Data Loading
- Data Cleaning
- Handling Missing Values
- Feature Encoding
- Train-Test Split
- Random Forest Model Creation
- Model Training
- Prediction
- Model Evaluation
- Classification Report

Technologies Used

Programming Language

- Python

Data Science & Machine Learning

- Pandas
- NumPy
- Scikit-learn
- Random Forest Classifier

Web Technologies

- HTML
- CSS
- JavaScript

Development Tools

- Google Colab
- GitHub

Machine Learning Model

The project uses the Random Forest Classifier.

Random Forest combines multiple decision trees to make a final classification. It is suitable for classification problems because it can learn patterns from multiple applicant and financial features.

Data Preprocessing

The dataset is processed before training the model.

The preprocessing steps include:

1. Removing unnecessary columns
2. Handling missing values
3. Encoding categorical features
4. Separating input features and target variable
5. Splitting the dataset into training and testing data

Model Training

The dataset is divided into:

- 80% Training Data
- 20% Testing Data

The Random Forest model is trained using the training data and then tested using unseen testing data.

Model Evaluation

The model is evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Classification Report

System Working

The web system follows this process:

User Input → Data Processing → Classification → Result

The user enters applicant details such as age, gender, job, housing, credit amount, and loan duration.

The system processes the information and provides the corresponding credit-risk classification.

Project Files

File| Description
"index.html"| Creates the structure of the webpage
"style.css"| Provides webpage design and styling
"scripts.js"| Handles JavaScript functionality
"credit_risk_model.py"| Contains the Machine Learning implementation
"german_credit_data.csv"| Contains the credit-risk dataset
"README.md"| Contains project documentation

Prediction Output

The system classifies an applicant into:

Low Credit Risk

or

High Credit Risk

Advantages

- Faster credit-risk assessment
- Reduces manual analysis
- Easy-to-use web interface
- Uses Machine Learning for classification
- Provides quick prediction results

Future Enhancements

- Use a larger real-world dataset
- Improve model performance
- Compare multiple Machine Learning algorithms
- Connect the web interface directly to the trained model
- Deploy the system as an online application
- Add graphical analysis and dashboards

Conclusion

The Credit Risk Classification System demonstrates how Machine Learning can be used to analyze applicant information and classify credit risk.

The project combines Python, Pandas, NumPy, Scikit-learn, Random Forest, HTML, CSS, and JavaScript to create a complete credit-risk classification project.

Author

Lahari Sanaga

B.Tech – CSE (Data Science)
