#cover_letter_generator/schemas.py
from pathlib import Path
import sys
import os

sys.path.insert(0, str(Path(__file__).parent.parent))
from pydantic import BaseModel
from typing import List, Optional
from cv_analysis.schemas import CVData, MatchAnalysis

class JobDescription(BaseModel):
    title: str
    company: str
    responsibilities: List[str]
    requirements: List[str]



class CoverLetterRequest(BaseModel):
    job_description: JobDescription
    cv_data: CVData
    match_data: Optional[MatchAnalysis] = None

class CoverLetter(BaseModel):
    content: str




