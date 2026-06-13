import re

COMMON_SKILLS = [
    "python", "java", "javascript", "react", "node", "sql", "mongodb",
    "fastapi", "flask", "django", "machine learning", "deep learning",
    "nlp", "langchain", "faiss", "rag", "llm", "groq", "openai",
    "html", "css", "git", "docker", "aws", "azure", "api",
    "pandas", "numpy", "scikit-learn", "tensorflow", "pytorch",
    "communication", "microsoft office", "cyber security"
]

def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower())

def extract_skills(text: str):
    normalized = normalize_text(text)
    return [skill for skill in COMMON_SKILLS if skill in normalized]

def analyze_match(resume_text: str, job_description: str):
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(job_description)

    matched_skills = sorted(list(set(resume_skills) & set(jd_skills)))
    missing_skills = sorted(list(set(jd_skills) - set(resume_skills)))

    ats_score = 0
    if jd_skills:
        ats_score = int((len(matched_skills) / len(set(jd_skills))) * 100)

    return {
        "ats_score": ats_score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
    }