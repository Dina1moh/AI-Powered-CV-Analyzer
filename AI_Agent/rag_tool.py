# rag_tool.py
import sys
import sys
from pathlib import Path    
import os
sys.path.insert(0, str(Path(__file__).parent.parent))
from dotenv import load_dotenv
import cohere
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_core.tools import Tool
from langchain_cohere import CohereEmbeddings
# Load environment variables
load_dotenv(override=True)
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
EMBEDDING_MODEL_ID = os.getenv("EMBEDDING_MODEL_ID")

def load_document(file_path):
    """
    Load a document from the given file path.
    Supports .pdf, .docx, and .txt extensions.
    Returns a list of LangChain Document objects.
    """
    try:
        # Check if file exists first
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            return []
            
        _, ext = os.path.splitext(file_path.lower())
        if ext == ".pdf":
            loader = PyPDFLoader(file_path)
        elif ext == ".docx":
            loader = Docx2txtLoader(file_path)
        elif ext == ".txt":
            loader = TextLoader(file_path)
        else:
            print(f"Unsupported file type: {file_path}")
            return []
            
        docs = loader.load()
        return docs
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return []

def chunk_data(documents, chunk_size=512, chunk_overlap=50):
    """
    Split documents into smaller chunks for embedding.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_documents(documents)

def create_rag_tool(file_path: str):
    """
    Create a retriever tool dynamically for the given file path.
    Returns None if the file is invalid.
    """
    # Check if file exists first
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return None
        
    # Load document
    documents = load_document(file_path)
    if not documents:
        print("No valid documents loaded.")
        return None

    try:
        # 1. Split into chunks
        chunks = chunk_data(documents)

        # 2. Setup embedding
        cohere_client = cohere.Client(COHERE_API_KEY)
        embedding = CohereEmbeddings(
            model=EMBEDDING_MODEL_ID,
            client=cohere_client,
            user_agent="langchain-client"
        )

        # 3. Create vector store
        vector_store = Chroma.from_documents(documents=chunks, embedding=embedding,collection_name="rag_collection")

                # 4. Create retriever tool
        retriever = vector_store.as_retriever(search_kwargs={"k": 3})
        return Tool(
            name="document_search",
            func=retriever.invoke,
            description=f"Use this tool to search for information in the uploaded document: {os.path.basename(file_path)}. Use it for questions specifically about this document. If the information is not found, you should explicitly state that and then use other search tools."
        )
    except Exception as e:
        print(f"Error creating RAG tool: {e}")
        return None
     
