
# 📄 PDF to Table Extractor

This is a **Streamlit-based** web application that extracts transactions from bank statement PDFs. The extracted transactions can be **downloaded as an Excel file**. The app also detects **encoding issues** (like `cid:21`) and **alerts the user** if the text is unreadable.

---

## 🚀 Features
✅ Extracts transactions from **PDF bank statements**  
✅ Supports **structured table detection**  
✅ **Handles encoding issues** and alerts users  
✅ **Exports transactions to Excel** for easy analysis  
✅ **Simple, fast, and user-friendly**  

---

## 🛠 Requirements  

Ensure you have **Python 3.7+** installed before proceeding.  

### **Required Python Libraries**  
Install the dependencies using:  

```sh
pip install streamlit pandas pdfplumber openpyxl
```

---

## 📂 How to Run  

1️⃣ **Clone the repository (if applicable)**  
```sh
git clone https://github.com/your-repository-name.git
cd your-repository-name
```

2️⃣ **Run the application**  
```sh
streamlit run app.py
```

---

## 📸 Screenshots  

🔹 **Upload PDF**  
![Upload PDF](https://github.com/user-attachments/assets/dc631394-8c66-4be7-8cfb-5840bf6b0a15)  

🔹 **Extracted Tables**  
![Extracted Transactions](https://github.com/user-attachments/assets/10249105-3da6-474a-825f-cfd1cf65a1f0)  

🔹 **Error Handling (Encoding Issues)**  
![Encoding Error](https://github.com/user-attachments/assets/94a046a5-359e-4f49-b156-a009eb51f1b9)  

---

## 🔥 Error Handling  

If text extraction **fails** due to encoding issues (e.g., `cid:21`), the app will display:  

```
🚫 The text is not extractable, or no tables were found in the PDF.
```

### ✅ **Possible Solutions**  
- **Try another PDF format**  
- **Ensure the PDF contains selectable text** (scanned PDFs won't work)  
- **Use OCR tools like Tesseract if needed**  

---

## 📜 License  
This project is licensed under the **MIT License**.

---

## 👨‍💻 Author  
**[Pranav Singla]**  
📧 [pranavsingla1407@gmail.com]  
```
