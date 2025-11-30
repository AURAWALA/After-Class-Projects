import pandas as pd


data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, 35, 40, 22],
    "Department": ["HR", "IT", "Finance", "IT", "HR"],
    "Salary": [50000, 60000, 70000, 65000, 48000]
}


df = pd.DataFrame(data)
print("Original DataFrame:\n", df)


print("\nFirst 3 rows:\n", df.head(3))
print("\nDataFrame Info:\n", df.info())
print("\nSummary statistics:\n", df.describe())


print("\nSelect 'Name' column:\n", df["Name"])
print("\nSelect multiple columns:\n", df[["Name", "Salary"]])


print("\nEmployees older than 30:\n", df[df["Age"] > 30])
print("\nEmployees in IT department:\n", df[df["Department"] == "IT"])


df["Bonus"] = df["Salary"] * 0.10
print("\nDataFrame with Bonus:\n", df)


df.loc[df["Name"] == "Alice", "Salary"] = 52000
print("\nUpdated Salary for Alice:\n", df)


print("\nSort by Age descending:\n", df.sort_values(by="Age", ascending=False))


grouped = df.groupby("Department")["Salary"].mean()
print("\nAverage Salary by Department:\n", grouped)


df_dropped = df.drop(columns=["Bonus"])
print("\nDataFrame after dropping Bonus column:\n", df_dropped)

