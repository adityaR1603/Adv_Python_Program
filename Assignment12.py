
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create sample customer churn dataset
data = {
    'CustomerID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Age': [25, 35, 45, np.nan, 30, 50, 40, 28, np.nan, 60],
    'MonthlyCharges': [500, 700, 800, 600, np.nan, 900, 750, 550, 650, 1000],
    'Tenure': [2, 12, 24, 5, 36, 48, 10, 3, 18, 60],
    'Churn': ['Yes', 'No', 'No', 'Yes', 'No',
              'No', 'Yes', 'Yes', 'No', 'No']
}

df = pd.DataFrame(data)

# Display original dataset
print("Original Dataset:")
print(df)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Handle missing values using mean
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['MonthlyCharges'] = df['MonthlyCharges'].fillna(
    df['MonthlyCharges'].mean()
)

# Remove duplicate records
df.drop_duplicates(inplace=True)

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Churn count
print("\nCustomer Churn Count:")
print(df['Churn'].value_counts())

# Calculate churn percentage
churn_percentage = (
    df['Churn'].value_counts(normalize=True) * 100
)
print("\nChurn Percentage:")
print(churn_percentage)

# Average monthly charges by churn
print("\nAverage Monthly Charges:")
print(df.groupby('Churn')['MonthlyCharges'].mean())

# Visualization 1: Churn distribution
df['Churn'].value_counts().plot(
    kind='bar', title='Customer Churn Distribution'
)
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.show()

# Visualization 2: Age distribution
plt.hist(df['Age'], bins=5, edgecolor='black')
plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Visualization 3: Monthly charges by churn
df.boxplot(column='MonthlyCharges', by='Churn')
plt.title("Monthly Charges vs Churn")
plt.suptitle("")
plt.xlabel("Churn")
plt.ylabel("Monthly Charges")
plt.show()

# Visualization 4: Tenure distribution
df.groupby('Churn')['Tenure'].mean().plot(
    kind='bar', title='Average Tenure by Churn'
)
plt.xlabel("Churn")
plt.ylabel("Average Tenure")
plt.show()

print("\nCleaned Dataset:")
print(df)