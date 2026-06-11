# 📚 AI Notes Assistant

An AI-powered academic notes assistant that helps students quickly understand lengthy PDF notes by generating concise summaries using Google's Gemini API.

## 🚀 Features

* 📄 Upload PDF notes
* 📝 Extract text from PDFs
* 🤖 Generate AI-powered summaries using Gemini
* ⚡ Fast and lightweight (no large model downloads)
* 🎓 Designed for students and academic use

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI Model

* Gemini 2.5 Flash API

### Libraries Used

* PyPDF2
* Streamlit
* Google Generative AI

---

## 📂 Project Structure

```bash
AI_Notes_Assistant/
│
├── app.py
│
├── codess/
│   ├── pdf.py
│   ├── chunks.py
│   └── summarize.py
│
├── requirements.txt
│
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/AI_Notes_Assistant.git
cd AI_Notes_Assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 🔑 API Configuration

Create a Gemini API key from Google AI Studio.

Store the API key securely and configure it before running the application.

---

## 🎯 How It Works

1. User uploads a PDF document.
2. Text is extracted using PyPDF2.
3. Extracted content is sent to Gemini API.
4. Gemini generates a concise summary.
5. Summary is displayed through a Streamlit interface.

---

## 📈 Future Improvements

* Important Question Generator
* Flashcard Generation
* Topic Extraction
* OCR Support for Scanned PDFs
* Multi-language Support
* PDF Chat Feature
* Study Notes Generator

---

## 💡 Use Cases

* College Notes Summarization
* Exam Preparation
* Quick Revision
* Academic Research Assistance
* Study Material Analysis

---

## 👩‍💻 Author

Shagun Ojha

BCA (Machine Learning & Data Science)

Passionate about Artificial Intelligence, Data Science, and Building Practical AI Applications.

---

⭐ If you found this project useful, consider giving it a star.
