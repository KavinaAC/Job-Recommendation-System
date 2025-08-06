import sqlite3
import pickle
from sentence_transformers import SentenceTransformer

# Load Sentence-BERT model
bert_model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to SQLite database
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

# Fetch job details, ensuring we retrieve certifications
cursor.execute("SELECT title, description, salary_range, certifications FROM jobs")
job_rows = cursor.fetchall()

# Separate job details
job_titles = [row[0] for row in job_rows]
job_descriptions = [row[1] for row in job_rows]
salary_ranges = [row[2] for row in job_rows]

# Ensure certifications exist, replace None values with an empty string
certifications = [", ".join(row[3]) if isinstance(row[3], (list, tuple)) else str(row[3]) for row in job_rows]

# Generate BERT embeddings for job descriptions
job_embeddings = bert_model.encode(job_descriptions)

print(f"Generated job embeddings shape: {job_embeddings.shape}")
# Save job details and embeddings into a pickle file (with certifications)
with open("job_embeddings.pkl", "wb") as f:
    pickle.dump((job_titles, job_descriptions, salary_ranges, certifications, job_embeddings), f)

# Close database connection
conn.close()

print("✅ Job embeddings regenerated successfully!")
