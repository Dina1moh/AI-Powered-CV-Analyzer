#data_extraction.py
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser
import sys
from pathlib import Path    
import os

sys.path.insert(0, str(Path(__file__).parent.parent))

from cv_analysis.schemas import CVData
from dotenv import load_dotenv
load_dotenv()



OPENAI_API_KEY = os.getenv("OPENAI_API_KEY_BASE")
OPENAI_API_BASE = "https://openrouter.ai/api/v1"
OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME")


llm = ChatOpenAI(
    model=OPENAI_MODEL_NAME,              
    temperature=0,
    openai_api_key=OPENAI_API_KEY,
    openai_api_base="https://openrouter.ai/api/v1",
    )

parser = PydanticOutputParser(pydantic_object = CVData)
def extract_cv_data(cv_text):
    template = """
    Extract the following fields from the CV text and return as JSON:
    Name, Email, Phone, Address, Education (degree, institution, year), 
    Experience (job_title, company, start_date, end_date, description),
    Skills.
    
    {format_instructions}

    CV Text:
    {cv_text}
    """
    prompt = PromptTemplate(
        input_variables = ["cv_text"],
        template=template ,
        partial_variables={"format_instructions": parser.get_format_instructions()}
        
    )
    prompt_and_model = prompt | llm | parser 
    response = prompt_and_model.invoke({"cv_text":cv_text})
    return response
    
    
      