import json
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from app.config import GROQ_API_KEY, GROQ_MODEL

def get_llm():
    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY is missing. Add it in Render environment variables or backend/.env.")

    return ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name=GROQ_MODEL,
        temperature=0.2,
    )

def generate_ai_match_analysis(resume_text: str, job_description: str, semantic_matches):
    llm = get_llm()

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """
You are an ATS resume matching expert.
Return only valid JSON.
Do not include markdown.

JSON format:
{{
  "ats_score": number,
  "summary": "short explanation",
  "matched_skills": ["skill"],
  "missing_skills": ["skill"],
  "improvement_suggestions": ["suggestion"],
  "tailored_resume_summary": "improved resume summary"
}}
"""
        ),
        (
            "human",
            """
Resume:
{resume_text}

Job Description:
{job_description}

Semantic FAISS Matches:
{semantic_matches}
"""
        )
    ])

    chain = prompt | llm

    response = chain.invoke({
        "resume_text": resume_text[:6000],
        "job_description": job_description[:4000],
        "semantic_matches": semantic_matches[:10],
    })

    try:
        return json.loads(response.content)
    except json.JSONDecodeError:
        return {
            "ats_score": 0,
            "summary": response.content,
            "matched_skills": [],
            "missing_skills": [],
            "improvement_suggestions": [],
            "tailored_resume_summary": "",
        }