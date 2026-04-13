import re
import pytesseract
import numpy as np
import cv2

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def clean_text(text):
    text = text.lower()
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
    return text


def extract_text_from_image(uploaded_file):
    file_bytes = np.asarray(bytearray(uploaded_file.getvalue()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    gray = cv2.medianBlur(gray, 3)

    thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]

    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(thresh, config=custom_config)

    return text


def extract_skills(resume_text, job_keywords):
    found_skills = []
    resume_words = set(resume_text.split())

    for skill in job_keywords:
        skill_words = skill.split()
        if all(word in resume_words for word in skill_words):
            found_skills.append(skill)

    return found_skills


def calculate_score(resume_skills, job_skills):
    match = len(set(resume_skills) & set(job_skills))
    score = (match / len(job_skills)) * 100
    return round(score, 2)


def get_missing_skills(resume_skills, job_skills):
    return list(set(job_skills) - set(resume_skills))


def suggest_improvements(text):
    suggestions = []

    if "project" not in text:
        suggestions.append("Add a projects section")

    if "experience" not in text:
        suggestions.append("Mention work experience or internships")

    if not any(char.isdigit() for char in text):
        suggestions.append("Add measurable achievements (e.g., increased efficiency by 20%)")

    if "skills" not in text:
        suggestions.append("Add a clear skills section")

    if len(text.split()) < 150:
        suggestions.append("Resume content is too short, add more details")

    return suggestions