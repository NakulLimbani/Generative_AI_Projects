# **Tutorial 8: AI-Based Text Summarization Application**

---

## **Objective**
This tutorial demonstrates the implementation of **text summarization** using **pre-trained transformer models (T5, BART, Pegasus)** for **abstractive summarization** and **TextRank** for **extractive summarization**. It explores different summarization techniques and evaluates their effectiveness using **ROUGE and BLEU scores**.

---

## **Key Features**
- Implementation of **Abstractive (T5, BART, Pegasus)** and **Extractive (TextRank)** summarization methods.
- **Flask-based web application** for interactive summarization.
- **Evaluation using ROUGE & BLEU scores** for performance comparison.

---

## **Usage**
- Run the provided Flask application to summarize text using different models.
- Compare summarization outputs and evaluation scores dynamically.
- Experiment with different input texts and analyze model behavior.

---

## **Steps to Run the Application**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/your-github-username/T8-Text-Summarization.git
cd T8-Text-Summarization
```

### **2️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **3️⃣ Run the Flask Web App**  
```bash
python app.py
```

### **4️⃣ Access the Application**  
- Open **http://127.0.0.1:5000/** in your web browser.  
- Enter text to be summarized.  
- Select a **summarization model** (T5, BART, Pegasus, TextRank).  
- Click **"Summarize"** to generate the output.  
- View **evaluation metrics (ROUGE, BLEU)** for the generated summary.  

---

🔹 Experiment with different texts and compare the summarization models! 🚀
```
