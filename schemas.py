# schemas.py
from pydantic import BaseModel, Field
from typing import List, Optional

class Education(BaseModel):
    degree: str = Field(..., description="The degree obtained (e.g., BSc Computer Science)")
    institution: str = Field(..., description="The name of the educational institution")
    year: Optional[str] = Field(None, description="Year of graduation or study period")

class Experience(BaseModel):
    job_title: str = Field(..., description="Title of the job position (e.g., Software Engineer)")
    company: str = Field(..., description="Company name where the job was held")
    start_date: Optional[str] = Field(None, description="Start date of the job (YYYY-MM format)")
    end_date: Optional[str] = Field(None, description="End date of the job (YYYY-MM format)")
    description: Optional[str] = Field(None, description="Description of responsibilities and achievements in this role")

class CVData(BaseModel):
    name: str = Field(..., description="Full name of the person")
    email: str = Field(..., description="Email address of the person") 
    phone: Optional[str] = Field(None, description="Phone number of the person")
    address: Optional[str] = Field(None, description="Home address of the person")
    education: List[Education] = Field(default_factory=list, description="List of educational qualifications")
    experience: List[Experience] = Field(default_factory=list, description="List of work experiences")
    skills: List[str] = Field(default_factory=list, description="List of professional skills")

class MatchAnalysis(BaseModel):
    match_percentage: float = Field(..., description="Overall match percentage between CV and job description")
    strengths: List[str] = Field(..., description="List of strengths and matching qualifications")
    gaps: List[str] = Field(..., description="List of gaps or missing qualifications")
    recommended_skills: List[str] = Field(..., description="List of recommended skills to acquire")
    improvement_suggestions: List[str] = Field(..., description="Specific suggestions to improve job application")