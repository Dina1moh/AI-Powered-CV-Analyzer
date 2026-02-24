from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser
import sys
from pathlib import Path    
import os
sys.path.insert(0, str(Path(__file__).parent.parent))
from cover_letter_generator.schemas import CoverLetter, JobDescription
from cv_analysis.schemas import CVData, MatchAnalysis

from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY_BASE")
OPENAI_API_BASE = "https://openrouter.ai/api/v1"
OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME")

llm = ChatOpenAI(
    model=OPENAI_MODEL_NAME,
    temperature=0,
    openai_api_key=OPENAI_API_KEY,
    openai_api_base=OPENAI_API_BASE,
)


class CoverLetterCreator:
    def __init__(self):
        self.parser = PydanticOutputParser(pydantic_object=CoverLetter)

    def create_cover_letter(
        self,
        cv_data: CVData,
        match_data: MatchAnalysis,
        job_description: JobDescription
    ):
        experience_text = "; ".join(
            [f"{exp.job_title} at {exp.company} ({exp.start_date or 'N/A'} - {exp.end_date or 'N/A'})"
             for exp in cv_data.experience]
        )

        template = """
        Create a professional cover letter based on the CV analysis and job description.

        Candidate Info:
        Name: {cv_name}
        Skills: {skills}
        Experience: {experience}

        Match Analysis:
        Strengths: {strengths}
        Gaps: {gaps}
        Recommended Skills: {recommended_skills}

        Job Description:
        Title: {job_title}
        Company: {company}
        Responsibilities: {responsibilities}
        Requirements: {requirements}

        {format_instructions}
        """

        prompt = PromptTemplate(
            template=template,
            input_variables=[
                "cv_name", "skills", "experience",
                "strengths", "gaps", "recommended_skills",
                "job_title", "company", "responsibilities", "requirements"
            ],
            partial_variables={"format_instructions": self.parser.get_format_instructions()}
        )

        chain = prompt | llm | self.parser

        response = chain.invoke({
            "cv_name": cv_data.name,
            "skills": ", ".join(cv_data.skills),
            "experience": experience_text,
            "strengths": ", ".join(match_data.strengths if match_data else []),
            "gaps": ", ".join(match_data.gaps if match_data else []),
            "recommended_skills": ", ".join(match_data.recommended_skills if match_data else []),
            "job_title": job_description.title,
            "company": job_description.company,
            "responsibilities": ", ".join(job_description.responsibilities),
            "requirements": ", ".join(job_description.requirements),
        })

        return response
