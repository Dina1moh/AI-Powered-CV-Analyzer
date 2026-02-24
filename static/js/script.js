// Global State
let cvData = null;
let matchData = null;

// Extract CV
async function extractCV() {
    const fileInput = document.getElementById("cvFile");
    if (!fileInput.files.length) return alert("Please upload a CV file");

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    const res = await fetch("/extract", { method: "POST", body: formData });
    const data = await res.json();
    if (data.error) return alert(data.error);

    cvData = data;
    displayList("cvResult", data);
}

// Match Job
async function matchJob() {
    const jobDescriptionText = document.getElementById("jobDescription").value;
    if (!cvData) return alert("Extract CV first");

    const res = await fetch("/match", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ cv_data: cvData, job_description: jobDescriptionText })
    });
    const data = await res.json();
    matchData = data;
    displayList("matchResult", data);
}

// Generate Cover Letter
async function generateCoverLetter() {
    const jobDescriptionText = document.getElementById("jobDescription").value;
    if (!cvData || !matchData) return alert("Run CV extraction and match first");

    const jobDescription = {
        title: "Unknown",
        company: "Unknown",
        responsibilities: jobDescriptionText.split("\n"),
        requirements: []
    };

    const res = await fetch("/generate_cover_letter", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ cv_data: cvData, match_data: matchData, job_description: jobDescription })
    });
    const data = await res.json();
    if (data.error) return alert(data.error);

    document.getElementById("coverLetterResult").innerHTML = `<ul><li>${data.content.replace(/\n/g,"</li><li>")}</li></ul>`;
}

// Download Cover Letter PDF
async function downloadCoverLetter() {
    const content = document.getElementById("coverLetterResult").innerText;
    if (!content) return alert("Generate cover letter first");

    const res = await fetch("/download_cover_letter", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ content })
    });
    const data = await res.json();
    if (data.pdf_url) window.open(data.pdf_url, "_blank");
}

// RAG Chat
async function sendRagMessage() {
    const messageInput = document.getElementById("ragMessage");
    const fileInput = document.getElementById("ragFile");
    const message = messageInput.value;
    if (!message) return;

    const formData = new FormData();
    formData.append("message", message);

    if (cvData && matchData) {
        // Create cv_analysis dictionary for agent
        const cv_analysis = {
            match_percentage: matchData.match_percentage,
            strengths: matchData.strengths,
            gaps: matchData.gaps,
            recommended_skills: matchData.recommended_skills,
            improvement_suggestions: matchData.improvement_suggestions || []
        };
        formData.append("cv_analysis", JSON.stringify(cv_analysis));
    }

    if (fileInput.files.length) formData.append("file", fileInput.files[0]);

    const res = await fetch("/rag/chat", { method: "POST", body: formData });
    const data = await res.json();
    if (data.success) appendChat("AI", data.response);
    else appendChat("Error", data.error);

    messageInput.value = "";
}

// Helpers
function displayList(elementId, obj) {
    const container = document.getElementById(elementId);
    container.innerHTML = "<ul>" + Object.entries(obj).map(([key, value]) =>
        `<li><strong>${key}:</strong> ${value}</li>`).join("") + "</ul>";
}

function appendChat(sender, text) {
    const chatBox = document.getElementById("chatBox");
    const msg = document.createElement("div");
    msg.className = "chat-message";
    msg.innerHTML = `<strong>${sender}:</strong> ${text}`;
    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
}