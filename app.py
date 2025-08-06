import os
import pickle
import numpy as np
import re
from flask import Flask, request, render_template, redirect, url_for, session
from sentence_transformers import SentenceTransformer
import PyPDF2

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Required for session handling
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load BERT model
bert_model = SentenceTransformer("all-MiniLM-L6-v2")

# Load job embeddings
# Load job embeddings
with open("job_embeddings.pkl", "rb") as f:
    data = pickle.load(f)
    print(f"Loaded pickle data length: {len(data)}")  # Debugging

    if len(data) == 5:  # Since job_types is removed
        job_titles, job_descriptions, salary_ranges, certifications, job_embeddings = data
    else:
        raise ValueError("Unexpected data format in job_embeddings.pkl")


# Create job data
jobs = [
    {
        "title": title, 
        "description": desc, 
        "salary_range": salary, 
        "certifications": cert if cert else "No certifications recommended"  # Ensure it's not empty
    }
    for title, desc, salary, cert in zip(job_titles, job_descriptions, salary_ranges, certifications)
]


# Extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with open(pdf_path, "rb") as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                text += page.extract_text() or ""
        return text.strip() if text else None
    except Exception as e:
        print("Error reading PDF:", e)
        return None

# Match jobs using cosine similarity
def match_jobs(resume_text):
    resume_embedding = bert_model.encode([resume_text])[0]
    similarities = np.dot(job_embeddings, resume_embedding)  # Compute similarities
    sorted_indices = np.argsort(similarities)[::-1]  # Sort in descending order

    recommended_jobs = []
    for i in sorted_indices[:3]:  # Take top 3 matches
        job_certifications = certifications[i] if certifications[i] else "No Certifications Recommended"
     
        recommended_jobs.append({
            "title": jobs[i]["title"],
            "description": jobs[i]["description"],
            "salary_range": jobs[i]["salary_range"],
            "certifications": job_certifications,  # Ensure this is passed
            "score": float(similarities[i])
        })
    return recommended_jobs


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        name = request.form.get("name")
        
        # Simple validation
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return render_template("login.html", message="⚠️ Invalid email format!")
        if not password or len(password) < 5:
            return render_template("login.html", message="⚠️ Password must be at least 5 characters!")
        
        session["user"] = name  # Store user in session
        return redirect(url_for("index"))
    
    return render_template("login.html")

@app.route("/resume", methods=["GET", "POST"])
def index():
    if "user" not in session:
        return redirect(url_for("login"))
    
    if request.method == "POST":
        if "resume" not in request.files:
            return render_template("index.html", message="⚠️ No file uploaded!")
        
        resume_file = request.files["resume"]
        if resume_file.filename == "":
            return render_template("index.html", message="⚠️ No file selected!")
        
        resume_path = os.path.join(UPLOAD_FOLDER, resume_file.filename)
        resume_file.save(resume_path)
        
        resume_text = extract_text_from_pdf(resume_path)
        if not resume_text:
            return render_template("index.html", message="⚠️ Could not extract text from resume!")
        
        matched_jobs = match_jobs(resume_text)
        return render_template("results.html", jobs=matched_jobs)
    
    return render_template("index.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


