# ============================================================
# CONCRETE COMPRESSIVE STRENGTH DASHBOARD
# Beginner-Friendly Streamlit Project
# ============================================================


# ============================================================
# 1. IMPORT LIBRARIES
# ============================================================

import streamlit as st
import pandas as pd
import plotly.express as px

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


# ============================================================
# 2. PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Concrete Strength Dashboard",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# 3. DASHBOARD DESIGN
# ============================================================

st.markdown(
    """
    <style>

    /* Main page */
    .stApp {
        background-color: #f7f8fa;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #f1f3f7;
        border-right: 1px solid #d9dde5;
    }

    /* Sidebar title */
    section[data-testid="stSidebar"] h1 {
        color: #252a34;
        font-size: 1.7rem;
        font-weight: 700;
    }

    /* Sidebar headings */
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #343944;
        font-weight: 600;
    }

    /* Sidebar labels */
    section[data-testid="stSidebar"] label {
        color: #404653;
        font-size: 0.92rem;
        font-weight: 500;
    }

    /* Number input */
    section[data-testid="stSidebar"]
    div[data-testid="stNumberInput"] > div {
        background-color: white;
        border-radius: 12px;
    }

    /* Metric cards */
    div[data-testid="stMetric"] {
        background-color: white;
        border-radius: 14px;
        border: 1px solid #e0e4ea;
        padding: 15px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# 4. DATASET PATH
# ============================================================

file_path = "cement.csv"


# ============================================================
# 5. LOAD DATASET
# ============================================================

try:

    data = pd.read_csv(file_path)

except Exception as error:

    st.error(
        "The dataset could not be loaded."
    )

    st.write(
        "Please check the dataset path:"
    )

    st.code(file_path)

    st.write(
        "Error:",
        error
    )

    st.stop()


# ============================================================
# 6. DATA CLEANING
# ============================================================

# Clean column names

data.columns = (
    data.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("-", "_")
)


# Required columns

required_columns = [
    "cement",
    "slag",
    "ash",
    "water",
    "superplastic",
    "coarseagg",
    "fineagg",
    "age",
    "strength"
]


# Check missing columns

missing_columns = [
    column
    for column in required_columns
    if column not in data.columns
]


if missing_columns:

    st.error(
        "The following required columns are missing:"
    )

    st.write(
        missing_columns
    )

    st.stop()


# Convert all required columns into numeric values

for column in required_columns:

    data[column] = pd.to_numeric(
        data[column],
        errors="coerce"
    )


# Remove missing values

data = data.dropna(
    subset=required_columns
)


# Remove duplicate rows

data = data.drop_duplicates()


# Remove invalid values

data = data[
    (data["cement"] >= 0) &
    (data["slag"] >= 0) &
    (data["ash"] >= 0) &
    (data["water"] > 0) &
    (data["superplastic"] >= 0) &
    (data["coarseagg"] >= 0) &
    (data["fineagg"] >= 0) &
    (data["age"] > 0) &
    (data["strength"] > 0)
]


# Reset index

data = data.reset_index(
    drop=True
)


# ============================================================
# 7. INPUT FEATURES
# ============================================================

features = [
    "cement",
    "slag",
    "ash",
    "water",
    "superplastic",
    "coarseagg",
    "fineagg",
    "age"
]


# ============================================================
# 8. CREATE INPUT AND OUTPUT DATA
# ============================================================

X = data[features]

y = data["strength"]


# ============================================================
# 9. SPLIT DATA INTO TRAINING AND TESTING DATA
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


# ============================================================
# 10. CREATE LINEAR REGRESSION MODEL
# ============================================================

model = LinearRegression()


# ============================================================
# 11. TRAIN THE MODEL
# ============================================================

model.fit(
    X_train,
    y_train
)


# ============================================================
# 12. TEST THE MODEL
# ============================================================

test_prediction = model.predict(
    X_test
)


# Calculate Mean Absolute Error

mae = mean_absolute_error(
    y_test,
    test_prediction
)


# Calculate R² Score

r2 = r2_score(
    y_test,
    test_prediction
)


# ============================================================
# 13. SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        "# Dashboard Controls"
    )

    st.markdown("---")


    # --------------------------------------------------------
    # CONCRETE PARAMETERS
    # --------------------------------------------------------

    st.markdown(
        "### 🧪 Concrete Parameters"
    )


    st.caption(
        "Change the values below to update the prediction."
    )


    # ========================================================
    # CEMENT
    # ========================================================

    cement = st.number_input(
        "Cement",
        min_value=float(
            data["cement"].min()
        ),
        max_value=float(
            data["cement"].max()
        ),
        value=float(
            data["cement"].median()
        ),
        step=1.0
    )


    # ========================================================
    # SLAG
    # ========================================================

    slag = st.number_input(
        "Slag",
        min_value=float(
            data["slag"].min()
        ),
        max_value=float(
            data["slag"].max()
        ),
        value=float(
            data["slag"].median()
        ),
        step=1.0
    )


    # ========================================================
    # ASH
    # ========================================================

    ash = st.number_input(
        "Ash",
        min_value=float(
            data["ash"].min()
        ),
        max_value=float(
            data["ash"].max()
        ),
        value=float(
            data["ash"].median()
        ),
        step=1.0
    )


    # ========================================================
    # WATER
    # ========================================================

    water = st.number_input(
        "Water",
        min_value=float(
            data["water"].min()
        ),
        max_value=float(
            data["water"].max()
        ),
        value=float(
            data["water"].median()
        ),
        step=1.0
    )


    # ========================================================
    # SUPERPLASTICIZER
    # ========================================================

    superplastic = st.number_input(
        "Superplasticizer",
        min_value=float(
            data["superplastic"].min()
        ),
        max_value=float(
            data["superplastic"].max()
        ),
        value=float(
            data["superplastic"].median()
        ),
        step=0.1
    )


    # ========================================================
    # COARSE AGGREGATE
    # ========================================================

    coarseagg = st.number_input(
        "Coarse Aggregate",
        min_value=float(
            data["coarseagg"].min()
        ),
        max_value=float(
            data["coarseagg"].max()
        ),
        value=float(
            data["coarseagg"].median()
        ),
        step=1.0
    )


    # ========================================================
    # FINE AGGREGATE
    # ========================================================

    fineagg = st.number_input(
        "Fine Aggregate",
        min_value=float(
            data["fineagg"].min()
        ),
        max_value=float(
            data["fineagg"].max()
        ),
        value=float(
            data["fineagg"].median()
        ),
        step=1.0
    )


    # ========================================================
    # AGE
    # ========================================================

    age = st.number_input(
        "Age (Days)",
        min_value=float(
            data["age"].min()
        ),
        max_value=float(
            data["age"].max()
        ),
        value=float(
            data["age"].median()
        ),
        step=1.0
    )


    st.markdown("---")

    st.success(
        "✓ Prediction updates automatically"
    )


# ============================================================
# 14. USER SELECTED DATA
# ============================================================

user_data = pd.DataFrame({

    "cement": [cement],

    "slag": [slag],

    "ash": [ash],

    "water": [water],

    "superplastic": [superplastic],

    "coarseagg": [coarseagg],

    "fineagg": [fineagg],

    "age": [age]

})


# ============================================================
# 15. PREDICT CONCRETE STRENGTH
# ============================================================

predicted_strength = model.predict(
    user_data
)[0]


# ============================================================
# 16. MAIN TITLE
# ============================================================

st.title(
    "🏗️ Concrete Compressive Strength Dashboard"
)


st.write(
    """
    This interactive dashboard predicts the compressive
    strength of concrete using **Linear Regression**.

    Select the concrete mixture proportions from the
    sidebar. The predicted strength changes automatically
    when the selected values are changed.
    """
)


# ============================================================
# 17. PREDICTION
# ============================================================

st.subheader(
    "🎯 Predicted Compressive Strength"
)


prediction_col1, prediction_col2, prediction_col3 = st.columns(3)


with prediction_col1:

    st.metric(
        "Predicted Strength",
        f"{predicted_strength:.2f} MPa"
    )


with prediction_col2:

    st.metric(
        "R² Score",
        f"{r2:.3f}"
    )


with prediction_col3:

    st.metric(
        "Mean Absolute Error",
        f"{mae:.2f} MPa"
    )


# ============================================================
# 18. SELECTED CONCRETE PROPORTIONS
# ============================================================

st.subheader(
    "🧪 Selected Concrete Proportions"
)


selected_data = pd.DataFrame({

    "Parameter": [
        "Cement",
        "Slag",
        "Ash",
        "Water",
        "Superplasticizer",
        "Coarse Aggregate",
        "Fine Aggregate",
        "Age"
    ],

    "Selected Value": [
        cement,
        slag,
        ash,
        water,
        superplastic,
        coarseagg,
        fineagg,
        age
    ]

})


st.dataframe(
    selected_data,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# 19. CHART 1
# SELECTED MIX VS DATASET AVERAGE
# ============================================================

st.subheader(
    "📊 1. Selected Mix vs Dataset Average"
)


comparison_data = pd.DataFrame({

    "Parameter": [
        "Cement",
        "Slag",
        "Ash",
        "Water",
        "Superplasticizer",
        "Coarse Aggregate",
        "Fine Aggregate",
        "Age"
    ],

    "Selected Value": [
        cement,
        slag,
        ash,
        water,
        superplastic,
        coarseagg,
        fineagg,
        age
    ],

    "Dataset Average": [
        data["cement"].mean(),
        data["slag"].mean(),
        data["ash"].mean(),
        data["water"].mean(),
        data["superplastic"].mean(),
        data["coarseagg"].mean(),
        data["fineagg"].mean(),
        data["age"].mean()
    ]

})


fig1 = px.bar(
    comparison_data,
    x="Parameter",
    y=[
        "Selected Value",
        "Dataset Average"
    ],
    barmode="group",
    title="Selected Mix vs Dataset Average",
    color_discrete_sequence=[
        "#3498DB",
        "#AED6F1"
    ]
)


fig1.update_layout(
    plot_bgcolor="white",
    paper_bgcolor="white"
)


st.plotly_chart(
    fig1,
    use_container_width=True
)


# ============================================================
# 20. CHART 2
# CEMENT VS STRENGTH
# ============================================================

st.subheader(
    "🟢 2. Cement vs Concrete Strength"
)


fig2 = px.scatter(
    data,
    x="cement",
    y="strength",
    title="Cement vs Concrete Strength",
    labels={
        "cement": "Cement",
        "strength": "Strength (MPa)"
    },
    color_discrete_sequence=[
        "#2ECC71"
    ]
)


fig2.add_scatter(
    x=[cement],
    y=[predicted_strength],
    mode="markers",
    marker={
        "size": 18,
        "symbol": "star",
        "color": "#145A32"
    },
    name="Selected Mix"
)


st.plotly_chart(
    fig2,
    use_container_width=True
)


# ============================================================
# 21. CHART 3
# SLAG VS STRENGTH
# ============================================================

st.subheader(
    "🟠 3. Slag vs Concrete Strength"
)


fig3 = px.scatter(
    data,
    x="slag",
    y="strength",
    title="Slag vs Concrete Strength",
    labels={
        "slag": "Slag",
        "strength": "Strength (MPa)"
    },
    color_discrete_sequence=[
        "#E67E22"
    ]
)


fig3.add_scatter(
    x=[slag],
    y=[predicted_strength],
    mode="markers",
    marker={
        "size": 18,
        "symbol": "star",
        "color": "#873600"
    },
    name="Selected Mix"
)


st.plotly_chart(
    fig3,
    use_container_width=True
)


# ============================================================
# 22. CHART 4
# ASH VS STRENGTH
# ============================================================

st.subheader(
    "🟣 4. Ash vs Concrete Strength"
)


fig4 = px.scatter(
    data,
    x="ash",
    y="strength",
    title="Ash vs Concrete Strength",
    labels={
        "ash": "Ash",
        "strength": "Strength (MPa)"
    },
    color_discrete_sequence=[
        "#9B59B6"
    ]
)


fig4.add_scatter(
    x=[ash],
    y=[predicted_strength],
    mode="markers",
    marker={
        "size": 18,
        "symbol": "star",
        "color": "#512E5F"
    },
    name="Selected Mix"
)


st.plotly_chart(
    fig4,
    use_container_width=True
)


# ============================================================
# 23. CHART 5
# WATER VS STRENGTH
# ============================================================

st.subheader(
    "🔴 5. Water vs Concrete Strength"
)


fig5 = px.scatter(
    data,
    x="water",
    y="strength",
    title="Water vs Concrete Strength",
    labels={
        "water": "Water",
        "strength": "Strength (MPa)"
    },
    color_discrete_sequence=[
        "#E74C3C"
    ]
)


fig5.add_scatter(
    x=[water],
    y=[predicted_strength],
    mode="markers",
    marker={
        "size": 18,
        "symbol": "star",
        "color": "#922B21"
    },
    name="Selected Mix"
)


st.plotly_chart(
    fig5,
    use_container_width=True
)


# ============================================================
# 24. CHART 6
# AGE VS STRENGTH
# ============================================================

st.subheader(
    "🔵 6. Age vs Concrete Strength"
)


fig6 = px.scatter(
    data,
    x="age",
    y="strength",
    title="Age vs Concrete Strength",
    labels={
        "age": "Age (Days)",
        "strength": "Strength (MPa)"
    },
    color_discrete_sequence=[
        "#16A085"
    ]
)


fig6.add_scatter(
    x=[age],
    y=[predicted_strength],
    mode="markers",
    marker={
        "size": 18,
        "symbol": "star",
        "color": "#0B5345"
    },
    name="Selected Mix"
)


st.plotly_chart(
    fig6,
    use_container_width=True
)


# ============================================================
# 25. CHART 7
# CORRELATION HEATMAP
# ============================================================

st.subheader(
    "🔥 7. Correlation Heatmap"
)


correlation = data[
    required_columns
].corr()


fig7 = px.imshow(
    correlation,
    text_auto=".2f",
    aspect="auto",
    title="Correlation Between Concrete Variables",
    color_continuous_scale="RdBu_r"
)


st.plotly_chart(
    fig7,
    use_container_width=True
)


# ============================================================
# 26. LINEAR REGRESSION COEFFICIENTS
# ============================================================

st.subheader(
    "📌 Linear Regression Model Coefficients"
)


coefficient_data = pd.DataFrame({

    "Parameter": [
        "Cement",
        "Slag",
        "Ash",
        "Water",
        "Superplasticizer",
        "Coarse Aggregate",
        "Fine Aggregate",
        "Age"
    ],

    "Coefficient": model.coef_

})


coefficient_data["Coefficient"] = (
    coefficient_data["Coefficient"]
    .round(4)
)


st.dataframe(
    coefficient_data,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# 27. MODEL INFORMATION
# ============================================================

st.subheader(
    "🤖 Model Information"
)


model_col1, model_col2 = st.columns(2)


with model_col1:

    st.write(
        "**Model:** Linear Regression"
    )

    st.write(
        "**Training Data:** 80%"
    )

    st.write(
        "**Testing Data:** 20%"
    )


with model_col2:

    st.write(
        f"**R² Score:** {r2:.3f}"
    )

    st.write(
        f"**Mean Absolute Error:** {mae:.2f} MPa"
    )

    st.write(
        "**Target Variable:** Concrete Strength"
    )


# ============================================================
# 28. ANALYSIS REPORT
# ============================================================

st.markdown("---")

st.subheader(
    "📑 Analysis Report"
)


# ------------------------------------------------------------
# Calculate basic statistics
# ------------------------------------------------------------

total_records = len(data)

average_strength = data[
    "strength"
].mean()

minimum_strength = data[
    "strength"
].min()

maximum_strength = data[
    "strength"
].max()

median_strength = data[
    "strength"
].median()


# ------------------------------------------------------------
# Calculate correlations
# ------------------------------------------------------------

correlation_values = (
    data[
        features + ["strength"]
    ]
    .corr()["strength"]
    .drop("strength")
)


highest_positive_variable = (
    correlation_values.idxmax()
)

highest_positive_value = (
    correlation_values.max()
)


highest_negative_variable = (
    correlation_values.idxmin()
)

highest_negative_value = (
    correlation_values.min()
)


# ------------------------------------------------------------
# Variable display names
# ------------------------------------------------------------

display_names = {

    "cement": "Cement",

    "slag": "Slag",

    "ash": "Ash",

    "water": "Water",

    "superplastic": "Superplasticizer",

    "coarseagg": "Coarse Aggregate",

    "fineagg": "Fine Aggregate",

    "age": "Age"

}


# ============================================================
# REPORT SUMMARY
# ============================================================

report1, report2, report3, report4 = st.columns(4)


with report1:

    st.metric(
        "Total Records",
        f"{total_records:,}"
    )


with report2:

    st.metric(
        "Average Strength",
        f"{average_strength:.2f} MPa"
    )


with report3:

    st.metric(
        "Minimum Strength",
        f"{minimum_strength:.2f} MPa"
    )


with report4:

    st.metric(
        "Maximum Strength",
        f"{maximum_strength:.2f} MPa"
    )


# ============================================================
# ANALYSIS SUMMARY
# ============================================================

st.markdown(
    "### 🔎 Analysis Summary"
)


st.write(
    f"""
    The cleaned dataset contains **{total_records:,} valid
    concrete observations**.

    The average compressive strength is
    **{average_strength:.2f} MPa**.

    The minimum recorded strength is
    **{minimum_strength:.2f} MPa**, while the maximum recorded
    strength is **{maximum_strength:.2f} MPa**.

    The median strength is
    **{median_strength:.2f} MPa**.

    Among the input variables,
    **{display_names[highest_positive_variable]}**
    has the highest positive correlation with concrete
    strength, with a correlation coefficient of
    **{highest_positive_value:.3f}**.

    **{display_names[highest_negative_variable]}**
    has the most negative correlation with concrete
    strength, with a correlation coefficient of
    **{highest_negative_value:.3f}**.
    """
)


# ============================================================
# SELECTED MIXTURE ANALYSIS
# ============================================================

st.markdown(
    "### 🧪 Selected Concrete Mix Analysis"
)


st.write(
    f"""
    For the concrete mixture selected in the sidebar, the
    Linear Regression model predicts a compressive strength
    of **{predicted_strength:.2f} MPa**.

    The selected mixture contains:

    • Cement: **{cement:.2f}**

    • Slag: **{slag:.2f}**

    • Ash: **{ash:.2f}**

    • Water: **{water:.2f}**

    • Superplasticizer: **{superplastic:.2f}**

    • Coarse Aggregate: **{coarseagg:.2f}**

    • Fine Aggregate: **{fineagg:.2f}**

    • Age: **{age:.0f} days**
    """
)


# ============================================================
# MODEL ANALYSIS
# ============================================================

st.markdown(
    "### 🤖 Model Analysis"
)


st.write(
    f"""
    Linear Regression was selected because concrete strength
    is a continuous numerical value.

    The dataset was divided into **80% training data** and
    **20% testing data**.

    The model achieved an R² score of **{r2:.3f}**.

    The Mean Absolute Error is **{mae:.2f} MPa**.

    The prediction is calculated directly from the concrete
    parameters selected in the sidebar. Therefore, changing
    Cement, Slag, Ash, Water, or the other input parameters
    changes the predicted compressive strength.
    """
)


# ============================================================
# CORRELATION TABLE
# ============================================================

st.markdown(
    "### 📊 Correlation with Concrete Strength"
)


correlation_table = pd.DataFrame({

    "Parameter": [
        display_names[name]
        for name in correlation_values.index
    ],

    "Correlation": [
        value
        for value in correlation_values.values
    ]

})


correlation_table[
    "Correlation"
] = correlation_table[
    "Correlation"
].round(3)


st.dataframe(
    correlation_table,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# FINAL CONCLUSION
# ============================================================

st.markdown(
    "### 📝 Conclusion"
)


st.info(
    f"""
    The concrete dataset was cleaned and analysed using
    Python, Streamlit and Plotly.

    Linear Regression was used to predict concrete
    compressive strength from the concrete mixture
    parameters.

    For the currently selected concrete mixture, the
    predicted compressive strength is
    **{predicted_strength:.2f} MPa**.

    The dashboard allows the user to interactively change
    the concrete proportions from the sidebar and observe
    the corresponding change in the predicted strength
    and graphical analysis.
    """
)


# ============================================================
# 29. FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "Concrete Compressive Strength Dashboard | "
    "Python • Streamlit • Plotly • Linear Regression"
)