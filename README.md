# 📄 AI Resume Ranking System

🚀 A simple AI-powered system that analyzes resumes and ranks candidates based on how well they match a given Job Description.

---
## 💡 Why This Project?

Manual resume screening is time-consuming and inefficient. This project demonstrates how AI techniques can automate candidate evaluation and help recruiters quickly identify the best candidates based on skills and relevance.

---

## 🔍 Overview

Recruitment platforms receive hundreds of resumes for a single job. This project automates the process of:

- Extracting information from resumes  
- Identifying relevant skills  
- Matching resumes with job descriptions  
- Ranking candidates based on a scoring algorithm  

---

## ⚙️ Features

✅ Upload multiple resumes (PDF/DOCX)  
✅ Extract candidate details (Email, Phone, Skills)  
✅ Match resumes with Job Description  
✅ Rank candidates based on score  
✅ Show matched & missing skills  
✅ Explainable scoring system (with breakdown)  
✅ Clean and interactive UI using Streamlit  

---

## 🧠 How It Works

### 1. Resume Parsing
- Extracts text from PDF/DOCX using `pdfplumber` and `python-docx`

### 2. Skill Extraction
- Uses keyword matching from a predefined skill set

### 3. Job Description Matching
- Uses **TF-IDF + Cosine Similarity** to compare resume and JD

### 4. Scoring Algorithm

Final score is calculated using:

- Skill Match → 50%  
- Text Similarity → 30%  
- Skill Depth → 20%  

### 5. Ranking
- Candidates are sorted based on final score

---

## 🖥️ Tech Stack

- Python  
- Streamlit  
- Pandas  
- Scikit-learn  
- pdfplumber  
- python-docx  

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/shanusinha26/ai-resume-ranking-system.git
cd ai-resume-ranking-system
2. Create virtual environment
python -m venv venv
venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Run the app
streamlit run app.py
📊 Example

Input:

Job Description

Multiple Resumes

Output:

Ranked candidates

Match score

Matched & Missing skills

🎯 Key Highlights

Explainable AI approach

Real-world use case (Recruitment automation)

Simple yet effective ranking logic

Clean UI for better usability

⚠️ Limitations

Uses keyword-based skill extraction

Does not handle advanced NLP understanding

Supports only PDF and DOCX formats

📌 Future Improvements

Add experience extraction

Improve skill extraction using NLP

Add database integration

Deploy as a web application

👨‍💻 Author

Shanu Sinha
📧 sinhashanu2003@gmail.com

🔗 GitHub: https://github.com/shanusinha26/ai-resume-ranking-system

🔗 LinkedIn: https://www.linkedin.com/in/shanu-sinha-20a6a12b6/