# # Import libraries
# import matplotlib.pyplot as plt
# import numpy as np
# import seaborn as sns   # for heatmap

# # Sample data
# x = np.array([1,2,3,4,5])
# y = np.array([10,20,25,30,40])

# data = np.array([1,2,2,3,3,3,4,4,5])
# categories = ['A','B','C','D']
# values = [10,20,15,25]

# matrix = np.array([[1,2,3],
#                    [4,5,6],
#                    [7,8,9]])

# # -------------------------------
# # 1. Line Plot (with attributes)
# # -------------------------------
# plt.figure(figsize=(6,4))
# plt.plot(x, y, color='blue', marker='o', linestyle='--', label='Line Data')
# plt.xlabel("X Axis")
# plt.ylabel("Y Axis")
# plt.title("Line Plot")
# plt.grid()
# plt.legend()
# plt.show()

# # -------------------------------
# # 2. Scatter Plot
# # -------------------------------
# plt.figure(figsize=(6,4))
# plt.scatter(x, y, color='red')
# plt.xlabel("X Axis")
# plt.ylabel("Y Axis")
# plt.title("Scatter Plot")
# plt.grid()
# plt.show()

# # -------------------------------
# # 3. Bar Chart
# # -------------------------------
# plt.figure(figsize=(6,4))
# plt.bar(categories, values, color='green')
# plt.title("Bar Chart")
# plt.xlabel("Categories")
# plt.ylabel("Values")
# plt.show()

# # -------------------------------
# # 4. Histogram (PDF important)
# # -------------------------------
# plt.figure(figsize=(6,4))
# plt.hist(data, bins=5, color='purple')
# plt.title("Histogram")
# plt.xlabel("Values")
# plt.ylabel("Frequency")
# plt.show()

# # -------------------------------
# # 5. Pie Chart
# # -------------------------------
# plt.figure(figsize=(6,4))
# plt.pie(values, labels=categories, autopct='%1.1f%%')
# plt.title("Pie Chart")
# # 6. Box Plot
# # -------------------------------
# plt.figure(figsize=(6,4))
# plt.boxplot(data)
# plt.title("Box Plot")
# plt.show()

# # ------------------------------
# plt.show()

# # --------------------------------
# # 7. Heatmap (PDF important)
# # -------------------------------
# plt.figure(figsize=(6,4))
# sns.heatmap(matrix, annot=True)
# plt.title("Heatmap")
# plt.show()

# # -------------------------------
# # 8. Time Series Plot (PDF important)
# # -------------------------------
# time = np.arange(1,6)
# values = np.array([5,10,15,10,20])

# plt.figure(figsize=(6,4))
# plt.plot(time, values, marker='o')
# plt.title("Time Series Plot")
# plt.xlabel("Time")
# plt.ylabel("Value")
# plt.grid()
# plt.show()


import pandas as pd

# -------------------------------
# 1. Create DataFrame
# -------------------------------
data = {
    'Name': ['Steve', 'Lia', 'Vin', 'Katie'],
    'Age': [32, 28, 45, 38],
    'Gender': ['Male', 'Female', 'Male', 'Female'],
    'Rating': [3.45, 4.6, 3.9, 2.78]
}

df = pd.DataFrame(data)

print("Original DataFrame:\n", df)

# -------------------------------
# 2. Basic Info (VIEW)
# -------------------------------
print("\nHEAD:\n", df.head())
print("\nSHAPE:", df.shape)
print("\nCOLUMNS:", df.columns)

# -------------------------------
# 3. Selection
# -------------------------------
print("\nSingle Column:\n", df['Name'])
print("\nMultiple Columns:\n", df[['Name', 'Age']])

# -------------------------------
# 4. Row Access
# -------------------------------
print("\nUsing loc:\n", df.loc[1])
print("\nUsing iloc:\n", df.iloc[2])

# -------------------------------
# 5. Modify Data (Add Column)
# -------------------------------
df['Bonus'] = df['Rating'] * 10
print("\nAfter Adding Column:\n", df)

# -------------------------------
# 6. Missing Values (CLEANING)
# -------------------------------
df.loc[1, 'Age'] = None   # create missing value

print("\nCheck Missing (isnull):\n", df.isnull())

# dropna types
print("\nDrop rows with any NaN:\n", df.dropna())
print("\nDrop columns with NaN:\n", df.dropna(axis=1))
print("\nDrop rows if all values are NaN:\n", df.dropna(how='all'))

# fill missing values
print("\nFill missing values:\n", df.fillna(0))

# -------------------------------
# 7. Grouping
# -------------------------------
print("\nGroupBy Gender (Average Rating):\n",
      df.groupby('Gender')['Rating'].mean())

# -------------------------------
# 8. Sorting
# -------------------------------
print("\nSorted by Age:\n", df.sort_values(by='Age'))

# -------------------------------
# 9. Statistics
# -------------------------------
print("\nStatistics:\n", df.describe())