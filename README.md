# 🧾 Invoice Generator App

A full-stack application that automates invoice generation from Excel data and fills a PDF template with invoice details. Built with **Python**, **C# (.NET Core)**, **ReactJS**, and integrated with **AWS services** for file storage, notifications, and backend processing.
Note: the PDF template must have fillable fields with the same name as the Excel spreadsheet
---

## 📌 Features

- Upload an Excel spreadsheet with invoice data
- Automatically detect new entries and generate PDF invoices
- Fill in a predefined PDF invoice template
- Store generated invoices on AWS S3
- React frontend to manage and download invoices
- Notification system when invoices are ready (email or UI)
- Backend built in Python (for processing) and C# (.NET) for APIs

---

## 🏗️ Tech Stack (as planned)

### Frontend
- [ReactJS](https://reactjs.org)
- TailwindCSS (optional)
- Axios (for API calls)

### Backend
- **Python** (Excel parsing, PDF generation)
  - Libraries: `pandas`, `fpdf2`, `openpyxl`, `boto3`
- **C#** (.NET 6 Web API for endpoints)
  - Libraries: `PdfSharpCore`, `EPPlus`, `AWSSDK.S3`

### Cloud & Infrastructure
- AWS S3 (file storage)
- AWS Lambda / EC2 (backend hosting)
- AWS API Gateway (expose APIs)
- AWS SNS / SES (notifications)
- AWS IAM (security)
- AWS DynamoDB or RDS (metadata storage)

---

## 📂 Project Structure

