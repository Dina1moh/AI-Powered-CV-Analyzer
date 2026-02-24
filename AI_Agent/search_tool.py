# Tools_search.py
from dotenv import load_dotenv 
import os
from langchain_community.utilities import SerpAPIWrapper
from langchain.tools import tool

# Load API key
load_dotenv()
serpapi_key = os.getenv("BING_SUBSCRIPTION_KEY")

serpapi = SerpAPIWrapper(serpapi_api_key=serpapi_key)

@tool
def search(query: str) -> str:
    """Useful for searching the web"""
    return serpapi.run(query)

