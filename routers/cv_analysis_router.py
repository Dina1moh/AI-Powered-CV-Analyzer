# routers/cv_analysis_router.py
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import sys
from pathlib import Path
import os

sys.path.insert(0, str(Path(__file__).parent.parent))
from cv_analysis.data_extraction import extract_cv_data
from cv_analysis.match_analysis import JobMatcher
from cv_analysis.text_extractor import get_pdf_text
from cv_analysis.schemas import CVData

api_bp = Blueprint("api", __name__)
job_matcher = JobMatcher()

# =========================
# Extract CV
# =========================
@api_bp.route("/extract", methods=["POST"])
def extract():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    cv_text = get_pdf_text(file)
    cv_data = extract_cv_data(cv_text)
    return jsonify(cv_data.model_dump())

# =========================
# Match Job
# =========================
@api_bp.route("/match", methods=["POST"])
def match():
    data = request.json
    cv_data_dict = data.get("cv_data")
    job_description = data.get("job_description")

    if not cv_data_dict or not job_description:
        return jsonify({"error": "cv_data and job_description are required"}), 400

    cv_data = CVData(**cv_data_dict)
    result = job_matcher.analyze_job_match(cv_data, job_description)
    return jsonify(result.model_dump())