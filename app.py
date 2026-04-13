import os
print(os.listdir())
import streamlit as st
from job_data import jobs
from utils import *
from PyPDF2 import PdfReader
import pandas as pd

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("📄 AI Resume Analyzer (OCR + NLP)")
st.write("Upload your resume to analyze job fit, skills, and suggestions")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF, TXT, Image)",
    type=["pdf", "txt", "png", "jpg", "jpeg"]
)

def read_file(file):
    if file.type == "application/pdf":
        pdf = PdfReader(file)
        text = ""
        for page in pdf.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted
        return text
    elif file.type in ["image/png", "image/jpeg"]:
        return extract_text_from_image(file)
    else:
        return file.read().decode("utf-8")

if uploaded_file:
    with st.spinner("Processing resume..."):
        resume_text = read_file(uploaded_file)
        cleaned_text = clean_text(resume_text)

    st.subheader("Extracted Resume Text")
    st.text_area("Resume Content", resume_text, height=200)

    results = {}

    for job, skills in jobs.items():
        found_skills = extract_skills(cleaned_text, skills)
        score = calculate_score(found_skills, skills)
        missing = get_missing_skills(found_skills, skills)

        results[job] = {
            "score": score,
            "missing": missing,
            "found": found_skills
        }

    sorted_jobs = sorted(results.items(), key=lambda x: x[1]["score"], reverse=True)

    st.subheader("Best Job Match")
    best_job = sorted_jobs[0]
    st.success(f"{best_job[0]} → {best_job[1]['score']}% match")

    st.subheader("Detected Skills")
    if best_job[1]["found"]:
        st.write(", ".join(best_job[1]["found"]))
    else:
        st.write("No relevant skills detected")

    st.subheader("Skill Gaps")
    if best_job[1]["missing"]:
        st.write(", ".join(best_job[1]["missing"]))
    else:
        st.write("No major skill gaps")

    st.subheader("Job Match Scores")
    for job, data in sorted_jobs:
        st.write(f"{job}: {data['score']}%")

    st.subheader("Top 3 Job Roles")
    for job, data in sorted_jobs[:3]:
        st.write(f"{job} → {data['score']}%")

    st.subheader("Job Match Visualization")
    df = pd.DataFrame([
        {"Job": job, "Score": data["score"]}
        for job, data in results.items()
    ])
    st.bar_chart(df.set_index("Job"))

    st.subheader("Resume Improvement Suggestions")
    suggestions = suggest_improvements(cleaned_text)

    if suggestions:
        for s in suggestions:
            st.write(f"- {s}")
    else:
        st.write("Your resume looks strong")

else:
    st.info("Upload a resume to begin")