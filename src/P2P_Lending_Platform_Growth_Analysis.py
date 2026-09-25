import pandas as pd

df=pd.read_csv("P2P_Lending_Platform_Growth_Analysis.csv")

print(df.head())

print(df.tail())

print(df.shape)

print(df.columns)

print(df.dtypes)

df.info()

print(df.isnull().sum())

print(df.duplicated().sum())

print(df.describe())

print(df["Loan_Status"].unique())

print("Total Loans:",len(df))

print("Total Loan Amount:",df["Loan_Amount_INR"].sum())

print("Average Loan Amount:", df["Loan_Amount_INR"].mean())

print("Highest Loan Amount:", df["Loan_Amount_INR"].max())

print("Total Funded Amount:", df["Funded_Amount_INR"].sum())

print("Average Interest Rate:", df["Interest_Rate"].mean())

print(df["Loan_Status"].value_counts())

print(df["Loan_Purpose"].value_counts())

print(df["Risk_Grade"].value_counts())

print(df["Borrower_City"].value_counts())

print(df["Issue_Date"].str[:4].value_counts().sort_index())

print(df.groupby("Loan_Status")["Funded_Amount_INR"].sum())

print(df.groupby("Loan_Purpose")["Loan_Amount_INR"].mean())

print(df["Employment_Type"].value_counts())

print(df.groupby("Employment_Type")["Loan_Amount_INR"].mean())

print(df["Risk_Grade"].value_counts().sort_index())

print(df.groupby("Risk_Grade")["Interest_Rate"].mean())

defaulted=df[df["Loan_Status"]=="Defaulted"]
print("Defaulted Loans:",len(defaulted))

default_rate=len(defaulted)/len(df)*100
print("Default Rate:",round(default_rate,2),"%")

print("Total Repayment:", df["Total_Repayment_INR"].sum())

print("Average Investors:", df["Investor_Count"].mean())

print(df.groupby("Risk_Grade")["Loan_Amount_INR"].mean())

df["Issue_Date"]=pd.to_datetime(df["Issue_Date"],errors="coerce")
print(df["Issue_Date"].head())

print("Invalid Dates:",df["Issue_Date"].isnull().sum())

df["Borrower_City"]=df["Borrower_City"].fillna("Unknown")
df["Employment_Type"]=df["Employment_Type"].fillna("Unknown")
df["Annual_Income_INR"]=df["Annual_Income_INR"].fillna(df["Annual_Income_INR"].median())
df["Interest_Rate"]=df["Interest_Rate"].fillna(df["Interest_Rate"].median())
print(df.isnull().sum())

df=df.drop_duplicates()
print("Duplicates after cleaning:",df.duplicated().sum())

print("Shape after cleaning:", df.shape)
print(df.head())
print(df.isnull().sum())

df.to_csv("P2P_Lending_Cleaned.csv", index=False)
print("Cleaned file saved successfully")

df["Year"]=df["Issue_Date"].dt.year
print(df["Year"].value_counts().sort_index())

print(df.groupby("Year")["Funded_Amount_INR"].sum())

print(df.groupby("Loan_Purpose")["Funded_Amount_INR"].sum().sort_values(ascending=False))

print(df.groupby("Borrower_City")["Funded_Amount_INR"].sum().sort_values(ascending=False))

default_by_risk = df.groupby("Risk_Grade")["Loan_Status"].apply(
    lambda x: (x == "Defaulted").sum() / len(x) * 100)
print(default_by_risk)

# Loan Growth by Year
import matplotlib.pyplot as plt
yearly_loans = df.groupby("Year")["Loan_ID"].count()
plt.figure(figsize=(8,5))
plt.plot(yearly_loans.index, yearly_loans.values, marker="o")
plt.title("Loan Growth by Year")
plt.xlabel("Year")
plt.ylabel("Number of Loans")
plt.grid(True)
plt.savefig("loan_growth_by_year.png")
plt.show()

# Funding by Loan Purpose
funding_purpose = df.groupby("Loan_Purpose")["Funded_Amount_INR"].sum()
plt.figure(figsize=(11,7))
plt.bar(funding_purpose.index, funding_purpose.values)
plt.title("Funding by Loan Purpose")
plt.xlabel("Loan Purpose")
plt.ylabel("Funded Amount (INR)")
plt.xticks(rotation=45)
plt.savefig("funding_by_purpose.png")
plt.show()

# Loan Status Distribution
status_count = df["Loan_Status"].value_counts()
plt.figure(figsize=(7,5))
plt.pie(status_count.values, labels=status_count.index, autopct="%1.1f%%")
plt.title("Loan Status Distribution")
plt.savefig("loan_status.png")
plt.show()

# Risk Grade Distribution
risk_count = df["Risk_Grade"].value_counts().sort_index()
plt.figure(figsize=(7,5))
plt.bar(risk_count.index, risk_count.values)
plt.title("Risk Grade Distribution")
plt.xlabel("Risk Grade")
plt.ylabel("Number of Loans")
plt.savefig("risk_grade.png")
plt.show()

# Funding by City
city_funding = df.groupby("Borrower_City")["Funded_Amount_INR"].sum().sort_values(ascending=False)
plt.figure(figsize=(10,6))
plt.bar(city_funding.index, city_funding.values)
plt.title("Funding by City")
plt.xlabel("Borrower City") 
plt.ylabel("Funded Amount (INR)")
plt.xticks(rotation=45)
plt.savefig("funding_by_city.png")
plt.show()

# Default Rate by Risk Grade
city_funding = df.groupby("Borrower_City")["Funded_Amount_INR"].sum().sort_values(ascending=False)
plt.figure(figsize=(10,6))
plt.bar(city_funding.index, city_funding.values)
plt.title("Funding by City")
plt.xlabel("Borrower City")
plt.ylabel("Funded Amount (INR)")
plt.xticks(rotation=45)
plt.savefig("default_rate_by_risk.png")
plt.show()

# Business Insights
print("\nBusiness Insights")
print("1.The lending platform has 2000 loans after data cleaning.")
print("2.Total funded amount is around Rs. 510.23 million.")
print("3.The average loan amount is around Rs. 267,830.")
print("4.Loan activity increased from 2021 to 2025.")
print("5.Debt Consolidation has the highest number of loans.")
print("6.Completed loans are the largest loan status category.")
print("7.Risk Grade B has the highest number of loans.")
print("8.The overall default rate is around 4.25%.")
print("9.Funding levels differ across borrower cities.")
print("10.The platform shows an increase in loan funding over the years.")