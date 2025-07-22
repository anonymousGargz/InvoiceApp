import pandas as pd
from datetime import datetime, timedelta
import random

# Sample data
first_names = ["John", "Jane", "Alice", "Bob", "Mary", "Steve", "Laura", "Tom", "Nina", "Paul"]
surnames = ["Smith", "Doe", "Brown", "Wilson", "Johnson", "Lee", "Garcia", "Martinez", "Davis", "Clark"]
invoice_nos = [f"INV{1000+i}" for i in range(10)]

# Generate random dates for Invoice Date and Consultation Date
base_date = datetime.today()
invoice_dates = [base_date - timedelta(days=random.randint(1, 30)) for _ in range(10)]
consultation_dates = [date - timedelta(days=random.randint(0, 5)) for date in invoice_dates]

# Generate random Total Due amounts
total_due = [round(random.uniform(50, 500), 2) for _ in range(10)]

# Create DataFrame
df = pd.DataFrame({
    "First Name": first_names,
    "Surname": surnames,
    "Invoice No": invoice_nos,
    "Invoice Date": [date.strftime("%Y-%m-%d") for date in invoice_dates],
    "Consultation Date": [date.strftime("%Y-%m-%d") for date in consultation_dates],
    "Total Due": total_due
})

# Save to Excel
file_path = "C://Users//gnisa//Documents//Projects//InvoiceApp//invoiceBackend//invoices_sample.xlsx"
df.to_excel(file_path, index=False)

file_path
