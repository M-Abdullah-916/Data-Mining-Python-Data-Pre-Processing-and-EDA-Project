import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

# Importing File and Sheets from the given Dataset
dataset = pd.ExcelFile('Dataset1(7 sheets).xlsx', engine='openpyxl')
# We don't need Row 2,3 and 4 because it adds nothing to our data.
D1 = pd.read_excel(dataset, sheet_name="D1", skiprows=(2, 3, 4))
D2 = pd.read_excel(dataset, sheet_name="D2", skiprows=(2, 3, 4))
D3 = pd.read_excel(dataset, sheet_name="D3", skiprows=(2, 3, 4))
D4 = pd.read_excel(dataset, sheet_name="D4", skiprows=(2, 3, 4))
D5 = pd.read_excel(dataset, sheet_name="D5", skiprows=(2, 3, 4))
D6 = pd.read_excel(dataset, sheet_name="D6", skiprows=(2, 3, 4))
D7 = pd.read_excel(dataset, sheet_name="D7", skiprows=(2, 3, 4))

# Checking for Duplication
print("Total Duplications in D1 Sheet")
print(D1.nunique())
print("Total Duplications in D2 Sheet")
print(D2.nunique())
print("Total Duplications in D3 Sheet")
print(D3.nunique())
print("Total Duplications in D4 Sheet")
print(D4.nunique())
print("Total Duplications in D5 Sheet")
print(D5.nunique())
print("Total Duplications in D6 Sheet")
print(D6.nunique())
print("Total Duplications in D7 Sheet")
print(D7.nunique())

# Checking Null Values
print("-----------------------------------------------------------------------------------------")
print("Total Null Values in D1 Sheet")
print(D1.isnull().sum())
print("Total Null Values in D2 Sheet")
print(D2.isnull().sum())
print("Total Null Values in D3 Sheet")
print(D3.isnull().sum())
print("Total Null Values in D4 Sheet")
print(D4.isnull().sum())
print("Total Null Values in D5 Sheet")
print(D5.isnull().sum())
print("Total Null Values in D6 Sheet")
print(D6.isnull().sum())
print("Total Null Values in D7 Sheet")
print(D7.isnull().sum())

# Displaying Null Values using Heatmap
print("-----------------------------------------------------------------------------------------")
sns.heatmap(D1.isnull(), cbar=False, cmap='viridis')
plt.title("D1 Null Values")
plt.show()
sns.heatmap(D2.isnull(), cbar=False, cmap='viridis')
plt.title("D2 Null Values")
plt.show()
sns.heatmap(D3.isnull(), cbar=False, cmap='viridis')
plt.title("D3 Null Values")
plt.show()
sns.heatmap(D4.isnull(), cbar=False, cmap='viridis')
plt.title("D4 Null Values")
plt.show()
sns.heatmap(D5.isnull(), cbar=False, cmap='viridis')
plt.title("D5 Null Values")
plt.show()
sns.heatmap(D6.isnull(), cbar=False, cmap='viridis')
plt.title("D6 Null Values")
plt.show()
sns.heatmap(D7.isnull(), cbar=False, cmap='viridis')
plt.title("D7 Null Values")
plt.show()

# Replacing missing values with Median of the corresponding column
print("-----------------------------------------------------------------------------------------")
num_col_D1 = ['As:1', 'As:2', 'As:3', 'As:4', 'As:5', 'As:6', 'As', 'Qz:1', 'Qz:2', 'Qz:3', 'Qz:4', 'Qz:4', 'Qz:5',
              'Qz:6', 'Qz:7', 'Qz', 'S-I', 'S-II']
for col in num_col_D1:
    D1[col] = pd.to_numeric(D1[col])
    D1[col].fillna(D1[col].median(), inplace=True)
grades_mode = D1.Grade.mode()
D1.Grade.fillna(grades_mode, inplace=True)

num_col_D2 = ['As:1', 'As:2', 'As:3', 'As:4', 'As:5', 'As:6', 'As', 'Qz:1', 'Qz:2', 'Qz:3', 'Qz:4', 'Qz:4', 'Qz:5',
              'Qz:6', 'Qz', 'S-I', 'S-II']
for col in num_col_D2:
    D2[col] = pd.to_numeric(D2[col])
    D2[col].fillna(D2[col].median(), inplace=True)
grades_mode = D2.Grade.mode()
D2.Grade.fillna(grades_mode, inplace=True)

num_col_D3 = ['As:1', 'As:2', 'As:3', 'As:4', 'As:5', 'As:6', 'As', 'Qz:1', 'Qz:2', 'Qz:3', 'Qz:4', 'Qz:4', 'Qz:5',
              'Qz:6', 'Qz:7', 'Qz:8', 'Qz', 'S-I', 'S-II']
for col in num_col_D3:
    D3[col] = pd.to_numeric(D3[col])
    D3[col].fillna(D3[col].median(), inplace=True)
grades_mode = D3.Grade.mode()
D3.Grade.fillna(grades_mode, inplace=True)

num_col_D4 = ['As:1', 'As:2', 'As:3', 'As:4', 'As:5', 'As:6', 'As:7', 'As', 'Qz:1', 'Qz:2', 'Qz:3', 'Qz:4', 'Qz:4',
              'Qz:5', 'Qz', 'S-I', 'S-II']
for col in num_col_D4:
    D4[col] = pd.to_numeric(D4[col])
    D4[col].fillna(D4[col].median(), inplace=True)
grades_mode = D4.Grade.mode()
D4.Grade.fillna(grades_mode, inplace=True)

num_col_D5 = ['As:1', 'As:2', 'As:3', 'As:4', 'As:5', 'As:6', 'As', 'Qz:1', 'Qz:2', 'Qz:3', 'Qz:4', 'Qz:4', 'Qz:5',
              'Qz:6', 'Qz:7', 'Qz:8', 'Qz', 'S-I', 'S-II']
for col in num_col_D5:
    D5[col] = pd.to_numeric(D5[col])
    D5[col].fillna(D5[col].median(), inplace=True)
grades_mode = D5.Grade.mode()
D5.Grade.fillna(grades_mode, inplace=True)

num_col_D6 = ['As:1', 'As:2', 'As:3', 'As:4', 'As:5', 'As:6', 'As', 'Qz:1', 'Qz:2', 'Qz:3', 'Qz:4', 'Qz:4', 'Qz:5',
              'Qz:6', 'Qz:7', 'Qz', 'S-I', 'S-II']
for col in num_col_D6:
    D6[col] = pd.to_numeric(D6[col])
    D6[col].fillna(D6[col].median(), inplace=True)
grades_mode = D6.Grade.mode()
D6.Grade.fillna(grades_mode, inplace=True)

num_col_D7 = ['As:1', 'As:2', 'As:3', 'As:4', 'As:5', 'As:6', 'As', 'Qz:1', 'Qz:2', 'Qz:3', 'Qz:4', 'Qz:4', 'Qz:5',
              'Qz:6', 'Qz:7', 'Qz:8', 'Qz', 'S-I', 'S-II']
for col in num_col_D7:
    D7[col] = pd.to_numeric(D7[col])
    D7[col].fillna(D7[col].median(), inplace=True)
grades_mode = D7.Grade.mode()
D7.Grade.fillna(grades_mode, inplace=True)

# Performing Data-Reduction Techniques
#   Removing 1st Column from data as it only contains serial number that is not helpful for us
print("-----------------------------------------------------------------------------------------")
D1 = D1.drop(columns=D1.columns[0])
D2 = D2.drop(columns=D2.columns[0])
D3 = D3.drop(columns=D3.columns[0])
D4 = D4.drop(columns=D4.columns[0])
D5 = D5.drop(columns=D5.columns[0])
D6 = D6.drop(columns=D6.columns[0])
D7 = D7.drop(columns=D7.columns[0])

# Data Cleared. Now proceeding to Checking Correlation of attributes.
print("-----------------------------------------------------------------------------------------")
plt.figure(figsize=(13, 13))
sns.heatmap(D1[['As:1', 'As:2', 'As:3', 'As:4', 'As:5', 'As:6', 'As', 'Qz:1', 'Qz:2', 'Qz:3', 'Qz:4', 'Qz:4', 'Qz:5',
                'Qz:6', 'Qz:7', 'Qz', 'S-I', 'S-II']].corr(), cbar=True, annot=True, cmap='Blues')
plt.title("D1 Correlation Matrix")
plt.show()

plt.figure(figsize=(13, 13))
sns.heatmap(D2[['As:1', 'As:2', 'As:3', 'As:4', 'As:5', 'As:6', 'As', 'Qz:1', 'Qz:2', 'Qz:3', 'Qz:4', 'Qz:4', 'Qz:5',
                'Qz:6', 'Qz', 'S-I', 'S-II']].corr(), cbar=True, annot=True, cmap='Blues')
plt.title("D2 Correlation Matrix")
plt.show()

plt.figure(figsize=(13, 13))
sns.heatmap(D3[['As:1', 'As:2', 'As:3', 'As:4', 'As:5', 'As:6', 'As', 'Qz:1', 'Qz:2', 'Qz:3', 'Qz:4', 'Qz:4', 'Qz:5',
                'Qz:6', 'Qz:7', 'Qz:8', 'Qz', 'S-I', 'S-II']].corr(), cbar=True, annot=True, cmap='Blues')
plt.title("D3 Correlation Matrix")
plt.show()

plt.figure(figsize=(13, 13))
sns.heatmap(D4[['As:1', 'As:2', 'As:3', 'As:4', 'As:5', 'As:6', 'As:7', 'As', 'Qz:1', 'Qz:2', 'Qz:3', 'Qz:4', 'Qz:4',
                'Qz:5', 'Qz', 'S-I', 'S-II']].corr(), cbar=True, annot=True, cmap='Blues')
plt.title("D4 Correlation Matrix")
plt.show()

plt.figure(figsize=(13, 13))
sns.heatmap(D5[['As:1', 'As:2', 'As:3', 'As:4', 'As:5', 'As:6', 'As', 'Qz:1', 'Qz:2', 'Qz:3', 'Qz:4', 'Qz:4', 'Qz:5',
                'Qz:6', 'Qz:7', 'Qz:8', 'Qz', 'S-I', 'S-II']].corr(), cbar=True, annot=True, cmap='Blues')
plt.title("D5 Correlation Matrix")
plt.show()

plt.figure(figsize=(13, 13))
sns.heatmap(D6[['As:1', 'As:2', 'As:3', 'As:4', 'As:5', 'As:6', 'As', 'Qz:1', 'Qz:2', 'Qz:3', 'Qz:4', 'Qz:4', 'Qz:5',
                'Qz:6', 'Qz:7', 'Qz', 'S-I', 'S-II']].corr(), cbar=True, annot=True, cmap='Blues')
plt.title("D6 Correlation Matrix")
plt.show()

plt.figure(figsize=(13, 13))
sns.heatmap(D7[['As:1', 'As:2', 'As:3', 'As:4', 'As:5', 'As:6', 'As', 'Qz:1', 'Qz:2', 'Qz:3', 'Qz:4', 'Qz:4', 'Qz:5',
                'Qz:6', 'Qz:7', 'Qz:8', 'Qz', 'S-I', 'S-II']].corr(), cbar=True, annot=True, cmap='Blues')
plt.title("D7 Correlation Matrix")
plt.show()

# Showing the relation between assignments weightage and Grades
print("-----------------------------------------------------------------------------------------")
D1.groupby('Grade')['As'].mean().plot.bar()
plt.title("Grade vs Assignment")
plt.show()

# Showing the relation between quizzes weightage and Grades
D1.groupby('Grade')['Qz'].mean().plot.bar()
plt.title("Grade vs Quizzes")
plt.show()

# Showing the relation between S-I weightage and Grades
D1.groupby('Grade')['S-I'].mean().plot.bar()
plt.title("Grade vs S-I")
plt.show()

# Showing the relation between S-II weightage and Grades
D1.groupby('Grade')['S-II'].mean().plot.bar()
plt.title("Grade vs S-II")
plt.show()

# Same can be done for D2 to D7 for further analysis

# Performing  EDA on D1
# Selecting only Numerical Values
print("-----------------------------------------------------------------------------------------")
num_cols = D1.select_dtypes(include=np.number).columns.tolist()
for col in num_cols:
    print(col)
    print('Skew :', round(D1[col].skew(), 2))
    plt.figure(figsize=(15, 4))
    plt.subplot(1, 2, 1)
    D1[col].hist(grid=False)
    plt.ylabel('Count')
    plt.subplot(1, 2, 2)
    sns.boxplot(x=D1[col])
    plt.show()
# Same can be done for D2 to D7 for further analysis

# -----------------------------------PART 2 OF DM PROJECT-----------------------------------
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB

print("-----------------------------------------------------------------------------------------")
X_D1 = D1[['As:1', 'As:2', 'As:3', 'As:4', 'As:5', 'As:6', 'As', 'Qz:1', 'Qz:2', 'Qz:3', 'Qz:4', 'Qz:4', 'Qz:5', 'Qz:6',
           'Qz:7', 'Qz', 'S-I', 'S-II']]
Y_D1 = D1['Grade']

X_D1_train, X_D1_test, Y_D1_train, Y_D1_test = train_test_split(X_D1, Y_D1, test_size=0.2)

# Standardizing the D1 Values
D1_Scaler = StandardScaler()
X_D1_train = D1_Scaler.fit_transform(X_D1_train)
X_D1_test = D1_Scaler.transform(X_D1_test)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_D1_train, Y_D1_train)
clf = DecisionTreeClassifier(criterion="entropy", max_depth=3)
clf = clf.fit(X_D1_train, Y_D1_train)
nb = classifier = GaussianNB()
classifier.fit(X_D1_train, Y_D1_train)

Y_D1_Prediction_KNN = knn.predict(X_D1_test)
D1_Accuracy_KNN = accuracy_score(Y_D1_test, Y_D1_Prediction_KNN)
D1_Confusion_Matrix_KNN = confusion_matrix(Y_D1_test, Y_D1_Prediction_KNN)
D1_Precision_KNN = precision_score(Y_D1_test, Y_D1_Prediction_KNN, pos_label="Pass")
D1_Recall_KNN = recall_score(Y_D1_test, Y_D1_Prediction_KNN, pos_label="Pass")

Y_D1_Prediction_Decision = clf.predict(X_D1_test)
D1_Accuracy_Decision = accuracy_score(Y_D1_test, Y_D1_Prediction_Decision)
D1_Precision_Decision = precision_score(Y_D1_test, Y_D1_Prediction_Decision, pos_label="Pass")
D1_Recall_Decision = recall_score(Y_D1_test, Y_D1_Prediction_Decision, pos_label="Pass")

Y_D1_Prediction_Naive_Bayes = nb.predict(X_D1_test)
D1_Accuracy_Naive_Bayes = accuracy_score(Y_D1_test, Y_D1_Prediction_Naive_Bayes)
D1_Precision_Naive_Bayes = precision_score(Y_D1_test, Y_D1_Prediction_Naive_Bayes, pos_label="Pass")
D1_Recall_Naive_Bayes = recall_score(Y_D1_test, Y_D1_Prediction_Naive_Bayes, pos_label="Pass")


print("D1 Confusion Matrix:")
print(D1_Confusion_Matrix_KNN)
print("D1 Accuracy KNN:", D1_Accuracy_KNN*100)
print("D1 Precision KNN:", D1_Precision_KNN*100)
print("D1 Recall KNN:", D1_Recall_KNN*100)
print("D1 Accuracy Decision Tree:", D1_Accuracy_Decision*100)
print("D1 Precision Decision Tree:", D1_Precision_Decision*100)
print("D1 Recall Decision Tree:", D1_Recall_Decision*100)
print("D1 Accuracy Naive Bayes:", D1_Accuracy_Naive_Bayes*100)
print("D1 Precision Naive Bayes:", D1_Precision_Naive_Bayes*100)
print("D1 Recall Naive Bayes:", D1_Recall_Naive_Bayes*100)

print("-----------------------------------------------------------------------------------------")
X_D2 = D2[['As:1', 'As:2', 'As:3', 'As:4', 'As:5', 'As:6', 'As', 'Qz:1', 'Qz:2', 'Qz:3', 'Qz:4', 'Qz:4', 'Qz:5', 'Qz:6',
           'Qz', 'S-I', 'S-II']]
Y_D2 = D2['Grade']

X_D2_train, X_D2_test, Y_D2_train, Y_D2_test = train_test_split(X_D2, Y_D2, test_size=0.2)

# Standardizing the D1 Values
D2_Scaler = StandardScaler()
X_D2_train = D2_Scaler.fit_transform(X_D2_train)
X_D2_test = D2_Scaler.transform(X_D2_test)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_D2_train, Y_D2_train)
clf = DecisionTreeClassifier(criterion="entropy", max_depth=3)
clf = clf.fit(X_D2_train, Y_D2_train)
nb = classifier = GaussianNB()
classifier.fit(X_D2_train, Y_D2_train)

Y_D2_Prediction_KNN = knn.predict(X_D2_test)
D2_Accuracy_KNN = accuracy_score(Y_D2_test, Y_D2_Prediction_KNN)
D2_Confusion_Matrix_KNN = confusion_matrix(Y_D2_test, Y_D2_Prediction_KNN)
D2_Precision_KNN = precision_score(Y_D2_test, Y_D2_Prediction_KNN, pos_label="Pass")
D2_Recall_KNN = recall_score(Y_D2_test, Y_D2_Prediction_KNN, pos_label="Pass")

Y_D2_Prediction_Decision = clf.predict(X_D2_test)
D2_Accuracy_Decision = accuracy_score(Y_D2_test, Y_D2_Prediction_Decision)
D2_Precision_Decision = precision_score(Y_D2_test, Y_D2_Prediction_Decision, pos_label="Pass")
D2_Recall_Decision = recall_score(Y_D2_test, Y_D2_Prediction_Decision, pos_label="Pass")

Y_D2_Prediction_Naive_Bayes = nb.predict(X_D2_test)
D2_Accuracy_Naive_Bayes = accuracy_score(Y_D2_test, Y_D2_Prediction_Naive_Bayes)
D2_Precision_Naive_Bayes = precision_score(Y_D2_test, Y_D2_Prediction_Naive_Bayes, pos_label="Pass")
D2_Recall_Naive_Bayes = recall_score(Y_D2_test, Y_D2_Prediction_Naive_Bayes, pos_label="Pass")


print("D2 Confusion Matrix:")
print(D2_Confusion_Matrix_KNN)
print("D2 Accuracy KNN:", D2_Accuracy_KNN*100)
print("D2 Precision KNN:", D2_Precision_KNN*100)
print("D2 Recall KNN:", D2_Recall_KNN*100)
print("D2 Accuracy Decision Tree:", D2_Accuracy_Decision*100)
print("D2 Precision Decision Tree:", D2_Precision_Decision*100)
print("D2 Recall Decision Tree:", D2_Recall_Decision*100)
print("D2 Accuracy Naive Bayes:", D2_Accuracy_Naive_Bayes*100)
print("D2 Precision Naive Bayes:", D2_Precision_Naive_Bayes*100)
print("D2 Recall Naive Bayes:", D2_Recall_Naive_Bayes*100)

print("-----------------------------------------------------------------------------------------")
X_D3 = D3[['As:1', 'As:2', 'As:3', 'As:4', 'As:5', 'As:6', 'As', 'Qz:1', 'Qz:2', 'Qz:3', 'Qz:4', 'Qz:4', 'Qz:5', 'Qz:6',
           'Qz:7', 'Qz:8', 'Qz', 'S-I', 'S-II']]
Y_D3 = D3['Grade']

X_D3_train, X_D3_test, Y_D3_train, Y_D3_test = train_test_split(X_D3, Y_D3, test_size=0.2)

# Standardizing the D1 Values
D3_Scaler = StandardScaler()
X_D3_train = D3_Scaler.fit_transform(X_D3_train)
X_D3_test = D3_Scaler.transform(X_D3_test)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_D3_train, Y_D3_train)
clf = DecisionTreeClassifier(criterion="entropy", max_depth=3)
clf = clf.fit(X_D3_train, Y_D3_train)
nb = classifier = GaussianNB()
classifier.fit(X_D3_train, Y_D3_train)

Y_D3_Prediction_KNN = knn.predict(X_D3_test)
D3_Accuracy_KNN = accuracy_score(Y_D3_test, Y_D3_Prediction_KNN)
D3_Confusion_Matrix_KNN = confusion_matrix(Y_D3_test, Y_D3_Prediction_KNN)
D3_Precision_KNN = precision_score(Y_D3_test, Y_D3_Prediction_KNN, pos_label="Pass")
D3_Recall_KNN = recall_score(Y_D3_test, Y_D3_Prediction_KNN, pos_label="Pass")

Y_D3_Prediction_Decision = clf.predict(X_D3_test)
D3_Accuracy_Decision = accuracy_score(Y_D3_test, Y_D3_Prediction_Decision)
D3_Precision_Decision = precision_score(Y_D3_test, Y_D3_Prediction_Decision, pos_label="Pass")
D3_Recall_Decision = recall_score(Y_D3_test, Y_D3_Prediction_Decision, pos_label="Pass")

Y_D3_Prediction_Naive_Bayes = nb.predict(X_D3_test)
D3_Accuracy_Naive_Bayes = accuracy_score(Y_D3_test, Y_D3_Prediction_Naive_Bayes)
D3_Precision_Naive_Bayes = precision_score(Y_D3_test, Y_D3_Prediction_Naive_Bayes, pos_label="Pass")
D3_Recall_Naive_Bayes = recall_score(Y_D3_test, Y_D3_Prediction_Naive_Bayes, pos_label="Pass")


print("D3 Confusion Matrix:")
print(D3_Confusion_Matrix_KNN)
print("D3 Accuracy KNN:", D3_Accuracy_KNN*100)
print("D3 Precision KNN:", D3_Precision_KNN*100)
print("D3 Recall KNN:", D3_Recall_KNN*100)
print("D3 Accuracy Decision Tree:", D3_Accuracy_Decision*100)
print("D3 Precision Decision Tree:", D3_Precision_Decision*100)
print("D3 Recall Decision Tree:", D3_Recall_Decision*100)
print("D3 Accuracy Naive Bayes:", D3_Accuracy_Naive_Bayes*100)
print("D3 Precision Naive Bayes:", D3_Precision_Naive_Bayes*100)
print("D3 Recall Naive Bayes:", D3_Recall_Naive_Bayes*100)

print("-----------------------------------------------------------------------------------------")
X_D4 = D4[['As:1', 'As:2', 'As:3', 'As:4', 'As:5', 'As:6', 'As:7', 'As', 'Qz:1', 'Qz:2', 'Qz:3', 'Qz:4', 'Qz:4', 'Qz:5',
           'Qz', 'S-I', 'S-II']]
Y_D4 = D4['Grade']

X_D4_train, X_D4_test, Y_D4_train, Y_D4_test = train_test_split(X_D4, Y_D4, test_size=0.2)

# Standardizing the D1 Values
D4_Scaler = StandardScaler()
X_D4_train = D4_Scaler.fit_transform(X_D4_train)
X_D4_test = D4_Scaler.transform(X_D4_test)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_D4_train, Y_D4_train)
clf = DecisionTreeClassifier(criterion="entropy", max_depth=3)
clf = clf.fit(X_D4_train, Y_D4_train)
nb = classifier = GaussianNB()
classifier.fit(X_D4_train, Y_D4_train)

Y_D4_Prediction_KNN = knn.predict(X_D4_test)
D4_Accuracy_KNN = accuracy_score(Y_D4_test, Y_D4_Prediction_KNN)
D4_Confusion_Matrix_KNN = confusion_matrix(Y_D4_test, Y_D4_Prediction_KNN)
D4_Precision_KNN = precision_score(Y_D4_test, Y_D4_Prediction_KNN, pos_label="Pass")
D4_Recall_KNN = recall_score(Y_D4_test, Y_D4_Prediction_KNN, pos_label="Pass")

Y_D4_Prediction_Decision = clf.predict(X_D4_test)
D4_Accuracy_Decision = accuracy_score(Y_D4_test, Y_D4_Prediction_Decision)
D4_Precision_Decision = precision_score(Y_D4_test, Y_D4_Prediction_Decision, pos_label="Pass")
D4_Recall_Decision = recall_score(Y_D4_test, Y_D4_Prediction_Decision, pos_label="Pass")

Y_D4_Prediction_Naive_Bayes = nb.predict(X_D4_test)
D4_Accuracy_Naive_Bayes = accuracy_score(Y_D4_test, Y_D4_Prediction_Naive_Bayes)
D4_Precision_Naive_Bayes = precision_score(Y_D4_test, Y_D4_Prediction_Naive_Bayes, pos_label="Pass")
D4_Recall_Naive_Bayes = recall_score(Y_D4_test, Y_D4_Prediction_Naive_Bayes, pos_label="Pass")


print("D4 Confusion Matrix:")
print(D4_Confusion_Matrix_KNN)
print("D4 Accuracy KNN:", D4_Accuracy_KNN*100)
print("D4 Precision KNN:", D4_Precision_KNN*100)
print("D4 Recall KNN:", D4_Recall_KNN*100)
print("D4 Accuracy Decision Tree:", D4_Accuracy_Decision*100)
print("D4 Precision Decision Tree:", D4_Precision_Decision*100)
print("D4 Recall Decision Tree:", D4_Recall_Decision*100)
print("D4 Accuracy Naive Bayes:", D4_Accuracy_Naive_Bayes*100)
print("D4 Precision Naive Bayes:", D4_Precision_Naive_Bayes*100)
print("D4 Recall Naive Bayes:", D4_Recall_Naive_Bayes*100)

print("-----------------------------------------------------------------------------------------")
X_D5 = D5[['As:1', 'As:2', 'As:3', 'As:4', 'As:5', 'As:6', 'As', 'Qz:1', 'Qz:2', 'Qz:3', 'Qz:4', 'Qz:4', 'Qz:5', 'Qz:6',
           'Qz:7', 'Qz:8', 'Qz', 'S-I', 'S-II']]
Y_D5 = D5['Grade']

X_D5_train, X_D5_test, Y_D5_train, Y_D5_test = train_test_split(X_D5, Y_D5, test_size=0.2)

# Standardizing the D1 Values
D5_Scaler = StandardScaler()
X_D5_train = D5_Scaler.fit_transform(X_D5_train)
X_D5_test = D5_Scaler.transform(X_D5_test)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_D5_train, Y_D5_train)
clf = DecisionTreeClassifier(criterion="entropy", max_depth=3)
clf = clf.fit(X_D5_train, Y_D5_train)
nb = classifier = GaussianNB()
classifier.fit(X_D5_train, Y_D5_train)

Y_D5_Prediction_KNN = knn.predict(X_D5_test)
D5_Accuracy_KNN = accuracy_score(Y_D5_test, Y_D5_Prediction_KNN)
D5_Confusion_Matrix_KNN = confusion_matrix(Y_D5_test, Y_D5_Prediction_KNN)
D5_Precision_KNN = precision_score(Y_D5_test, Y_D5_Prediction_KNN, pos_label="Pass")
D5_Recall_KNN = recall_score(Y_D5_test, Y_D5_Prediction_KNN, pos_label="Pass")

Y_D5_Prediction_Decision = clf.predict(X_D5_test)
D5_Accuracy_Decision = accuracy_score(Y_D5_test, Y_D5_Prediction_Decision)
D5_Precision_Decision = precision_score(Y_D5_test, Y_D5_Prediction_Decision, pos_label="Pass")
D5_Recall_Decision = recall_score(Y_D5_test, Y_D5_Prediction_Decision, pos_label="Pass")

Y_D5_Prediction_Naive_Bayes = nb.predict(X_D5_test)
D5_Accuracy_Naive_Bayes = accuracy_score(Y_D5_test, Y_D5_Prediction_Naive_Bayes)
D5_Precision_Naive_Bayes = precision_score(Y_D5_test, Y_D5_Prediction_Naive_Bayes, pos_label="Pass")
D5_Recall_Naive_Bayes = recall_score(Y_D5_test, Y_D5_Prediction_Naive_Bayes, pos_label="Pass")


print("D5 Confusion Matrix:")
print(D5_Confusion_Matrix_KNN)
print("D5 Accuracy KNN:", D5_Accuracy_KNN*100)
print("D5 Precision KNN:", D5_Precision_KNN*100)
print("D5 Recall KNN:", D5_Recall_KNN*100)
print("D5 Accuracy Decision Tree:", D5_Accuracy_Decision*100)
print("D5 Precision Decision Tree:", D5_Precision_Decision*100)
print("D5 Recall Decision Tree:", D5_Recall_Decision*100)
print("D5 Accuracy Naive Bayes:", D5_Accuracy_Naive_Bayes*100)
print("D5 Precision Naive Bayes:", D5_Precision_Naive_Bayes*100)
print("D5 Recall Naive Bayes:", D5_Recall_Naive_Bayes*100)

print("-----------------------------------------------------------------------------------------")
X_D6 = D6[['As:1', 'As:2', 'As:3', 'As:4', 'As:5', 'As:6', 'As', 'Qz:1', 'Qz:2', 'Qz:3', 'Qz:4', 'Qz:4', 'Qz:5', 'Qz:6',
           'Qz:7', 'Qz', 'S-I', 'S-II']]
Y_D6 = D6['Grade']

X_D6_train, X_D6_test, Y_D6_train, Y_D6_test = train_test_split(X_D6, Y_D6, test_size=0.2)

# Standardizing the D1 Values
D6_Scaler = StandardScaler()
X_D6_train = D6_Scaler.fit_transform(X_D6_train)
X_D6_test = D6_Scaler.transform(X_D6_test)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_D6_train, Y_D6_train)
clf = DecisionTreeClassifier(criterion="entropy", max_depth=3)
clf = clf.fit(X_D6_train, Y_D6_train)
nb = classifier = GaussianNB()
classifier.fit(X_D6_train, Y_D6_train)

Y_D6_Prediction_KNN = knn.predict(X_D6_test)
D6_Accuracy_KNN = accuracy_score(Y_D6_test, Y_D6_Prediction_KNN)
D6_Confusion_Matrix_KNN = confusion_matrix(Y_D6_test, Y_D6_Prediction_KNN)
D6_Precision_KNN = precision_score(Y_D6_test, Y_D6_Prediction_KNN, pos_label="Pass")
D6_Recall_KNN = recall_score(Y_D6_test, Y_D6_Prediction_KNN, pos_label="Pass")

Y_D6_Prediction_Decision = clf.predict(X_D6_test)
D6_Accuracy_Decision = accuracy_score(Y_D6_test, Y_D6_Prediction_Decision)
D6_Precision_Decision = precision_score(Y_D6_test, Y_D6_Prediction_Decision, pos_label="Pass")
D6_Recall_Decision = recall_score(Y_D6_test, Y_D6_Prediction_Decision, pos_label="Pass")

Y_D6_Prediction_Naive_Bayes = nb.predict(X_D6_test)
D6_Accuracy_Naive_Bayes = accuracy_score(Y_D6_test, Y_D6_Prediction_Naive_Bayes)
D6_Precision_Naive_Bayes = precision_score(Y_D6_test, Y_D6_Prediction_Naive_Bayes, pos_label="Pass")
D6_Recall_Naive_Bayes = recall_score(Y_D6_test, Y_D6_Prediction_Naive_Bayes, pos_label="Pass")


print("D6 Confusion Matrix:")
print(D6_Confusion_Matrix_KNN)
print("D6 Accuracy KNN:", D6_Accuracy_KNN*100)
print("D6 Precision KNN:", D6_Precision_KNN*100)
print("D6 Recall KNN:", D6_Recall_KNN*100)
print("D6 Accuracy Decision Tree:", D6_Accuracy_Decision*100)
print("D6 Precision Decision Tree:", D6_Precision_Decision*100)
print("D6 Recall Decision Tree:", D6_Recall_Decision*100)
print("D6 Accuracy Naive Bayes:", D6_Accuracy_Naive_Bayes*100)
print("D6 Precision Naive Bayes:", D6_Precision_Naive_Bayes*100)
print("D6 Recall Naive Bayes:", D6_Recall_Naive_Bayes*100)

print("-----------------------------------------------------------------------------------------")
X_D7 = D7[['As:1', 'As:2', 'As:3', 'As:4', 'As:5', 'As:6', 'As', 'Qz:1', 'Qz:2', 'Qz:3', 'Qz:4', 'Qz:4', 'Qz:5', 'Qz:6',
           'Qz:7', 'Qz:8', 'Qz', 'S-I', 'S-II']]
Y_D7 = D7['Grade']

X_D7_train, X_D7_test, Y_D7_train, Y_D7_test = train_test_split(X_D7, Y_D7, test_size=0.2)

# Standardizing the D7 Values
D7_Scaler = StandardScaler()
X_D7_train = D7_Scaler.fit_transform(X_D7_train)
X_D7_test = D7_Scaler.transform(X_D7_test)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_D7_train, Y_D7_train)
clf = DecisionTreeClassifier(criterion="entropy", max_depth=3)
clf = clf.fit(X_D7_train, Y_D7_train)
nb = classifier = GaussianNB()
classifier.fit(X_D7_train, Y_D7_train)

Y_D7_Prediction_KNN = knn.predict(X_D7_test)
D7_Accuracy_KNN = accuracy_score(Y_D7_test, Y_D7_Prediction_KNN)
D7_Confusion_Matrix_KNN = confusion_matrix(Y_D7_test, Y_D7_Prediction_KNN)
D7_Precision_KNN = precision_score(Y_D7_test, Y_D7_Prediction_KNN, pos_label="Pass")
D7_Recall_KNN = recall_score(Y_D7_test, Y_D7_Prediction_KNN, pos_label="Pass")

Y_D7_Prediction_Decision = clf.predict(X_D7_test)
D7_Accuracy_Decision = accuracy_score(Y_D7_test, Y_D7_Prediction_Decision)
D7_Precision_Decision = precision_score(Y_D7_test, Y_D7_Prediction_Decision, pos_label="Pass")
D7_Recall_Decision = recall_score(Y_D7_test, Y_D7_Prediction_Decision, pos_label="Pass")

Y_D7_Prediction_Naive_Bayes = nb.predict(X_D7_test)
D7_Accuracy_Naive_Bayes = accuracy_score(Y_D7_test, Y_D7_Prediction_Naive_Bayes)
D7_Precision_Naive_Bayes = precision_score(Y_D7_test, Y_D7_Prediction_Naive_Bayes, pos_label="Pass")
D7_Recall_Naive_Bayes = recall_score(Y_D7_test, Y_D7_Prediction_Naive_Bayes, pos_label="Pass")


print("D7 Confusion Matrix:")
print(D7_Confusion_Matrix_KNN)
print("D7 Accuracy KNN:", D7_Accuracy_KNN*100)
print("D7 Precision KNN:", D7_Precision_KNN*100)
print("D7 Recall KNN:", D7_Recall_KNN*100)
print("D7 Accuracy Decision Tree:", D7_Accuracy_Decision*100)
print("D7 Precision Decision Tree:", D7_Precision_Decision*100)
print("D7 Recall Decision Tree:", D7_Recall_Decision*100)
print("D7 Accuracy Naive Bayes:", D7_Accuracy_Naive_Bayes*100)
print("D7 Precision Naive Bayes:", D7_Precision_Naive_Bayes*100)
print("D7 Recall Naive Bayes:", D7_Recall_Naive_Bayes*100)
