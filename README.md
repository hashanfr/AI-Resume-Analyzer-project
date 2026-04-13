# AI Resume Analyzer

An AI-powered web application that analyzes resumes by extracting text from PDF and image files, evaluating skills, and matching candidates to suitable job roles with actionable feedback.

---

## Features

* Supports PDF, text, and image-based resumes
* Extracts text using OCR (Tesseract + OpenCV)
* Performs skill detection using NLP techniques
* Matches resumes with multiple job roles
* Calculates job-fit scores
* Identifies missing skills (skill gap analysis)
* Provides resume improvement suggestions
* Displays results with an interactive dashboard

---

## Tech Stack

* Python
* Streamlit
* OpenCV
* Tesseract OCR
* Pandas
* NumPy

---

## Project Structure

```
ai_resume_analyzer/
│
├── app.py
├──requirements.txt
├── job_data.py
├── utils.py
```

---

## How to Run

```bash
git clone https://github.com/hashanfr/AI-Resume-Analyzer-project.git
cd AI-Resume-Analyzer-project
pip install -r requirements.txt
streamlit run app.py
```

---

## How It Works

1. Upload a resume (PDF/Image/Text)
2. Extract text using OCR (for images)
3. Clean and process text data
4. Match extracted skills with predefined job roles
5. Calculate job match scores
6. Display:

   * Best job match
   * Skill gaps
   * Suggestions
   * Visual charts

---

## Output

* Job match percentage
* Top 3 suitable roles
* Detected skills
* Missing skills
* Improvement suggestions

---

## Future Improvements

* AI-based resume feedback using LLMs
* Advanced NLP for better skill extraction
* Resume ranking system for recruiters
* Deployment as a live web application

---

## Author

Hashanthra K
