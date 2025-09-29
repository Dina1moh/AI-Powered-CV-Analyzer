# cv_extractor/router.py
from flask import Blueprint, request, jsonify
import tempfile
import os
from text_extractor import get_pdf_text
from data_extraction import extract_cv_data
from match_analysis import JobMatcher
from flask_cors import CORS

api_bp = Blueprint('api', __name__)
CORS(api_bp)

@api_bp.route('/api/upload-cv', methods=['POST'])
def upload_cv():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if not file.filename.lower().endswith('.pdf'):
        return jsonify({'error': 'File must be a PDF'}), 400
    
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
            file.save(tmp_file.name)
            tmp_path = tmp_file.name
        
        cv_text = get_pdf_text(tmp_path)
        cv_data = extract_cv_data(cv_text)
        
        os.unlink(tmp_path)
        
        return jsonify({
            'success': True,
            'cv_data': cv_data.dict()
        })
    
    except Exception as e:
        if 'tmp_path' in locals() and os.path.exists(tmp_path):
            os.unlink(tmp_path)
        return jsonify({'error': str(e)}), 500

@api_bp.route('/api/analyze-job', methods=['POST'])
def analyze_job():
    try:
        data = request.get_json()
        cv_data_dict = data.get('cv_data')
        job_description = data.get('job_description')
        
        if not cv_data_dict or not job_description:
            return jsonify({'error': 'CV data and job description are required'}), 400
        
        from schemas import CVData
        cv_data = CVData(**cv_data_dict)
        
        job_matcher = JobMatcher()
        analysis = job_matcher.analyze_job_match(cv_data, job_description)
        
        return jsonify({
            'success': True,
            'analysis': analysis.dict()
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500