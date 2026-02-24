
# 📄 AI-Powered CV Analyzer V3

A powerful web application that extracts information from CVs (PDF format) and analyzes how well they match job descriptions using AI-powered analysis. **Now with RAG (Retrieval-Augmented Generation) Agent capabilities!**

![Flask](https://img.shields.io/badge/Flask-2.3.3-green)
![Python](https://img.shields.io/badge/Python-3.8%252B-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-orange)
![LangGraph](https://img.shields.io/badge/LangGraph-Agent-purple)

---

## ✨ Features

- 📄 **PDF CV Processing**: Upload and extract structured data from PDF CVs  
- 🤖 **AI-Powered Analysis**: Uses OpenAI's language models to analyze CV content  
- 💼 **Job Matching**: Compare your CV against job descriptions to get match percentages  
- 📊 **Detailed Insights**: Receive strengths, gaps, recommended skills, and improvement suggestions  
- 🎨 **User-Friendly Interface**: Clean, responsive web interface built with Bootstrap 5  
- 🔌 **RESTful API**: Flask backend with separate API routes for easy integration  
- 📱 **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices  
- 🧠 **RAG Agent System**: Intelligent agent with document search and web search capabilities  
- 📚 **Document Analysis**: Extract insights from PDFs using RAG (Retrieval-Augmented Generation)  
- 🔍 **Multi-Tool Agent**: Powered by LangGraph with search and document_search tools  

---

## 🛠 Technology Stack

- **Backend**: Python Flask  
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5  
- **PDF Processing**: PyPDF, python-docx  
- **AI Integration**: LangChain, OpenAI API, Cohere  
- **Agent Framework**: LangGraph with DeepAgents  
- **Vector Store**: ChromaDB, Langchain-Chroma  
- **Data Validation**: Pydantic  
- **Search Tools**: Google Search Integration  
- **API Design**: RESTful principles  

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher  
- OpenAI API key  
- pip (Python package manager)  
- Virtual environment (recommended)

### Setup Instructions

**1. Clone the repository:**

```bash
git clone <your-repository-url>
cd "AI-Powered CV Analyzer V3"
```

**2. Create and activate virtual environment:**

```bash
# Create virtual environment (Windows)
python -m venv v3

# Activate virtual environment
# On Windows:
v3\Scripts\Activate.ps1

# On macOS/Linux:
source v3/bin/activate
```

**3. Install dependencies:**

```bash
pip install -r requirements.txt
```

**4. Set up environment variables:**  
Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_API_BASE=your_api_base_url_here
OPENAI_MODEL_NAME=gpt-oss-120b
FLASK_ENV=development
```

---

## 🚀 How to Run the Project

### **Option 1: Run the Web Application**

After completing installation, start the Flask application:

```bash
# Make sure virtual environment is activated (v3\Scripts\Activate.ps1 on Windows)

python app.py
```

Open your browser and navigate to:
```
http://localhost:5000
```

The web interface will load with the following features:
- Upload PDF CV
- Extract CV information
- Input job description
- Analyze match percentage
- View recommendations

---

### **Option 2: Test the RAG Agent (Command Line)**

The RAG Agent allows you to ask questions about PDF documents using retrieval-augmented generation.

**Run the test script:**

```bash
# Make sure virtual environment is activated

python AI_Agent/test.py
```

**Example usage in Python:**

```python
from AI_Agent.test import ask_rag_agent

# Define file path and question
file_path = "path/to/your/document.pdf"
query = "What are the main topics covered?"

# Get response
answer = ask_rag_agent(file_path, query)
print(answer)
```

The RAG Agent will:
1. Search the document for relevant information
2. Query web sources if needed
3. Return a comprehensive answer with sources cited

---

### **Option 3: Use the RAG Router API**

```bash
python -c "from routers.rag_router import *; print('RAG Router activated')"
```

The RAG Router provides API endpoints for document-based Q&A without running the web interface.

---

### 1. Upload Your CV
- Click on "Choose PDF File" to select your CV  
- Supported format: PDF only  
- Maximum file size: 16MB  

### 2. View Extracted Information
- Personal details (name, email, phone, address)  
- Education history  
- Work experience  
- Skills list  

### 3. Analyze Job Match
- Paste a job description in the text area  
- Click "Analyze Match" to get detailed analysis  
- Receive match percentage and improvement suggestions  

### 4. Review Results
- **Match Percentage**: Overall compatibility score  
- **Strengths**: Areas where your CV matches well  
- **Gaps**: Missing qualifications or experience  
- **Recommended Skills**: Skills to develop  
- **Improvement Suggestions**: Specific advice to enhance your application  

---

## 📁 Project Structure

```text
AI-Powered CV Analyzer V3/
├── app.py                         # Main Flask application
├── requirements.txt               # Python dependencies
├── .env                           # Environment variables (create this)
│
├── AI_Agent/                      # NEW: RAG Agent System
│   ├── agent.py                   # Agent creation using LangGraph
│   ├── all_tools.py               # Base tools (search, Wikipedia, etc.)
│   ├── rag_tool.py                # Document RAG tool
│   ├── search_tool.py             # Web search integration
│   ├── test.py                    # Testing script for RAG agent
│   └── __init__.py
│
├── cv_analysis/                   # CV Analysis Module
│   ├── data_extraction.py         # Extract CV data using AI
│   ├── match_analysis.py          # Job matching analysis
│   ├── text_extractor.py          # PDF text extraction
│   ├── schemas.py                 # Pydantic data models
│   └── __init__.py
│
├── cover_letter_generator/        # Cover Letter Module
│   ├── cover_letter_creator.py    # Generate cover letters
│   ├── pdf_creator.py             # Create PDF output
│   ├── schemas.py                 # Data models
│   └── __init__.py
│
├── routers/                       # API Routes
│   ├── cv_analysis_router.py      # CV analysis endpoints
│   ├── rag_router.py              # RAG agent endpoints
│   ├── router_cover_letter.py     # Cover letter endpoints
│   └── __init__.py
│
├── static/                        # Frontend Assets
│   ├── css/
│   │   └── style.css              # Custom styles
│   ├── js/
│   │   └── script.js              # Frontend functionality
│   └── temp/                      # Temporary files
│
├── templates/                     # HTML Templates
│   └── index.html                 # Main interface
│
└── v3/                            # Virtual Environment
    ├── Scripts/                   # Python executables
    ├── Lib/                       # Installed packages
    └── pyvenv.cfg                 # Config file
```

---

## 💡 Quick Start Examples

### **Example 1: Ask Questions About a Document**

```python
from AI_Agent.test import ask_rag_agent

# Example: Research paper analysis
result = ask_rag_agent(
    file_path="research_paper.pdf",
    query="What are the main conclusions?"
)
print(result)
```

**Output:**
```
The main conclusions state that...
[Cited from document page 5 and supporting web sources]
```

---

### **Example 2: Using in Flask Route**

```python
from flask import Flask, request, jsonify
from AI_Agent.test import ask_rag_agent

app = Flask(__name__)

@app.route('/api/ask', methods=['POST'])
def ask_question():
    data = request.json
    answer = ask_rag_agent(
        file_path=data['file_path'],
        query=data['query']
    )
    return jsonify({"answer": answer})
```

---

### **Example 3: Processing Multiple Documents**

```python
from AI_Agent.test import ask_rag_agent

documents = [
    ("notes_1.pdf", "Key points from lecture 1?"),
    ("notes_2.pdf", "What topics were covered?"),
    ("summary.pdf", "Summarize the main themes")
]

for doc_path, question in documents:
    answer = ask_rag_agent(doc_path, question)
    print(f"Q: {question}\nA: {answer}\n")
```

---

## 🎯 Use Cases

- 📚 **Academic Research**: Analyze research papers and extract key findings
- 📄 **Document Analysis**: Extract insights from business documents
- 💼 **CV Matching**: Find relevant skills and experience in documents
- 🎓 **Educational**: Learn from lecture notes and study materials
- 📋 **Report Generation**: Summarize and analyze reports
- 🔍 **Information Retrieval**: Search across multiple documents

---

The **RAG (Retrieval-Augmented Generation) Agent** is an intelligent assistant that can answer questions about documents using a combination of document search and web search.

### **Available Tools**

1. **document_search** - Search within provided PDF documents
2. **search** - Web search for general knowledge
3. **Wikipedia** - Retrieve Wikipedia content
4. **Others** - Extensible tool framework

### **How It Works**

```
User Query
    ↓
LangGraph Agent (powered by gpt-oss-120b)
    ├─→ Analyzes query intent
    ├─→ Selects appropriate tools
    ├─→ Executes tool calls
    └─→ Processes results
    ↓
Formatted Answer with Sources
```

### **Example Usage**

```python
from AI_Agent.test import ask_rag_agent

# Ask about a document
pdf_file = "research_paper.pdf"
question = "What are the main findings?"

answer = ask_rag_agent(pdf_file, question)
print(answer)
```

### **Features**

- 📚 **Document-First**: Prioritizes document search before web search
- 🔍 **Multi-Source**: Combines document and web information
- 💡 **Smart Tool Selection**: Automatically chooses the best tool
- ✅ **Source Attribution**: Cites where information comes from
- 🔄 **Iterative Search**: Can refine searches based on results

---

### **POST** `/api/upload-cv`
Upload a PDF CV for processing.  

**Request**: Form-data with PDF file  
**Response**: Structured CV data in JSON format  

---

### **POST** `/api/analyze-job`
Analyze CV match against a job description.  

**Request**: JSON with CV data and job description  

```json
{
  "cv_data": {...},
  "job_description": "Job description text..."
}
```

**Response**: Match analysis results  

```json
{
  "match_percentage": 85.5,
  "strengths": ["Python experience", "Relevant education"],
  "gaps": ["Missing cloud experience"],
  "recommended_skills": ["AWS", "Docker"],
  "improvement_suggestions": ["Highlight project experience"]
}
```

---

### **RAG Agent Endpoints**

#### **POST** `/api/rag/ask`
Ask a question about a document using RAG.

**Request**: 
```json
{
  "file_path": "path/to/document.pdf",
  "query": "Your question here"
}
```

**Response**: 
```json
{
  "answer": "Comprehensive answer with cited sources...",
  "sources": [
    {"type": "document", "page": 1},
    {"type": "web", "url": "https://..."}
  ]
}
```

---

#### **POST** `/api/rag/documents`
Upload a document and embed it for RAG search.

**Request**: Form-data with PDF file  
**Response**: Document ID and embedding status

---

## 🌐 Deployment

### **Deploy to Heroku**
```bash
heroku login
heroku create your-app-name
heroku config:set OPENAI_API_KEY=your_api_key
heroku config:set OPENAI_API_BASE=your_api_base
heroku config:set OPENAI_MODEL_NAME=gpt-oss-120b
git push heroku main
```

**Note for RAG Agent:** Heroku's ephemeral filesystem means ChromaDB vector stores won't persist. Consider using:
- CloudStorage (AWS S3, Google Cloud Storage)
- Database backups before dyno restarts
- Persistent data services layer

---

### **Deploy to PythonAnywhere**
- Upload files to PythonAnywhere  
- Create virtual environment: `mkvirtualenv v3`
- Install dependencies: `pip install -r requirements.txt`
- Configure WSGI file to point to `app.py`  
- Set environment variables in the web app settings  
- Reload web app  

---

### **Deploy to AWS Lambda (Serverless)**
For RAG Agent as serverless function:

```bash
pip install zappa
zappa init
zappa deploy production
```

Advantages:
- Auto-scaling
- Pay per invocation
- No server management

Considerations:
- Cold start latency
- Function timeout limits (15 minutes max)
- Vector store management

---

### **Deploy to Docker**

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV OPENAI_API_KEY=your_key
CMD ["python", "app.py"]
```

Build and run:
```bash
docker build -t cv-analyzer .
docker run -p 5000:5000 cv-analyzer
```




## ⚡ Performance Tips

### **Optimize RAG Agent**

1. **Cache embeddings** - Store ChromaDB collections to avoid re-embedding
   ```python
   # Embeddings are cached automatically in .chroma directory
   ```

2. **Batch document processing**
   ```python
   # Instead of one document at a time
   for doc in documents:
       ask_rag_agent(doc, query)  # Reuses ChromaDB instance
   ```

3. **Use smaller models for faster inference**
   - Use `gpt-3.5-turbo` for speed
   - Use `gpt-4` for accuracy

4. **Limit context window**
   ```python
   # Reduce chunk size for faster search
   # In rag_tool.py: chunk_size=500  # default 1000
   ```

### **Web Application Performance**

1. **Enable pagination** for large CV lists
2. **Use async processing** for file uploads
3. **Implement caching** for repeated analyses
4. **Compress static assets** (CSS, JS)

### **Database Optimization**

1. **Regular ChromaDB maintenance**
   ```bash
   # Clear old embeddings monthly
   rm -rf .chroma
   ```

2. **Use persistent storage**
   - Local: `/data/embeddings/`
   - Cloud: S3 or Google Cloud Storage

---

## ❓ FAQ

**Q: Can I use this without OpenAI?**  
A: The core CV analysis requires OpenAI, but you can extend it with other LLM providers (Cohere, Anthropic, etc.) by modifying `agent.py`.

**Q: Is my data secure?**  
A: PDFs are processed server-side. For deployment, ensure:
- HTTPS is enabled
- Files are deleted after processing
- API keys are never logged
- Use environment variables for secrets

**Q: What's the maximum file size?**  
A: Currently set to 16MB. Larger files can be split into chunks.

**Q: Can I use this for multiple PDFs?**  
A: Yes! Process multiple documents through the RAG agent and it will search across embeddings.

**Q: Does the RAG agent require internet?**  
A: For document_search: No (local)  
For web search tool: Yes  
You can disable web search to work offline.

**Q: How accurate is the job matching?**  
A: Accuracy depends on:
- CV quality and clarity
- Job description completeness
- Model quality (using gpt-oss-120b)
- Always review suggestions manually

**Q: Can I integrate this with my existing app?**  
A: Yes! Use the API endpoints or import functions directly:
```python
from cv_analysis.match_analysis import analyze_match
from AI_Agent.test import ask_rag_agent
```

**Q: How do I handle large documents?**  
A: ChromaDB automatically chunks large PDFs into manageable sizes for embedding.

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository  
2. Create a feature branch: `git checkout -b feature/amazing-feature`  
3. Commit your changes: `git commit -m 'Add amazing feature'`  
4. Push to the branch: `git push origin feature/amazing-feature`  
5. Open a pull request  

---

## 📝 License
This project is licensed under the **MIT License** - see the LICENSE file for details.

---

## 🆘 Troubleshooting

### **General Issues**

| Issue | Solution |
|-------|----------|
| OpenAI API errors | Check API key is valid and has credits |
| PDF not recognized | Ensure PDF is not image-based (use OCR if needed) |
| Virtual environment not found | Run: `python -m venv v3` |
| Module import errors | Run: `pip install -r requirements.txt` |

### **RAG Agent Issues**

| Issue | Solution |
|-------|----------|
| `InvalidUpdateError` in agent | Ensure `invoke()` is called with dict: `{"messages": [...]}` |
| No document search results | Verify PDF file path and format |
| Agent timeout | Increase timeout or split large documents |
| Empty response | Check LLM output; try simpler queries first |

### **Environment Setup**

If you encounter virtual environment issues:

```bash
# Remove old virtual environment
rmdir /s v3  # Windows
rm -rf v3    # Linux/Mac

# Create fresh virtual environment
python -m venv v3

# Activate and reinstall packages
v3\Scripts\Activate.ps1  # Windows
source v3/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

---

## 🆘 Support

If you encounter any issues:
- Check that your OpenAI API key is valid and has sufficient credits  
- Ensure you're using a PDF file (not scanned images)  
- Verify all environment variables are set correctly  
- Check the browser console for JavaScript errors  

For additional support, please open an issue on GitHub.

---

## 🙏 Acknowledgments
- **OpenAI** for the powerful language models  
- **LangChain** and **LangGraph** for the agent framework  
- **Flask** community for the excellent web framework  
- **Bootstrap** for the responsive UI components  
- **PyPDF** team for PDF text extraction capabilities  
- **ChromaDB** for vector storage and retrieval  
- **DeepAgents** for advanced agent capabilities  

---

<div align="center">
Made with ❤️ using Python, Flask, and LangGraph  
<br><br>
<img src="https://img.shields.io/badge/Flask-2.3.3-green" />
<img src="https://img.shields.io/badge/Python-3.8%252B-blue" />
<img src="https://img.shields.io/badge/LangGraph-Agent-purple" />
<img src="https://img.shields.io/badge/OpenAI-GPT--4-orange" />
</div>
