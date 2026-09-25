from reportlab.pdfgen import canvas

pdf = canvas.Canvas("P2P_Lending_Growth_Analysis_Report.pdf")
pdf.drawString(100, 750, "Peer-to-Peer Lending Platform Growth Analysis")
pdf.drawString(100, 720, "Project Overview")
pdf.drawString(100, 700, "This project analyzes the growth of a peer-to-peer lending platform")
pdf.drawString(100, 680, "using loan, borrower, funding, repayment and risk-related data.")
pdf.drawString(100, 640, "Dataset Information")

pdf.drawString(100, 620, "Total Records: 2,008")
pdf.drawString(100, 600, "Total Columns: 16")
pdf.drawString(100, 580, "Data Period: 2021 to 2025")
pdf.drawString(100, 560, "Duplicate Records Found: 8")
pdf.drawString(100, 540, "Duplicate Records After Cleaning: 0")

pdf.drawString(100, 480, "Missing values were checked and handled.")
pdf.drawString(100, 460, "Missing city and employment values were replaced with Unknown.")
pdf.drawString(100, 440, "Missing income and interest rate values were filled using the median.")
pdf.drawString(100, 420, "Duplicate records were removed.")
pdf.drawString(100, 400, "The cleaned dataset contains 2,000 records.")

pdf.drawString(100, 370, "Python EDA")
pdf.drawString(100, 350, "Python and Pandas were used to analyze the lending data.")
pdf.drawString(100, 330, "The analysis covered loan amounts, funding, loan status and risk grades.")
pdf.drawString(100, 310, "Loan growth was analyzed from 2021 to 2025.")
pdf.drawString(100, 290, "Funding was analyzed by loan purpose and borrower city.")
pdf.drawString(100, 270, "Default rates were also analyzed across different risk grades.")

pdf.drawString(100, 240, "SQL Analysis")
pdf.drawString(100, 220, "SQL was used to analyze the cleaned lending dataset.")
pdf.drawString(100, 200, "A total of 10 SQL queries were performed.")
pdf.drawString(100, 180, "The analysis covered total loans, funding, loan amounts,")
pdf.drawString(100, 160, "loan status, loan purpose, interest rate, yearly growth,")
pdf.drawString(100, 140, "risk grades and default rate.")


pdf.showPage()
pdf.drawString(100, 750, "Business Insights")
pdf.drawString(100, 720, "1. The lending platform has 2000 loans after data cleaning.")
pdf.drawString(100, 690, "2. Total funded amount is around Rs. 510.23 million.")
pdf.drawString(100, 660, "3. The average loan amount is around Rs. 267,830.")
pdf.drawString(100, 630, "4. Loan activity increased from 2021 to 2025.")
pdf.drawString(100, 600, "5. Debt Consolidation has the highest number of loans.")
pdf.drawString(100, 570, "6. Completed loans are the largest loan status category.")
pdf.drawString(100, 540, "7. Risk Grade B has the highest number of loans.")
pdf.drawString(100, 510, "8. The overall default rate is around 4.25%.")
pdf.drawString(100, 480, "9. Funding levels differ across borrower cities.")
pdf.drawString(100, 450, "10. The platform shows an increase in loan funding over the years.")

pdf.showPage()
pdf.drawString(100, 750, "Conclusion")
pdf.drawString(100, 720, "The analysis shows that the P2P lending platform")
pdf.drawString(100, 700, "experienced growth in loan activity and funding over time.")
pdf.drawString(100, 680, "The analysis also highlights differences in loan purposes,")
pdf.drawString(100, 660, "cities, risk grades and loan repayment status.")
pdf.drawString(100, 620, "Python, Pandas and SQL were used to perform the analysis.")
pdf.drawString(100, 600, "The results can help understand lending activity,")
pdf.drawString(100, 580, "funding patterns and loan risk across the platform.")

graphs = [
    ("Loan Growth by Year", "loan_growth_by_year.png"),
    ("Funding by Loan Purpose", "funding_by_purpose.png"),
    ("Loan Status Distribution", "loan_status.png"),
    ("Risk Grade Distribution", "risk_grade.png"),
    ("Funding by City", "funding_by_city.png"),
    ("Default Rate by Risk Grade", "default_rate_by_risk.png")
]
for title, image in graphs:
    pdf.showPage()
    pdf.drawString(100, 750, title)
    pdf.drawImage(image, 50, 250, width=500, height=400)

pdf.save()

print("PDF created successfully")