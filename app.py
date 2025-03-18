import streamlit as st
import pandas as pd
import pdfplumber
import re
from io import BytesIO

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            extracted_text = page.extract_text()
            if extracted_text:
                text += extracted_text + "\n"
    return text

# Function to check for encoding issues not possible without ocr
def is_text_encoded(text):
    return bool(re.search(r'cid:\d+|��', text))  # Detects encoded text like 'cid:21'

# Function to extract transactions from text
def extract_transactions(text):
    transaction_pattern = re.compile(r'(\d{2}-[A-Za-z]{3}-\d{4})\s+(.*?)\n([\d,.]+)\s+([\d,.]+Dr|[\d,.]+Cr)')
    transactions = transaction_pattern.findall(text)

    data = []
    for date, desc, amount, balance in transactions:
        debit, credit = ('', '')
        if 'Cr' in balance:
            credit = amount
        else:
            debit = amount

        data.append({
            'Date': date,
            'Description': desc.strip(),
            'Debit': debit,
            'Credit': credit,
            'Balance': balance
        })

    return pd.DataFrame(data)

# Streamlit App
st.set_page_config(page_title="Table from PDF Extractor", layout="wide")

st.title("📄 Bank Statement Extractor")
st.write("Upload a **bank statement PDF** to extract transactions and download the results as an Excel file.")

uploaded_file = st.file_uploader("📂 Upload a PDF", type=["pdf"])

if uploaded_file:
    with st.spinner("Extracting data..."):
        text = extract_text_from_pdf(uploaded_file)

    # If text is encoded or missing, display an error message
    if not text or is_text_encoded(text):
        st.error("🚫 The text is not extractable, or no tables were found in the PDF. Try OCR")
    else:
        transactions_df = extract_transactions(text)

        if not transactions_df.empty:
            st.success("✅ Transactions extracted successfully!")
            st.write(transactions_df)

            # Convert DataFrame to Excel
            output = BytesIO()
            with pd.ExcelWriter(output, engine="openpyxl") as writer:
                transactions_df.to_excel(writer, index=False)
            excel_data = output.getvalue()

            # Download button
            st.download_button(
                label="📥 Download Excel File",
                data=excel_data,
                file_name="bank_transactions.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        else:
            st.error("🚫 No tables were found in the PDF.")

st.info("Developed with ❤️ using Streamlit.")
