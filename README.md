# Concrete Compressive Strength Dashboard
### Interactive Data Analysis and Machine Learning for Concrete Strength Prediction
##  Project Overview
The **Concrete Compressive Strength Dashboard** is an interactive data-analysis and machine-learning application developed using **Python, Pandas, Plotly, Streamlit, and Scikit-learn**.
The dashboard analyses concrete mixture parameters and predicts **compressive strength** using a **Linear Regression** model. Users can modify concrete parameters through the interactive sidebar and instantly view the predicted strength along with graphical analysis.
##  Objectives

1. Analyse the factors affecting concrete compressive strength.
2. Predict concrete compressive strength using machine learning.
3. Provide interactive controls for selecting concrete parameters.
4. Visualize relationships between concrete ingredients and strength.
5. Evaluate the performance of the prediction model.

##  Tools & Technologies

| Category           | Technology                          |
| ------------------ | ----------------------------------- |
| Programming        | Python                              |
| Data Processing    | Pandas                              |
| Data Visualization | Plotly                              |
| Dashboard          | Streamlit                           |
| Machine Learning   | Scikit-learn                        |
| Prediction Model   | Linear Regression                   |
| Model Evaluation   | R² Score, Mean Absolute Error (MAE) |

##  Input Parameters

The model uses the following eight parameters:

* Cement
* Slag
* Ash
* Water
* Superplasticizer
* Coarse Aggregate
* Fine Aggregate
* Age

###  Target Variable

**Concrete Compressive Strength (MPa)**

##  Dashboard Features

### 1. Strength Prediction

Predicts concrete compressive strength based on the selected mixture parameters.

### 2. Mix Comparison

Compares the selected concrete mixture with the average values in the dataset.

### 3. Parameter Analysis

The dashboard provides graphical analysis of:

* Cement vs Strength
* Slag vs Strength
* Ash vs Strength
* Water vs Strength
* Age vs Strength

### 4. Correlation Analysis

A correlation heatmap displays relationships among the concrete mixture parameters and compressive strength.

### 5. Regression Analysis

Displays the Linear Regression coefficients for the input parameters.

### 6. Statistical Analysis

Provides:

* Total number of records
* Average strength
* Minimum strength
* Maximum strength
* Median strength

### 7. Model Evaluation

The model is evaluated using:

* **R² Score**
* **Mean Absolute Error (MAE)**

##  Machine Learning Model

The project uses **Linear Regression** because concrete compressive strength is a continuous numerical variable.

The dataset is divided into:

* **80% Training Data**
* **20% Testing Data**

The eight concrete parameters are used as independent variables to predict compressive strength.

##  Methodology

**Data Collection → Data Cleaning → Data Preparation → Exploratory Data Analysis → Data Visualization → Linear Regression → Prediction → Model Evaluation → Interactive Dashboard**

##  Data Preprocessing

The dataset is processed before modelling by:

* Standardizing column names
* Converting required columns into numeric format
* Handling missing values
* Removing duplicate records
* Removing invalid parameter values
* Preparing features and target variables

##  Model Evaluation

### R² Score

R² indicates how well the Linear Regression model explains the variation in concrete compressive strength.

### Mean Absolute Error (MAE)

MAE represents the average difference between the actual and predicted compressive strength values.

##  Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/concrete-compressive-strength-dashboard.git
```

### 2. Open the Project Folder

```bash
cd concrete-compressive-strength-dashboard
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application

```bash
streamlit run app.py
```

The dashboard will open in your web browser.

##  Project Structure

```text
concrete-compressive-strength-dashboard/
│
├── app.py
├── cement.csv
├── requirements.txt
├── README.md
└── .gitignore
```

> If your Python file or dataset has a different name, replace `app.py` and `cement.csv` with your actual filenames.

##  Future Scope

The dashboard can be further enhanced with:

* Advanced machine-learning models
* Concrete mixture optimization
* Strength forecasting
* Real-time data integration
* Comparative model analysis
* Automated report generation
* Cloud deployment

##  Outcome

The project provides a centralized and interactive platform for **analysing concrete data, visualizing relationships, and predicting compressive strength**.

Users can modify concrete parameters through the sidebar and observe the corresponding prediction and graphical analysis.

##  Project

**Concrete Compressive Strength Dashboard**

**Technologies:** Python | Pandas | Plotly | Streamlit | Scikit-learn

---

###  If you find this project useful, consider giving the repository a star!
