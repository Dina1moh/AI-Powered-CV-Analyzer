# routers/rag_router.py
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import sys, os, json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from AI_Agent.agent import ask_agent
from AI_Agent.rag_tool import create_rag_tool
from AI_Agent.all_tools import base_tools

rag_bp = Blueprint("rag_router", __name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# =========================
# Helper: Prepare Tools
# =========================
def prepare_tools(file_path=None):
    tools = list(base_tools)
    if file_path:
        rag_tool = create_rag_tool(file_path)
        if rag_tool:
            tools.append(rag_tool)
    return tools

# =========================
# RAG Chat
# =========================
@rag_bp.route("/rag/chat", methods=["POST"])
def rag_chat():
    try:
        message = request.form.get("message")
        if not message:
            return jsonify({"error": "Message is required"}), 400

        # CV Analysis
        cv_analysis_raw = request.form.get("cv_analysis")
        cv_analysis = json.loads(cv_analysis_raw) if cv_analysis_raw else None

        # Optional document
        file = request.files.get("file")
        file_path = None
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)

        tools = prepare_tools(file_path)

        # Ask Agent
        answer = ask_agent(
            message=message,
            cv_analysis=cv_analysis,
            tools=tools
        )

        return jsonify({"success": True, "response": answer})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# =========================
# Health Check
# =========================
@rag_bp.route("/rag/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})