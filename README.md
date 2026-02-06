# 📄 Contract Analysis & Risk Assessment Bot

🔗 **Live App:** https://contract-risk-bot-11.streamlit.app  
🎥 **Demo Video:** [<paste-your-youtube-or-drive-link-here> ](https://drive.google.com/file/d/1EaBJvi4f2Ti0QBcSNwIHNk7JgaCtnucu/view?usp=sharing) 
💻 **GitHub Repo:** https://github.com/adityasingh-0803/contract-risk-bot  

---

## 🚀 Problem Statement

Small and medium businesses often struggle to understand complex legal contracts.  
Hidden clauses such as penalties, indemnity, auto-renewals, and non-compete terms may expose them to financial and legal risks.

Manual legal review is:
- expensive
- slow
- requires lawyers

---

## 💡 Solution

We built a **GenAI-powered Contract Risk Assessment Bot** that:

✅ extracts contract clauses  
✅ detects risky terms  
✅ scores risk levels (Low / Medium / High)  
✅ explains clauses in simple business language  
✅ generates downloadable reports  

This helps SMEs quickly understand contracts and make safer decisions.

---

## ✨ Features

- 📂 Upload contracts (PDF / DOCX / TXT)
- 🔍 Automatic clause extraction
- ⚠️ Clause-level risk scoring
- 🧠 Plain-English explanations
- 📊 Risk summary dashboard
- 📥 CSV export for legal review
- 🌐 Live deployed web app

---

## 🖥️ Demo

### Steps:
1. Upload contract file
2. System analyzes clauses
3. View risk levels & explanations
4. Download report

---

## 🧠 How It Works

Pipeline:

Upload → Text Extraction → Clause Splitting → Risk Detection → Explanation → Dashboard

---

## 🛠️ Tech Stack

- Python
- Streamlit
- spaCy (NLP)
- Rule-based risk engine
- LLM (optional GenAI reasoning)
- GitHub + Streamlit Cloud deployment

---

## 📁 Project Structure
```bash
contract-risk-bot/
│
├── app.py
├── requirements.txt
├── utils/
│ ├── extractor.py
│ ├── clause_splitter.py
│ ├── risk_engine.py
│ ├── llm_analyzer.py
├── sample_contracts/
```

---

## ⚙️ Run Locally

```bash
git clone <repo>
cd contract-risk-bot
pip install -r requirements.txt
streamlit run app.py
```

## 📈 Impact
```bash
⏱️ Reduces contract review time by 80%

💰 Saves legal consultation costs

🛡️ Helps SMEs avoid hidden risks

📑 Makes contracts easy to understand
```
## 👨‍💻 Author

Aditya Singh
Built for HCL × GUVI Hackathon
