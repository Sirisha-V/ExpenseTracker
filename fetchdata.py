import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Authenticate and fetch data from Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("Downloads/credentials.json", scope)
client = gspread.authorize(creds)

# Open the Google Sheet
sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/10bNlqh3KqMXvumnUJsoLpAVW4fuMQzLOIj29_xh6wkQ/edit?usp=drive_link")
worksheet = sheet.get_worksheet(0)

# Convert to DataFrame
data = worksheet.get_all_records()
df = pd.DataFrame(data)

# Analyze expenses
def analyze_expenses(df):
    total_expenses = df['Amount'].sum()
    waste_expenses = df[df['Category'] == 'Waste']['Amount'].sum()
    return total_expenses, waste_expenses

total_expenses, waste_expenses = analyze_expenses(df)
print(f"Total Expenses: {total_expenses}")
print(f"Waste Expenses: {waste_expenses}")
