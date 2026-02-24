# app/cover_letter_routes.py
import sys
from pathlib import Path
from flask import Blueprint, request, jsonify
from cover_letter_generator.cover_letter_creator import CoverLetterCreator
from cover_letter_generator.schemas import JobDescription, CoverLetter
from cover_letter_generator.pdf_creator import create_pdf
from cv_analysis.schemas import CVData, MatchAnalysis

cover_bp = Blueprint("cover", __name__)
creator = CoverLetterCreator()

# =========================
# Helper: Parse job description text
# =========================
def parse_job_description(text: str) -> JobDescription:
    lines = text.strip().split("\n")
    return JobDescription(
        title=lines[0] if len(lines) > 0 else "N/A",
        company=lines[1] if len(lines) > 1 else "N/A",
        responsibilities=lines[2].split(";") if len(lines) > 2 else [],
        requirements=lines[3].split(";") if len(lines) > 3 else []
    )

# =========================
# Generate Cover Letter
# =========================
@cover_bp.route("/generate_cover_letter", methods=["POST"])
def generate_cover_letter():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No JSON payload provided"}), 400

        job_desc_input = data.get("job_description")
        if isinstance(job_desc_input, str):
            job_description = parse_job_description(job_desc_input)
        elif isinstance(job_desc_input, dict):
            job_description = JobDescription(**job_desc_input)
        else:
            return jsonify({"error": "Invalid job_description format"}), 400

        cv_data_input = data.get("cv_data")
        if not cv_data_input:
            return jsonify({"error": "cv_data is required"}), 400
        cv_data = CVData(**cv_data_input)

        match_data_input = data.get("match_data")
        match_data = MatchAnalysis(**match_data_input) if match_data_input else None

        cover_letter: CoverLetter = creator.create_cover_letter(
            cv_data=cv_data,
            match_data=match_data,
            job_description=job_description
        )

        return jsonify(cover_letter.model_dump())
    except Exception as e:
        print(f"Error generating cover letter: {e}")
        return jsonify({"error": str(e)}), 500

# =========================
# Download Cover Letter PDF
# =========================
@cover_bp.route("/download_cover_letter", methods=["POST"])
def download_cover_letter():
    try:
        data = request.json
        if not data or "content" not in data:
            return jsonify({"error": "No content provided"}), 400

        content = data["content"]
        output_dir = Path("static/temp")
        output_dir.mkdir(parents=True, exist_ok=True)
        file_path = output_dir / "cover_letter.pdf"

        create_pdf(content, str(file_path))
        return jsonify({"pdf_url": f"/static/temp/cover_letter.pdf"})
    except Exception as e:
        print(f"Error creating PDF: {e}")
        return jsonify({"error": str(e)}), 500