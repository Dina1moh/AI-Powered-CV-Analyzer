# Main application file for the AI-Powered CV Analyzer and Cover Letter Generator
from pathlib import Path 
import sys
import os
sys.path.insert(0, str(Path(__file__).parent.parent))
from routers.cv_analysis_router import api_bp as api_app
from routers.router_cover_letter import cover_bp as cover_letter_bp
from routers.rag_router import rag_bp as rag_router_bp
from flask import Flask, render_template

app = Flask(__name__, 
            static_folder='static',
            template_folder='templates')
            
app.register_blueprint(api_app)
app.register_blueprint(cover_letter_bp)
app.register_blueprint(rag_router_bp)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)