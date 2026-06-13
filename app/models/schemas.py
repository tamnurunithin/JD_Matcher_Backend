from pydantic import BaseModel
from typing import List

class MatchResponse(BaseModel):
    ats_score: int
    summary: str
    matched_skills: List[str]
    missing_skills: List[str]
    improvement_suggestions: List[str]
    tailored_resume_summary: str
    grammar_issues: List[str]
    resume_preview: str