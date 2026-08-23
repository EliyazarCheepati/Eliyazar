import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)


# ============================================================
# 1. PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Student Performance Analysis",
    page_icon="🎓",
    layout="wide"
)


# ============================================================
# 2. PROJECT TITLE
# ============================================================

st.title(
    "🎓 Profile-Based Student Performance Analysis"
)

st.subheader(
    "Teacher Recommendation System Using Data Mining"
)

st.write(
    "A data mining based system for student profile analysis, "
    "performance prediction, machine learning algorithm comparison, "
    "and teacher recommendation."
)

st.divider()


# ============================================================
# 3. DATASET PATH
# ============================================================

file_path = r"C:\Users\HP\OneDrive\Documents\StudentPerformanceFactors.csv.xlsx"


# ============================================================
# 4. LOAD DATASET
# ============================================================

@st.cache_data
def load_data():

    data = pd.read_excel(file_path)

    return data


try:

    df = load_data()

except Exception as e:

    st.error(
        "Unable to load the dataset."
    )

    st.write(
        "Check whether this file exists:"
    )

    st.code(file_path)

    st.stop()


# ============================================================
# 5. CLEAN COLUMN NAMES
# ============================================================

df.columns = (
    df.columns
    .str.strip()
    .str.replace(" ", "_")
)


# ============================================================
# 6. CHECK REQUIRED COLUMN
# ============================================================

if "Exam_Score" not in df.columns:

    st.error(
        "Exam_Score column was not found in the dataset."
    )

    st.write(
        "Available columns:"
    )

    st.write(
        df.columns.tolist()
    )

    st.stop()


# ============================================================
# 7. CREATE PERFORMANCE LEVEL
# ============================================================

def performance_level(score):

    if score < 60:

        return "Low"

    elif score < 75:

        return "Medium"

    else:

        return "High"


df["Performance_Level"] = (
    df["Exam_Score"]
    .apply(performance_level)
)


# ============================================================
# 8. REMOVE MISSING VALUES
# ============================================================

df = df.dropna().reset_index(drop=True)


# ============================================================
# 9. SIDEBAR
# ============================================================

st.sidebar.title("📚 Project Modules")

page = st.sidebar.radio(

    "Select Module",

    [
        "🏠 Dashboard",
        "👨‍🎓 Student Profile",
        "🔮 Performance Prediction",
        "📊 Algorithm Comparison",
        "👨‍🏫 Teacher Recommendation"
    ]

)


# ============================================================
# 10. PREPARE MACHINE LEARNING DATA
# ============================================================

X = df.drop(
    columns=[
        "Exam_Score",
        "Performance_Level"
    ]
)

y = df["Performance_Level"]


# ============================================================
# 11. IDENTIFY NUMERICAL AND CATEGORICAL FEATURES
# ============================================================

numerical_features = (
    X.select_dtypes(
        include=["int64", "float64"]
    )
    .columns
    .tolist()
)


categorical_features = (
    X.select_dtypes(
        include=["object"]
    )
    .columns
    .tolist()
)


# ============================================================
# 12. PREPROCESSING
# ============================================================

preprocessor = ColumnTransformer(

    transformers=[

        (
            "numerical",

            "passthrough",

            numerical_features
        ),

        (
            "categorical",

            OneHotEncoder(
                handle_unknown="ignore"
            ),

            categorical_features
        )

    ]

)


# ============================================================
# 13. TRAIN TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.20,

    random_state=42,

    stratify=y

)


# ============================================================
# 14. RANDOM FOREST MODEL
# ============================================================

rf_model = Pipeline(

    steps=[

        (
            "preprocessor",

            preprocessor
        ),

        (
            "classifier",

            RandomForestClassifier(

                n_estimators=100,

                random_state=42,

                class_weight="balanced"

            )

        )

    ]

)


# ============================================================
# 15. DECISION TREE MODEL
# ============================================================

dt_model = Pipeline(

    steps=[

        (
            "preprocessor",

            preprocessor
        ),

        (
            "classifier",

            DecisionTreeClassifier(

                random_state=42,

                class_weight="balanced"

            )

        )

    ]

)


# ============================================================
# 16. TRAIN RANDOM FOREST
# ============================================================

rf_model.fit(
    X_train,
    y_train
)


# ============================================================
# 17. TRAIN DECISION TREE
# ============================================================

dt_model.fit(
    X_train,
    y_train
)


# ============================================================
# 18. PREDICTIONS
# ============================================================

rf_prediction = rf_model.predict(
    X_test
)


dt_prediction = dt_model.predict(
    X_test
)


# ============================================================
# 19. MODEL EVALUATION
# ============================================================

rf_accuracy = accuracy_score(
    y_test,
    rf_prediction
)

rf_precision = precision_score(
    y_test,
    rf_prediction,
    average="weighted",
    zero_division=0
)

rf_recall = recall_score(
    y_test,
    rf_prediction,
    average="weighted",
    zero_division=0
)

rf_f1 = f1_score(
    y_test,
    rf_prediction,
    average="weighted",
    zero_division=0
)


dt_accuracy = accuracy_score(
    y_test,
    dt_prediction
)

dt_precision = precision_score(
    y_test,
    dt_prediction,
    average="weighted",
    zero_division=0
)

dt_recall = recall_score(
    y_test,
    dt_prediction,
    average="weighted",
    zero_division=0
)

dt_f1 = f1_score(
    y_test,
    dt_prediction,
    average="weighted",
    zero_division=0
)


# ============================================================
# 20. CONFUSION MATRICES
# ============================================================

class_names = [
    "Low",
    "Medium",
    "High"
]


rf_cm = confusion_matrix(
    y_test,
    rf_prediction,
    labels=class_names
)


dt_cm = confusion_matrix(
    y_test,
    dt_prediction,
    labels=class_names
)


# ============================================================
# 21. MODULE 1 - DASHBOARD
# ============================================================

if page == "🏠 Dashboard":

    st.header(
        "📊 Student Performance Dashboard"
    )

    st.write(
        "Overview of the student dataset and machine learning results."
    )


    # --------------------------------------------------------
    # METRICS
    # --------------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(
            "👨‍🎓 Total Students",
            len(df)
        )


    with col2:

        st.metric(
            "📊 Average Score",
            f"{df['Exam_Score'].mean():.2f}"
        )


    with col3:

        st.metric(
            "📅 Average Attendance",
            f"{df['Attendance'].mean():.2f}%"
        )


    with col4:

        st.metric(
            "📚 Average Study Hours",
            f"{df['Hours_Studied'].mean():.2f}"
        )


    st.divider()


    # --------------------------------------------------------
    # PERFORMANCE DISTRIBUTION
    # --------------------------------------------------------

    st.subheader(
        "📈 Student Performance Distribution"
    )


    performance_count = (
        df["Performance_Level"]
        .value_counts()
        .reindex(
            ["Low", "Medium", "High"],
            fill_value=0
        )
    )


    st.bar_chart(
        performance_count
    )


    st.divider()


    # --------------------------------------------------------
    # ALGORITHM SUMMARY
    # --------------------------------------------------------

    st.subheader(
        "🤖 Machine Learning Algorithm Summary"
    )


    summary_df = pd.DataFrame({

        "Metric": [
            "Accuracy",
            "Precision",
            "Recall",
            "F1 Score"
        ],

        "Random Forest": [
            rf_accuracy * 100,
            rf_precision * 100,
            rf_recall * 100,
            rf_f1 * 100
        ],

        "Decision Tree": [
            dt_accuracy * 100,
            dt_precision * 100,
            dt_recall * 100,
            dt_f1 * 100
        ]

    })


    summary_df.iloc[:, 1:] = (
        summary_df.iloc[:, 1:]
        .round(2)
    )


    st.dataframe(
        summary_df,
        use_container_width=True,
        hide_index=True
    )


    st.divider()


    # --------------------------------------------------------
    # DATASET
    # --------------------------------------------------------

    st.subheader(
        "📋 Dataset Preview"
    )


    st.dataframe(
        df.head(20),
        use_container_width=True
    )


# ============================================================
# MODULE 2 - STUDENT PROFILE
# ============================================================

elif page == "👨‍🎓 Student Profile":

    st.header(
        "👨‍🎓 Student Profile Analysis"
    )


    student_number = st.number_input(

        "Enter Student Number",

        min_value=1,

        max_value=len(df),

        value=1,

        step=1

    )


    student = df.iloc[
        student_number - 1
    ]


    st.divider()


    st.subheader(
        "📚 Academic Profile"
    )


    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "Exam Score",
            student["Exam_Score"]
        )

        st.metric(
            "Previous Score",
            student["Previous_Scores"]
        )

        st.metric(
            "Attendance",
            f"{student['Attendance']}%"
        )


    with col2:

        st.metric(
            "Hours Studied",
            student["Hours_Studied"]
        )

        st.metric(
            "Sleep Hours",
            student["Sleep_Hours"]
        )

        st.metric(
            "Tutoring Sessions",
            student["Tutoring_Sessions"]
        )


    with col3:

        st.metric(
            "Physical Activity",
            student["Physical_Activity"]
        )

        st.metric(
            "Performance",
            student["Performance_Level"]
        )

        st.metric(
            "School Type",
            student["School_Type"]
        )


    st.divider()


    st.subheader(
        "🧠 Learning and Behavioural Profile"
    )


    profile_columns = [

        "Motivation_Level",

        "Internet_Access",

        "Parental_Involvement",

        "Access_to_Resources",

        "Extracurricular_Activities",

        "Teacher_Quality",

        "Peer_Influence",

        "Learning_Disabilities"

    ]


    available_profile_columns = [

        column

        for column in profile_columns

        if column in df.columns

    ]


    profile_data = {}


    for column in available_profile_columns:

        profile_data[column] = student[column]


    profile_df = pd.DataFrame(

        profile_data.items(),

        columns=[
            "Feature",
            "Value"
        ]

    )


    st.table(
        profile_df
    )


    if student["Performance_Level"] == "High":

        st.success(
            "🟢 Student belongs to the HIGH performance group."
        )

    elif student["Performance_Level"] == "Medium":

        st.warning(
            "🟡 Student belongs to the MEDIUM performance group."
        )

    else:

        st.error(
            "🔴 Student belongs to the LOW performance group."
        )


# ============================================================
# MODULE 3 - PERFORMANCE PREDICTION
# ============================================================

elif page == "🔮 Performance Prediction":

    st.header(
        "🔮 Student Performance Prediction"
    )


    st.write(
        "Enter student characteristics and use Random Forest "
        "to predict the student's performance level."
    )


    st.info(
        f"🌲 Random Forest Accuracy: "
        f"{rf_accuracy * 100:.2f}%"
    )


    st.divider()


    # --------------------------------------------------------
    # CREATE INPUT FROM EXISTING STUDENT
    # --------------------------------------------------------

    st.subheader(
        "📝 Select an Existing Student"
    )


    student_number = st.number_input(

        "Student Number",

        min_value=1,

        max_value=len(df),

        value=1,

        step=1

    )


    selected_student = df.iloc[
        student_number - 1
    ]


    input_data = X.iloc[
        [student_number - 1]
    ]


    st.write(
        "Selected Student Information:"
    )


    st.dataframe(
        input_data,
        use_container_width=True
    )


    predict_button = st.button(

        "🔮 Predict Performance",

        type="primary"

    )


    if predict_button:

        prediction = rf_model.predict(
            input_data
        )[0]


        probabilities = rf_model.predict_proba(
            input_data
        )[0]


        confidence = (
            max(probabilities) * 100
        )


        st.divider()


        st.subheader(
            "🎯 Prediction Result"
        )


        if prediction == "High":

            st.success(
                f"🟢 Predicted Performance: {prediction}"
            )

        elif prediction == "Medium":

            st.warning(
                f"🟡 Predicted Performance: {prediction}"
            )

        else:

            st.error(
                f"🔴 Predicted Performance: {prediction}"
            )


        st.metric(
            "Model Confidence",
            f"{confidence:.2f}%"
        )


        probability_df = pd.DataFrame({

            "Performance Level":
            rf_model.classes_,

            "Probability (%)":
            probabilities * 100

        })


        probability_df[
            "Probability (%)"
        ] = (
            probability_df[
                "Probability (%)"
            ].round(2)
        )


        st.subheader(
            "📊 Prediction Probabilities"
        )


        st.dataframe(
            probability_df,

            use_container_width=True,

            hide_index=True

        )


        st.bar_chart(

            probability_df.set_index(
                "Performance Level"
            )

        )


# ============================================================
# MODULE 4 - ALGORITHM COMPARISON
# ============================================================

elif page == "📊 Algorithm Comparison":

    st.header(
        "📊 Random Forest vs Decision Tree"
    )


    st.write(
        "The proposed Random Forest algorithm is compared "
        "with Decision Tree using four evaluation metrics."
    )


    st.divider()


    # --------------------------------------------------------
    # COMPARISON TABLE
    # --------------------------------------------------------

    comparison_df = pd.DataFrame({

        "Metric": [
            "Accuracy",
            "Precision",
            "Recall",
            "F1 Score"
        ],

        "Random Forest": [
            rf_accuracy * 100,
            rf_precision * 100,
            rf_recall * 100,
            rf_f1 * 100
        ],

        "Decision Tree": [
            dt_accuracy * 100,
            dt_precision * 100,
            dt_recall * 100,
            dt_f1 * 100
        ]

    })


    comparison_df.iloc[:, 1:] = (

        comparison_df.iloc[:, 1:]

        .round(2)

    )


    st.subheader(
        "📈 Performance Comparison"
    )


    st.dataframe(

        comparison_df,

        use_container_width=True,

        hide_index=True

    )


    # --------------------------------------------------------
    # CHART
    # --------------------------------------------------------

    st.subheader(
        "📊 Algorithm Comparison Chart"
    )


    chart_df = comparison_df.set_index(
        "Metric"
    )


    st.bar_chart(
        chart_df
    )


    st.divider()


    # --------------------------------------------------------
    # METRICS
    # --------------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(
            "RF Accuracy",
            f"{rf_accuracy * 100:.2f}%"
        )


    with col2:

        st.metric(
            "RF Precision",
            f"{rf_precision * 100:.2f}%"
        )


    with col3:

        st.metric(
            "RF Recall",
            f"{rf_recall * 100:.2f}%"
        )


    with col4:

        st.metric(
            "RF F1 Score",
            f"{rf_f1 * 100:.2f}%"
        )


    st.divider()


    # --------------------------------------------------------
    # CONFUSION MATRICES
    # --------------------------------------------------------

    st.subheader(
        "🔲 Confusion Matrix Comparison"
    )


    col1, col2 = st.columns(2)


    with col1:

        st.write(
            "### 🌲 Random Forest"
        )


        fig1, ax1 = plt.subplots()


        ax1.imshow(
            rf_cm
        )


        ax1.set_title(
            "Random Forest Confusion Matrix"
        )


        ax1.set_xlabel(
            "Predicted"
        )


        ax1.set_ylabel(
            "Actual"
        )


        ax1.set_xticks(
            range(len(class_names))
        )


        ax1.set_yticks(
            range(len(class_names))
        )


        ax1.set_xticklabels(
            class_names
        )


        ax1.set_yticklabels(
            class_names
        )


        for i in range(
            len(class_names)
        ):

            for j in range(
                len(class_names)
            ):

                ax1.text(
                    j,
                    i,
                    rf_cm[i, j],
                    ha="center",
                    va="center"
                )


        st.pyplot(
            fig1
        )


    with col2:

        st.write(
            "### 🌳 Decision Tree"
        )


        fig2, ax2 = plt.subplots()


        ax2.imshow(
            dt_cm
        )


        ax2.set_title(
            "Decision Tree Confusion Matrix"
        )


        ax2.set_xlabel(
            "Predicted"
        )


        ax2.set_ylabel(
            "Actual"
        )


        ax2.set_xticks(
            range(len(class_names))
        )


        ax2.set_yticks(
            range(len(class_names))
        )


        ax2.set_xticklabels(
            class_names
        )


        ax2.set_yticklabels(
            class_names
        )


        for i in range(
            len(class_names)
        ):

            for j in range(
                len(class_names)
            ):

                ax2.text(
                    j,
                    i,
                    dt_cm[i, j],
                    ha="center",
                    va="center"
                )


        st.pyplot(
            fig2
        )


    st.divider()


    # --------------------------------------------------------
    # FINAL ALGORITHM
    # --------------------------------------------------------

    accuracy_difference = (

        rf_accuracy

        -

        dt_accuracy

    ) * 100


    if rf_accuracy > dt_accuracy:

        st.success(

            f"""
## 🏆 Random Forest Selected

Random Forest achieved:

**Accuracy:** {rf_accuracy * 100:.2f}%

**Precision:** {rf_precision * 100:.2f}%

**Recall:** {rf_recall * 100:.2f}%

**F1 Score:** {rf_f1 * 100:.2f}%

Decision Tree achieved:

**Accuracy:** {dt_accuracy * 100:.2f}%

**Precision:** {dt_precision * 100:.2f}%

**Recall:** {dt_recall * 100:.2f}%

**F1 Score:** {dt_f1 * 100:.2f}%

Therefore, Random Forest is selected as the proposed
algorithm because it provides better classification
performance than Decision Tree.

**Accuracy improvement: {accuracy_difference:.2f} percentage points**
"""

        )


    else:

        st.warning(
            "Decision Tree achieved better accuracy on this dataset."
        )


# ============================================================
# MODULE 5 - TEACHER RECOMMENDATION
# ============================================================

elif page == "👨‍🏫 Teacher Recommendation":

    st.header(
        "👨‍🏫 Teacher Recommendation System"
    )


    st.write(
        "The system recommends the most suitable teacher "
        "based on the student's performance and learning profile."
    )


    st.divider()


    # ========================================================
    # TEACHER DATASET
    # ========================================================

    teachers = pd.DataFrame({

        "Teacher": [

            "Dr. Arun",

            "Ms. Priya",

            "Mr. Rahul",

            "Dr. Kavitha",

            "Mr. Suresh",

            "Ms. Anitha",

            "Dr. Naveen",

            "Ms. Divya",

            "Mr. Karthik",

            "Dr. Meena"

        ],

        "Subject": [

            "Mathematics",

            "Science",

            "Computer Science",

            "Mathematics",

            "English",

            "Science",

            "Computer Science",

            "English",

            "Mathematics",

            "Science"

        ],

        "Teaching_Style": [

            "Interactive",

            "Practical",

            "Technology Based",

            "Interactive",

            "Discussion Based",

            "Practical",

            "Technology Based",

            "Discussion Based",

            "Visual",

            "Practical"

        ],

        "Experience": [

            12,

            8,

            10,

            15,

            7,

            11,

            13,

            6,

            9,

            14

        ],

        "Teacher_Quality": [

            "High",

            "High",

            "High",

            "High",

            "Medium",

            "High",

            "High",

            "Medium",

            "High",

            "High"

        ],

        "Specialization": [

            "Problem Solving",

            "Experiments",

            "Programming",

            "Problem Solving",

            "Communication",

            "Experiments",

            "Programming",

            "Communication",

            "Problem Solving",

            "Experiments"

        ]

    })


    # ========================================================
    # SHOW TEACHERS
    # ========================================================

    st.subheader(
        "👨‍🏫 Available Teachers"
    )


    st.dataframe(

        teachers,

        use_container_width=True,

        hide_index=True

    )


    st.divider()


    # ========================================================
    # STUDENT PROFILE INPUT
    # ========================================================

    st.subheader(
        "📝 Student Learning Profile"
    )


    col1, col2 = st.columns(2)


    with col1:

        performance = st.selectbox(

            "Performance Level",

            [
                "Low",
                "Medium",
                "High"
            ]

        )


        motivation = st.selectbox(

            "Motivation Level",

            [
                "Low",
                "Medium",
                "High"
            ]

        )


        teaching_style = st.selectbox(

            "Preferred Teaching Style",

            [
                "Interactive",
                "Practical",
                "Technology Based",
                "Discussion Based",
                "Visual"
            ]

        )


    with col2:

        subject = st.selectbox(

            "Preferred Subject",

            [
                "Mathematics",
                "Science",
                "Computer Science",
                "English"
            ]

        )


        required_quality = st.selectbox(

            "Required Teacher Quality",

            [
                "Medium",
                "High"
            ]

        )


    st.divider()


    # ========================================================
    # RECOMMEND
    # ========================================================

    recommend_button = st.button(

        "🏆 Recommend Best Teacher",

        type="primary"

    )


    if recommend_button:


        teacher_scores = []


        for index, teacher in teachers.iterrows():


            score = 0


            # ------------------------------------------------
            # SUBJECT MATCH
            # ------------------------------------------------

            if teacher["Subject"] == subject:

                score += 30


            # ------------------------------------------------
            # TEACHING STYLE
            # ------------------------------------------------

            if teacher["Teaching_Style"] == teaching_style:

                score += 25


            # ------------------------------------------------
            # QUALITY
            # ------------------------------------------------

            if teacher["Teacher_Quality"] == required_quality:

                score += 20


            # ------------------------------------------------
            # PERFORMANCE MATCH
            # ------------------------------------------------

            if performance == "Low":

                if teacher["Teaching_Style"] in [

                    "Interactive",

                    "Practical",

                    "Discussion Based"

                ]:

                    score += 10


            elif performance == "Medium":

                if teacher["Teaching_Style"] in [

                    "Interactive",

                    "Visual",

                    "Practical"

                ]:

                    score += 10


            else:

                if teacher["Teaching_Style"] in [

                    "Technology Based",

                    "Visual",

                    "Interactive"

                ]:

                    score += 10


            # ------------------------------------------------
            # EXPERIENCE
            # ------------------------------------------------

            if teacher["Experience"] >= 10:

                score += 10

            else:

                score += 5


            teacher_scores.append(
                score
            )


        # ----------------------------------------------------
        # SCORE
        # ----------------------------------------------------

        teachers["Match_Score"] = teacher_scores


        max_score = teachers[
            "Match_Score"
        ].max()


        teachers["Compatibility"] = (

            teachers["Match_Score"]

            /

            max_score

            *

            100

        ).round(2)


        # ----------------------------------------------------
        # SORT
        # ----------------------------------------------------

        recommendations = teachers.sort_values(

            "Match_Score",

            ascending=False

        )


        best_teacher = recommendations.iloc[0]


        # ====================================================
        # RESULT
        # ====================================================

        st.divider()


        st.subheader(
            "🏆 Recommended Teacher"
        )


        st.success(

            f"""
## 👨‍🏫 {best_teacher["Teacher"]}

**Subject:** {best_teacher["Subject"]}

**Teaching Style:** {best_teacher["Teaching_Style"]}

**Experience:** {best_teacher["Experience"]} years

**Teacher Quality:** {best_teacher["Teacher_Quality"]}

**Specialization:** {best_teacher["Specialization"]}

### ⭐ Compatibility Score: {best_teacher["Compatibility"]}%
"""

        )


        st.divider()


        # ====================================================
        # TOP 5
        # ====================================================

        st.subheader(
            "🥇 Top Teacher Recommendations"
        )


        top_teachers = recommendations[

            [
                "Teacher",

                "Subject",

                "Teaching_Style",

                "Experience",

                "Teacher_Quality",

                "Compatibility"

            ]

        ].head(5)


        st.dataframe(

            top_teachers,

            use_container_width=True,

            hide_index=True

        )


        # ====================================================
        # CHART
        # ====================================================

        st.subheader(
            "📊 Teacher Compatibility"
        )


        chart = (

            top_teachers

            .set_index("Teacher")

            ["Compatibility"]

        )


        st.bar_chart(
            chart
        )


        st.info(

            f"""
### 💡 Recommendation Explanation

**{best_teacher["Teacher"]}** was selected because
this teacher achieved the highest compatibility score
with the selected student profile.

The recommendation considers:

• Subject compatibility

• Teaching style

• Teacher quality

• Student performance level

• Teacher experience

The teacher with the highest matching score is recommended.
"""

        )


# ============================================================
# FOOTER
# ============================================================

st.sidebar.divider()

st.sidebar.info(

    """
🎓 **Capstone Project**

Profile-Based Student Performance Analysis
and Teacher Recommendation System Using Data Mining

Primary Algorithm:
Random Forest

Comparison Algorithm:
Decision Tree

Dashboard:
Streamlit
"""

)