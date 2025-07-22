import pandas as pd
from fillpdf import fillpdfs
import os

PDF_TEMPLATE = 'C://Users//gnisa//Documents//Projects//InvoiceApp//invoiceBackend//ParkPDF.pdf'

import os
import pandas as pd
from pdfrw import PdfReader, PdfWriter, PdfDict



def fill_pdf(input_pdf_path, output_pdf_path, data_dict):
    ANNOT_KEY = '/Annots'
    ANNOT_FIELD_KEY = '/T'
    SUBTYPE_KEY = '/Subtype'
    WIDGET_SUBTYPE_KEY = '/Widget'

    template_pdf = PdfReader(input_pdf_path)
    for page in template_pdf.pages:
        annotations = page.get(ANNOT_KEY)
        if annotations:
            for annotation in annotations:
                if annotation.get(SUBTYPE_KEY) == WIDGET_SUBTYPE_KEY and annotation.get(ANNOT_FIELD_KEY):
                    key = annotation[ANNOT_FIELD_KEY][1:-1]  # Remove parentheses
                    if key in data_dict:
                        annotation.update(
                            PdfDict(V='{}'.format(data_dict[key]))
                        )
                        annotation.update(
                            PdfDict(AS='{}'.format(data_dict[key]))
                        )
    PdfWriter().write(output_pdf_path, template_pdf)


def generatePDF(EXCEL_PATH):
    df = pd.read_excel(EXCEL_PATH)
    column_headings = df.columns.tolist()
    column_headings.sort()

    fname=0
    sname=1
    date=2
    for i in range(0, len(column_headings)):
        if (column_headings[i].__contains__("surname")):
            sname=i
        elif (column_headings[i].__contains__("name")):
            fname=i
        elif (column_headings[i].__contains__("date")):
            date=i

    # Get form field names from your PDF template
    # Since fillpdfs is only used here to get form fields, 
    # you can keep using it or replace with pdfrw method if needed.
     # assuming you want to keep this just for field names
    formFields = list(fillpdfs.get_form_fields(PDF_TEMPLATE).keys())
    formFields.sort()
    print("Form fields in PDF template:", formFields)

    for index, row in df.iterrows():
        data_dict = {}
        # Map each form field to corresponding column value by position
        for j in range(len(formFields)):
            # Defensive check if Excel has enough columns for form fields
            if j < len(column_headings):
                data_dict[formFields[j]] = row[column_headings[j]]
            else:
                data_dict[formFields[j]] = ""  # or None if you prefer

        print("Data to fill:", data_dict)

        output_pdf_path = os.path.join(
            'C://Users//gnisa//Documents//Projects//InvoiceApp//invoiceBackend',
            f'{row[column_headings[fname]]}_{row[column_headings[sname]]}_{row[column_headings[date]]}_invoice.pdf'
        )

        fill_pdf(PDF_TEMPLATE, output_pdf_path, data_dict)
