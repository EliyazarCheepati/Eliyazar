import matplotlib.pyplot as plt
import numpy as np


# ============================================================
# RANDOM FOREST CONFUSION MATRIX
# ============================================================

random_forest_cm = np.array([
    [274, 9, 42],
    [0, 519, 58],
    [45, 63, 312]
])

classes = ["High", "Low", "Medium"]


plt.figure(figsize=(7, 6))

plt.imshow(random_forest_cm)

plt.title("Random Forest Confusion Matrix")
plt.xlabel("Predicted Class")
plt.ylabel("Actual Class")

plt.xticks(
    range(len(classes)),
    classes
)

plt.yticks(
    range(len(classes)),
    classes
)

# Display numbers inside the matrix
for i in range(len(classes)):
    for j in range(len(classes)):
        plt.text(
            j,
            i,
            random_forest_cm[i, j],
            ha="center",
            va="center",
            fontsize=14
        )

plt.colorbar(label="Number of Students")

plt.tight_layout()

plt.savefig(
    "random_forest_confusion_matrix.png",
    dpi=300
)

plt.show()


# ============================================================
# DECISION TREE CONFUSION MATRIX
# ============================================================

decision_tree_cm = np.array([
    [228, 12, 85],
    [18, 445, 114],
    [66, 114, 240]
])


plt.figure(figsize=(7, 6))

plt.imshow(decision_tree_cm)

plt.title("Decision Tree Confusion Matrix")
plt.xlabel("Predicted Class")
plt.ylabel("Actual Class")

plt.xticks(
    range(len(classes)),
    classes
)

plt.yticks(
    range(len(classes)),
    classes
)

# Display numbers inside the matrix
for i in range(len(classes)):
    for j in range(len(classes)):
        plt.text(
            j,
            i,
            decision_tree_cm[i, j],
            ha="center",
            va="center",
            fontsize=14
        )

plt.colorbar(label="Number of Students")

plt.tight_layout()

plt.savefig(
    "decision_tree_confusion_matrix.png",
    dpi=300
)

plt.show()


print("==========================================")
print("CONFUSION MATRICES CREATED SUCCESSFULLY")
print("==========================================")

print("Random Forest:")
print("random_forest_confusion_matrix.png")

print()

print("Decision Tree:")
print("decision_tree_confusion_matrix.png")