CREATE DATABASE p2p_lending_analysis;

USE p2p_lending_analysis;

CREATE TABLE p2p_loans (
    Loan_ID VARCHAR(20),
    Issue_Date DATE,
    Borrower_City VARCHAR(50),
    Employment_Type VARCHAR(50),
    Annual_Income_INR DECIMAL(15,2),
    Loan_Purpose VARCHAR(50),
    Loan_Amount_INR DECIMAL(15,2),
    Funded_Amount_INR DECIMAL(15,2),
    Interest_Rate DECIMAL(5,2),
    Loan_Term_Months INT,
    Risk_Grade VARCHAR(5),
    Loan_Status VARCHAR(20),
    Total_Repayment_INR DECIMAL(15,2),
    Investor_Count INT,
    Income_Verification VARCHAR(30),
    Loan_Channel VARCHAR(30)
);

SELECT * FROM p2p_loans;

SELECT COUNT(*) AS Total_Loans FROM p2p_loans;

SELECT SUM(Funded_Amount_INR) AS Total_Funded_Amount FROM p2p_loans;

SELECT AVG(Loan_Amount_INR) AS Average_Loan_Amount FROM p2p_loans;

SELECT MAX(Loan_Amount_INR) AS Highest_Loan_Amount
FROM p2p_loans;

SELECT Loan_Status, COUNT(*) AS Loan_Count FROM p2p_loans
GROUP BY Loan_Status;

SELECT Loan_Purpose, COUNT(*) AS Loan_Count
FROM p2p_loans GROUP BY Loan_Purpose
ORDER BY Loan_Count DESC;

SELECT AVG(Interest_Rate) AS Average_Interest_Rate FROM p2p_loans;

SELECT YEAR(Issue_Date) AS Year,COUNT(*) AS Loan_Count
FROM p2p_loans GROUP BY YEAR(Issue_Date)
ORDER BY Year;

SELECT Risk_Grade, COUNT(*) AS Loan_Count
FROM p2p_loans GROUP BY Risk_Grade
ORDER BY Risk_Grade;

SELECT COUNT(CASE WHEN Loan_Status = 'Defaulted' THEN 1 END) * 100.0
/ COUNT(*) AS Default_Rate
FROM p2p_loans;