# 💧 ML Based Water Quality Monitoring and Prediction System

A Hybrid Water Quality Prediction System that combines CPCB Rule-Based Classification with Machine Learning to provide accurate, interpretable, and real-time water quality assessment.

---

## 📖 Project Overview

Water quality monitoring is essential for protecting public health, aquatic ecosystems, and environmental sustainability.

This project integrates:

- CPCB (Central Pollution Control Board) Water Quality Standards
- Random Forest Machine Learning Model
- Feature Engineering
- Interactive Streamlit Dashboard

The system classifies water quality into five CPCB classes and provides prediction confidence, feature importance analysis, and water quality insights.

---

## 🎯 Objectives

- Automate water quality assessment
- Reduce dependence on manual interpretation
- Improve prediction accuracy using machine learning
- Provide explainable predictions through feature importance
- Support environmental monitoring and decision making

---

## 🏗 System Architecture

### Input Parameters

Users provide:

- Temperature (°C)
- Dissolved Oxygen (DO)
- pH
- Conductivity
- BOD
- Nitrate
- Fecal Coliform

### CPCB Rule Engine

The system first evaluates:

- DO
- BOD
- pH
- Fecal Coliform

and assigns a CPCB water quality class.

### Feature Engineering

Additional features generated:

- DO/BOD Ratio
- Pollution Index
- pH Deviation
- Log Conductivity
- Rule Label Feature

### Machine Learning Layer

Algorithm Used:

**Random Forest Classifier**

Pipeline:

1. Data Preprocessing
2. Feature Engineering
3. Standard Scaling
4. Random Forest Classification
5. Confidence Score Generation

---

## 📊 Water Quality Classes

| Class | Description |
|---------|-------------|
| A | Drinking Water Source |
| B | Outdoor Bathing |
| C | Treatment Required |
| D | Fisheries |
| E | Irrigation |

---

## 🚀 Features

### CPCB Rule-Based Classification

Implements official CPCB standards.

### Machine Learning Prediction

Predicts water quality using Random Forest.

### Confidence Score

Displays prediction confidence using probability scores.

### Comparison Analysis

Compares:

- CPCB Prediction
- Machine Learning Prediction

### Water Quality Insights

Provides:

- Safety Assessment
- Parameter Warnings
- Pollution Indicators

### Feature Importance

Displays influential factors affecting predictions.

---

## 🛠 Technologies Used

### Programming Language

- Python

### Libraries

- Streamlit
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Joblib
- OpenPyXL

### Development Tools

- VS Code
- Jupyter Notebook
- Git & GitHub

---

## 📁 Project Structure

```text
Water-Quality-Prediction-Dashboard/
│
├── app.py
├── model.pkl
├── scaler.pkl
├── train_model.ipynb
├── water_quality.xlsx
├── Project_Report.pdf
├── Project_Presentation.pptx
├── requirements.txt
├── README.md
├── .gitignore
│
└── screenshots/
    ├── dashboard_home.png
    ├── prediction_results.png
    └── feature_importance.png
```

---

## 📸 Screenshots

### Dashboard Home

![Dashboard Home](screenshots/dashboard_home.png)

### Prediction Results

![Prediction Results](screenshots/prediction_results.png)

### Feature Importance Analysis

![Feature Importance](screenshots/feature_importance.png)

---

## ▶️ How to Run

### Clone Repository

```bash
git clone https://github.com/yourusername/Water-Quality-Prediction-Dashboard.git
```

### Open Project Folder

```bash
cd Water-Quality-Prediction-Dashboard
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 🔬 Machine Learning Workflow

1. Load Dataset
2. Data Cleaning
3. Feature Engineering
4. CPCB Rule Generation
5. Standard Scaling
6. Random Forest Training
7. Model Evaluation
8. Deployment with Streamlit

---

## 📈 Project Highlights

- Hybrid CPCB + ML Prediction Framework
- Explainable AI through Feature Importance
- Real-Time Prediction Dashboard
- Regulatory Compliance
- User-Friendly Interface
- Environmental Decision Support Tool

---

## 🔮 Future Enhancements

- IoT Sensor Integration
- Water Quality Index (WQI)
- Geospatial Mapping
- Mobile Application
- SHAP Explainability
- Multi-Language Support
- Automated PDF Reports

---

## 👨‍💻 Author

### Rishabh Vyas


Bachelor of Technology (Computer Science & Engineering)

Drs. Kiran & Pallavi Patel Global University

2026

---

## 📚 References

- Central Pollution Control Board (CPCB)
- World Health Organization (WHO)
- Scikit-Learn Documentation
- Random Forest Research Papers
