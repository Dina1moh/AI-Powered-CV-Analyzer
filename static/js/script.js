document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('uploadForm');
    const fileInput = document.getElementById('cvFile');
    const submitBtn = document.getElementById('submitBtn');
    const loadingSpinner = document.getElementById('loadingSpinner');
    const errorAlert = document.getElementById('errorAlert');
    const cvResults = document.getElementById('cvResults');
    const jobAnalysisSection = document.getElementById('jobAnalysisSection');
    const analyzeJobBtn = document.getElementById('analyzeJobBtn');
    const jobAnalysisSpinner = document.getElementById('jobAnalysisSpinner');
    const jobAnalysisResults = document.getElementById('jobAnalysisResults');
    
    let cvData = null;

    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        if (!fileInput.files[0]) {
            showError('Please select a PDF file');
            return;
        }
        
        // Show loading state
        loadingSpinner.classList.remove('d-none');
        submitBtn.disabled = true;
        errorAlert.classList.add('d-none');
        
        const formData = new FormData();
        formData.append('file', fileInput.files[0]);
        
        try {
            const response = await fetch('/api/upload-cv', {
                method: 'POST',
                body: formData
            });
            
            const data = await response.json();
            
            if (!response.ok) {
                throw new Error(data.error || 'An error occurred');
            }
            
            // Store CV data
            cvData = data.cv_data;
            
            // Display CV results
            displayCVResults(cvData);
            
            // Show job analysis section
            jobAnalysisSection.classList.remove('d-none');
            cvResults.classList.remove('d-none');
            
        } catch (error) {
            showError(error.message);
        } finally {
            // Hide loading state
            loadingSpinner.classList.add('d-none');
            submitBtn.disabled = false;
        }
    });
    
    analyzeJobBtn.addEventListener('click', async function() {
        const jobDescription = document.getElementById('jobDescription').value.trim();
        
        if (!jobDescription) {
            showError('Please enter a job description');
            return;
        }
        
        // Show loading state for job analysis
        jobAnalysisSpinner.classList.remove('d-none');
        analyzeJobBtn.disabled = true;
        
        try {
            const response = await fetch('/api/analyze-job', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    cv_data: cvData,
                    job_description: jobDescription
                })
            });
            
            const data = await response.json();
            
            if (!response.ok) {
                throw new Error(data.error || 'An error occurred during analysis');
            }
            
            // Display job analysis results
            displayJobAnalysis(data.analysis);
            
        } catch (error) {
            showError(error.message);
        } finally {
            // Hide loading state
            jobAnalysisSpinner.classList.add('d-none');
            analyzeJobBtn.disabled = false;
        }
    });
    
    function displayCVResults(data) {
        const cvDataContent = document.getElementById('cvDataContent');
        
        let html = `
            <div class="row">
                <div class="col-md-6">
                    <div class="section-header">Personal Information</div>
                    <div class="result-item">
                        <p><strong>Name:</strong> ${data.name || 'Not specified'}</p>
                        <p><strong>Email:</strong> ${data.email || 'Not specified'}</p>
                        <p><strong>Phone:</strong> ${data.phone || 'Not specified'}</p>
                        <p><strong>Address:</strong> ${data.address || 'Not specified'}</p>
                    </div>
                </div>
        `;
        
        // Education
        html += `
            <div class="col-md-6">
                <div class="section-header">Education</div>
        `;
        
        if (data.education && data.education.length > 0) {
            data.education.forEach(edu => {
                html += `
                    <div class="result-item">
                        <p><strong>Degree:</strong> ${edu.degree || 'Not specified'}</p>
                        <p><strong>Institution:</strong> ${edu.institution || 'Not specified'}</p>
                        <p><strong>Year:</strong> ${edu.year || 'Not specified'}</p>
                    </div>
                `;
            });
        } else {
            html += `<p>No education information found</p>`;
        }
        
        html += `</div></div>`;
        
        // Experience
        html += `
            <div class="row mt-3">
                <div class="col-12">
                    <div class="section-header">Work Experience</div>
        `;
        
        if (data.experience && data.experience.length > 0) {
            data.experience.forEach(exp => {
                html += `
                    <div class="result-item">
                        <p><strong>Job Title:</strong> ${exp.job_title || 'Not specified'}</p>
                        <p><strong>Company:</strong> ${exp.company || 'Not specified'}</p>
                        <p><strong>Period:</strong> ${exp.start_date || 'Not specified'} to ${exp.end_date || 'Present'}</p>
                        ${exp.description ? `<p><strong>Description:</strong> ${exp.description}</p>` : ''}
                    </div>
                `;
            });
        } else {
            html += `<p>No work experience found</p>`;
        }
        
        html += `</div></div>`;
        
        // Skills
        html += `
            <div class="row mt-3">
                <div class="col-12">
                    <div class="section-header">Skills</div>
                    <div class="result-item">
        `;
        
        if (data.skills && data.skills.length > 0) {
            html += `<div class="d-flex flex-wrap">`;
            data.skills.forEach(skill => {
                html += `<span class="skill-badge">${skill}</span>`;
            });
            html += `</div>`;
        } else {
            html += `<p>No skills found</p>`;
        }
        
        html += `</div></div></div>`;
        
        cvDataContent.innerHTML = html;
    }
    
    function displayJobAnalysis(analysis) {
        let html = `
            <div class="alert alert-success">
                <h4>Match Analysis Results: <strong class="match-percentage">${analysis.match_percentage}%</strong></h4>
            </div>
            
            <div class="row">
                <div class="col-md-6">
                    <div class="section-header">Strengths</div>
                    <div class="result-item">
                        <ul class="list-group">
        `;
        
        analysis.strengths.forEach(strength => {
            html += `<li class="list-group-item strength-item">✓ ${strength}</li>`;
        });
        
        html += `
                        </ul>
                    </div>
                    
                    <div class="section-header mt-4">Recommended Skills</div>
                    <div class="result-item">
                        <div class="d-flex flex-wrap">
        `;
        
        analysis.recommended_skills.forEach(skill => {
            html += `<span class="skill-badge bg-warning text-dark">${skill}</span>`;
        });
        
        html += `
                        </div>
                    </div>
                </div>
                
                <div class="col-md-6">
                    <div class="section-header">Gaps</div>
                    <div class="result-item">
                        <ul class="list-group">
        `;
        
        analysis.gaps.forEach(gap => {
            html += `<li class="list-group-item gap-item">✗ ${gap}</li>`;
        });
        
        html += `
                        </ul>
                    </div>
                    
                    <div class="section-header mt-4">Improvement Suggestions</div>
                    <div class="result-item">
                        <ul class="list-group">
        `;
        
        analysis.improvement_suggestions.forEach(suggestion => {
            html += `<li class="list-group-item">💡 ${suggestion}</li>`;
        });
        
        html += `
                        </ul>
                    </div>
                </div>
            </div>
        `;
        
        jobAnalysisResults.innerHTML = html;
    }
    
    function showError(message) {
        errorAlert.textContent = message;
        errorAlert.classList.remove('d-none');
        
        // Hide the message after 5 seconds
        setTimeout(() => {
            errorAlert.classList.add('d-none');
        }, 5000);
    }
});