#match_analysis.py
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
import os
from schemas import  MatchAnalysis
from dotenv import load_dotenv
load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_BASE = "https://openrouter.ai/api/v1"
OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME")


llm = ChatOpenAI(
    model=OPENAI_MODEL_NAME,              
    temperature=0,
    openai_api_key=OPENAI_API_KEY,
    openai_api_base="https://openrouter.ai/api/v1",
    )



class JobMatcher:
    def __init__(self):
        self.parser = PydanticOutputParser(pydantic_object=MatchAnalysis)
    
    def analyze_job_match(self, cv_data, job_description):
        template = """
        Analyze the match between this CV and the job description.
        Provide a match percentage, strengths, gaps, recommended skills, and improvement suggestions.
        
        CV Data:
        {cv_data}
        
        Job Description:
        {job_description}
        
        {format_instructions}
        """
        
        prompt = PromptTemplate(
            template=template,
            input_variables=["cv_data", "job_description"],
            partial_variables={"format_instructions": self.parser.get_format_instructions()}
        )
        
        prompt_and_model = prompt | llm | self.parser
        response = prompt_and_model.invoke({
            "cv_data": str(cv_data.dict()),
            "job_description": job_description
        })
        
        return response
     