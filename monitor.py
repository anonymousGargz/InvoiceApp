# monitor.py
from createDatabase import getLastRow, create, addRow 
import time
import os
from pdfGenerator import generatePDF
import pandas as pd
from pdfGenerator import generatePDF

EXCEL_PATH = "C://Users//gnisa//Documents//Projects//InvoiceApp//invoiceBackend//invoices_sample.xlsx" ## File to be monitored for changes
FILE_PATH = "C://Users//gnisa//Documents//Projects//InvoiceApp//invoiceBackend//copied.xlsx"


def checkNewRows():
    lastProcessed = getLastRow()
    if lastProcessed is None:
        lastProcessed=0
    df = pd.read_excel(EXCEL_PATH)
    row_count = len(df)
    print(row_count)
    if (row_count> lastProcessed):
        change = row_count- lastProcessed
        # Select the first n rows
        df_to_copy = df.tail(change)
        print(df_to_copy)


        if not os.path.exists(FILE_PATH):
    # Create an empty DataFrame with the same columns
            empty_df = pd.DataFrame(columns=df.columns)
    # Write to Excel
            with pd.ExcelWriter(FILE_PATH, engine='openpyxl') as writer:
                empty_df.to_excel(writer, sheet_name="Base", index=False)

        else:
            print(f"{FILE_PATH} already exists.")
    # Write to the target sheet
        with pd.ExcelWriter(FILE_PATH, mode="a", if_sheet_exists="replace", engine="openpyxl") as writer:
            df_to_copy.to_excel(writer, sheet_name="Base", index=False)

    # Add new rows to the database to reflect having processed the existing rows
        for i in range(0, change):
            addRow()

        generatePDF(EXCEL_PATH=FILE_PATH)

create()
checkNewRows()