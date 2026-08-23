import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer

from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)


# ============================================================
# 1. LOAD DATASET
# ============================================================

file_path = r"C:\Users\HP\OneDrive\Documents\StudentPerformanceFactors.csv.xlsx"

df = pd.read_excel(file_path)

print("\n==============================================")
print("DATASET LOADED")
print("==============================================")

print("Dataset shape:", df.shape)


# ============================================================
# 2. CREATE BALANCED PERFORMANCE LEVEL
# ============================================================

# Divide students into three approximately equal groups
# based on their Exam_Score distribution.

df["Performance_Level"] = pd.qcut(
    df["Exam_Score"],
    q=3,
    labels=["Low", "Medium", "High"]
)


print("\n==============================================")
print("PERFORMANCE LEVEL DISTRIBUTION")
print("==============================================")

print(
    df["Performance_Level"].value_counts()
)

print("\nPerformance percentages:")

print(
    df["Performance_Level"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)


print("\n==============================================")
print("PERFORMANCE LEVEL DISTRIBUTION")
print("==============================================")

print(df["Performance_Level"].value_counts())


# ============================================================
# 3. REMOVE TARGET SOURCE FROM FEATURES
# ============================================================

# Exam_Score is used only to create Performance_Level.
# It must NOT be used as an input feature.

X = df.drop(
    columns=["Exam_Score", "Performance_Level"]
)

y = df["Performance_Level"]


# ============================================================
# 4. IDENTIFY NUMERICAL AND CATEGORICAL FEATURES
# ============================================================

numeric_features = X.select_dtypes(
    include=["int64", "float64"]
).columns.tolist()

categorical_features = X.select_dtypes(
    include=["object"]
).columns.tolist()


print("\n==============================================")
print("NUMERICAL FEATURES")
print("==============================================")

print(numeric_features)


print("\n==============================================")
print("CATEGORICAL FEATURES")
print("==============================================")

print(categorical_features)


# ============================================================
# 5. NUMERICAL PREPROCESSING
# ============================================================

numeric_transformer = Pipeline(
    steps=[
        (
            "imputer",
            SimpleImputer(strategy="median")
        )
    ]
)


# ============================================================
# 6. CATEGORICAL PREPROCESSING
# ============================================================

categorical_transformer = Pipeline(
    steps=[
        (
            "imputer",
            SimpleImputer(strategy="most_frequent")
        ),
        (
            "encoder",
            OneHotEncoder(
                handle_unknown="ignore"
            )
        )
    ]
)


# ============================================================
# 7. COMBINE PREPROCESSING
# ============================================================

preprocessor = ColumnTransformer(
    transformers=[
        (
            "num",
            numeric_transformer,
            numeric_features
        ),
        (
            "cat",
            categorical_transformer,
            categorical_features
        )
    ]
)


# ============================================================
# 8. TRAIN / TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


print("\n==============================================")
print("TRAIN / TEST DATA")
print("==============================================")

print("Training samples:", X_train.shape[0])
print("Testing samples :", X_test.shape[0])


# ============================================================
# 9. RANDOM FOREST MODEL
# ============================================================

random_forest = Pipeline(
    steps=[
        (
            "preprocessor",
            preprocessor
        ),
        (
            "model",
            RandomForestClassifier(
                n_estimators=200,
                random_state=42,
                class_weight="balanced"
            )
        )
    ]
)


# ============================================================
# 10. DECISION TREE MODEL
# ============================================================

decision_tree = Pipeline(
    steps=[
        (
            "preprocessor",
            preprocessor
        ),
        (
            "model",
            DecisionTreeClassifier(
                random_state=42,
                class_weight="balanced"
            )
        )
    ]
)


# ============================================================
# 11. TRAIN RANDOM FOREST
# ============================================================

print("\n==============================================")
print("TRAINING RANDOM FOREST")
print("==============================================")

random_forest.fit(X_train, y_train)

rf_prediction = random_forest.predict(X_test)


# ============================================================
# 12. TRAIN DECISION TREE
# ============================================================

print("\n==============================================")
print("TRAINING DECISION TREE")
print("==============================================")

decision_tree.fit(X_train, y_train)

dt_prediction = decision_tree.predict(X_test)


# ============================================================
# 13. RANDOM FOREST EVALUATION
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


# ============================================================
# 14. DECISION TREE EVALUATION
# ============================================================

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
# 15. DISPLAY COMPARISON
# ============================================================

print("\n\n======================================================")
print("       RANDOM FOREST VS DECISION TREE")
print("======================================================")

print(
    f"{'Metric':<15}"
    f"{'Random Forest':<20}"
    f"{'Decision Tree':<20}"
)

print("-" * 55)

print(
    f"{'Accuracy':<15}"
    f"{rf_accuracy:<20.4f}"
    f"{dt_accuracy:<20.4f}"
)

print(
    f"{'Precision':<15}"
    f"{rf_precision:<20.4f}"
    f"{dt_precision:<20.4f}"
)

print(
    f"{'Recall':<15}"
    f"{rf_recall:<20.4f}"
    f"{dt_recall:<20.4f}"
)

print(
    f"{'F1 Score':<15}"
    f"{rf_f1:<20.4f}"
    f"{dt_f1:<20.4f}"
)


# ============================================================
# 16. CLASSIFICATION REPORT
# ============================================================

print("\n\n==============================================")
print("RANDOM FOREST CLASSIFICATION REPORT")
print("==============================================")

print(
    classification_report(
        y_test,
        rf_prediction,
        zero_division=0
    )
)


print("\n==============================================")
print("DECISION TREE CLASSIFICATION REPORT")
print("==============================================")

print(
    classification_report(
        y_test,
        dt_prediction,
        zero_division=0
    )
)


# ============================================================
# 17. CONFUSION MATRICES
# ============================================================

print("\n==============================================")
print("RANDOM FOREST CONFUSION MATRIX")
print("==============================================")

print(
    confusion_matrix(
        y_test,
        rf_prediction
    )
)


print("\n==============================================")
print("DECISION TREE CONFUSION MATRIX")
print("==============================================")

print(
    confusion_matrix(
        y_test,
        dt_prediction
    )
)


# ============================================================
# 18. SELECT BEST ALGORITHM
# ============================================================

print("\n\n==============================================")
print("FINAL ALGORITHM COMPARISON")
print("==============================================")


if rf_f1 > dt_f1:

    print("🏆 BEST ALGORITHM: RANDOM FOREST")
    print(
        "Random Forest achieved the higher F1-score."
    )

elif dt_f1 > rf_f1:

    print("🏆 BEST ALGORITHM: DECISION TREE")
    print(
        "Decision Tree achieved the higher F1-score."
    )

else:

    print("🤝 BOTH ALGORITHMS HAVE THE SAME F1-SCORE")


print("\nModel comparison completed successfully!")