
# 📄 AI-Powered CV Analyzer

A powerful web application that extracts information from CVs (PDF format) and analyzes how well they match job descriptions using AI-powered analysis.

![Flask](https://img.shields.io/badge/Flask-2.3.3-green)
![Python](https://img.shields.io/badge/Python-3.8%252B-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5%252B-orange)

---

## ✨ Features

- 📄 **PDF CV Processing**: Upload and extract structured data from PDF CVs  
- 🤖 **AI-Powered Analysis**: Uses OpenAI's language models to analyze CV content  
- 💼 **Job Matching**: Compare your CV against job descriptions to get match percentages  
- 📊 **Detailed Insights**: Receive strengths, gaps, recommended skills, and improvement suggestions  
- 🎨 **User-Friendly Interface**: Clean, responsive web interface built with Bootstrap 5  
- 🔌 **RESTful API**: Flask backend with separate API routes for easy integration  
- 📱 **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices  

---

## 🛠 Technology Stack

- **Backend**: Python Flask  
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5  
- **PDF Processing**: PyPDF  
- **AI Integration**: LangChain, OpenAI API  
- **Data Validation**: Pydantic  
- **API Design**: RESTful principles  

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher  
- OpenAI API key  
- pip (Python package manager)  

### Setup Instructions
Clone the repository:

```bash
git clone <your-repository-url>
cd cv_extractor
```

Create a virtual environment (recommended):

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Set up environment variables:  
Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL_NAME=gpt-3.5-turbo
FLASK_ENV=development
```

Run the application:

```bash
python app.py
```

Open your browser and navigate to:

```
http://localhost:5000
```

---

## 🚀 Usage

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
cv_extractor/
├── app.py                 # Main Flask application
├── router.py              # API routes (separated from main app)
├── text_extractor.py      # PDF text extraction functionality
├── data_extraction.py     # CV data extraction using AI
├── match_analysis.py      # Job matching analysis
├── schemas.py             # Pydantic data models
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (create this)
├── static/
│   ├── css/
│   │   └── style.css      # Custom styles
│   └── js/
│       └── script.js      # Frontend functionality
└── templates/
    └── index.html         # Main HTML template
```

---

## 🔧 API Endpoints

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

## 🌐 Deployment

### Deploy to **Heroku**
```bash
heroku login
heroku create your-app-name
heroku config:set OPENAI_API_KEY=your_api_key
heroku config:set OPENAI_MODEL_NAME=gpt-3.5-turbo
git push heroku main
```

### Deploy to **PythonAnywhere**
- Upload files to PythonAnywhere  
- Create virtual environment and install dependencies  
- Configure WSGI file to point to `app.py`  
- Set environment variables in the console  
- Reload web app  

### Deploy to **Vercel/Netlify** (with Flask)
Note: For serverless deployment, you may need to use **Flask-Vercel** or similar adapters.  

---

## 🔒 Environment Variables

| Variable           | Description                                   | Required |
|--------------------|-----------------------------------------------|----------|
| `OPENAI_API_KEY`   | Your OpenAI API key                           | Yes      |
| `OPENAI_MODEL_NAME`| OpenAI model to use (default: gpt-3.5-turbo) | No       |
| `FLASK_ENV`        | Flask environment (development/production)    | No       |

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
- **Flask** community for the excellent web framework  
- **Bootstrap** for the responsive UI components  
- **PyPDF** team for PDF text extraction capabilities  

---

<div align="center">
Made with ❤️ using Python and Flask  
<br><br>
<img src="https://img.shields.io/badge/Flask-2.3.3-green" />
<img src="https://img.shields.io/badge/Python-3.8%252B-blue" />
<img src="https://img.shields.io/badge/OpenAI-GPT--3.5%252B-orange" />
</div>
