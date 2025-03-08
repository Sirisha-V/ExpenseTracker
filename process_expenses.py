import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Read the Excel file
file_path = 'Siri_Spend_Analysis.xlsx'
df = pd.read_excel(file_path)

# Process the data
total_expenses = df['COST'].sum()
gross_earned = 72000  # Example value, adjust as needed
remaining = gross_earned - total_expenses

# Generate summary report
summary = f"""
Expense Summary:
Total Expenses: {total_expenses}
Gross Earned: {gross_earned}
Remaining: {remaining}
"""

# Print the summary
print(summary)

# Send email with summary report
def send_email(subject, body, recipients):
    sender_email = "your_email@example.com"
    sender_password = "your_password"
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ", ".join(recipients)
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipients, text)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Example usage
recipients = ["user1@example.com", "user2@example.com"]
send_email("Monthly Expense Summary", summary, recipients)
