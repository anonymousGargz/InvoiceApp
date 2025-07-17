import pandas as pd
from fillpdf import fillpdfs
import os

PDF_TEMPLATE = 'C://Users//gnisa//Documents//Projects//InvoiceApp//invoiceBackend//ParkPDF.pdf'

def generatePDF(EXCEL_PATH):
    formFields = list( fillpdfs.get_form_fields(PDF_TEMPLATE).keys())
    print(formFields)
    df = pd.read_excel(EXCEL_PATH)
    # Get column headings for the Excel File
    column_headings = df.columns.tolist()

    columnsToFill = []

    for index, row in df.iterrows():
        # Assuming you want to loop over all column headings for this row:
        for i, col in enumerate(column_headings):
            print(row[col])
            columnsToFill.append(row[col])

        data_dict = {}

        # Make sure formFields and columnsToFill are aligned in length!
        for j in range(len(formFields)):
            data_dict[formFields[j]] = columnsToFill[j]
        
        print(data_dict)

        fillpdfs.write_fillable_pdf(
            input_pdf_path=PDF_TEMPLATE,
            output_pdf_path=os.path.join('C://Users//gnisa//Documents//Projects//InvoiceApp//invoiceBackend', f'{columnsToFill[0]}_invoice.pdf'),
            data_dict=data_dict
        )

        columnsToFill = []
