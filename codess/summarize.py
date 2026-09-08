import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not configured.")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_summary(chunks):

    text = "\n\n".join(chunks)

    prompt = f"""
You are an AI academic notes assistant.

Summarize the following study material for a college student.

Make the response:
- Clear
- Concise
- Well structured
- Easy to revise
- Exam oriented

Use this structure:

## 📌 Overview

## 🔑 Key Concepts

## 📝 Important Points

## 🎯 Exam Focus

Do not add information that is not present in the notes.

Study material:

{text[:15000]}
"""

    response = model.generate_content(prompt)

    if not response.text:
        raise ValueError("The AI returned an empty response.")

    return response.text