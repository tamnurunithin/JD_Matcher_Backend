import os
import shutil
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.services.document_parser import extract_resume_text
from app.services.grammar_service import find_repeated_words
from app.services.faiss_service import search_resume_matches
from app.services.llm_service import generate_ai_match_analysis

router = APIRouter()

UPLOAD_DIR = "app/uploads/resumes"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/match")
async def match_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    try:
        file_path = os.path.join(UPLOAD_DIR, resume.filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(resume.file, buffer)

        resume_text = extract_resume_text(file_path, resume.filename)

        semantic_matches = search_resume_matches(
            resume_text=resume_text,
            job_description=job_description
        )

        ai_result = generate_ai_match_analysis(
            resume_text=resume_text,
            job_description=job_description,
            semantic_matches=semantic_matches
        )

        grammar_issues = find_repeated_words(resume_text)

        return {
            "ats_score": ai_result.get("ats_score", 0),
            "summary": ai_result.get("summary", ""),
            "matched_skills": ai_result.get("matched_skills", []),
            "missing_skills": ai_result.get("missing_skills", []),
            "improvement_suggestions": ai_result.get("improvement_suggestions", []),
            "tailored_resume_summary": ai_result.get("tailored_resume_summary", ""),
            "grammar_issues": grammar_issues,
            "semantic_matches": semantic_matches[:5],
            "resume_preview": resume_text[:1000],
        }

    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))