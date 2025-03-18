# 📄 Bank Statement PDF Extractor

This is a **Streamlit-based** web application that extracts transactions from bank statement PDFs. The extracted transactions can be **downloaded as an Excel file**. The app also detects **encoding issues** (like `cid:21`) and **alerts the user** if the text is unreadable.

---

## 🚀 Features
✅ Extracts transactions from **PDF bank statements**  
✅ Supports **structured table detection**  
✅ **Handles encoding issues** and alerts users  
✅ **Exports transactions to Excel** for easy analysis  
✅ **Simple, fast, and user-friendly**  

---



## 📸 Screenshots  
🔹 **Upload PDF**  
![image](https://github.com/user-attachments/assets/dc631394-8c66-4be7-8cfb-5840bf6b0a15)
![Upload PDF](path/to/upload.pdf)  

🔹 **Extracted Tables**  
![image](https://github.com/user-attachments/assets/10249105-3da6-474a-825f-cfd1cf65a1f0)
![Extracted Transactions](path/to/extracted-data.png)  

🔹 **Error Handling (Encoding Issues)**  
![image](https://github.com/user-attachments/assets/94a046a5-359e-4f49-b156-a009eb51f1b9)
![Encoding Error](path/to/encoding-error.png)  

---

## 🛠 Installation

### **1️⃣ Install Dependencies**
Make sure you have **Python 3.7+** installed. Then, run:

```sh
pip install streamlit pandas pdfplumber openpyxl
2️⃣ Run the Application
Run the following command in the project directory:

sh
Copy
Edit
streamlit run app.py
📂 How to Use
Upload a Bank Statement PDF 📂
Wait for the extraction process ⏳
View extracted transactions in a table 📊
Download transactions as an Excel file 📥
🔥 Error Handling
If text extraction fails due to encoding issues (cid:21), the app will display:

pgsql
Copy
Edit
🚫 The text is not extractable, or no tables were found in the PDF.
✅ Solution
Try another PDF format
Ensure the PDF contains selectable text (scanned PDFs won't work)
Use OCR tools like Tesseract if needed
