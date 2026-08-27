"""
Unit 04 - Exercise 09: AI-based Resume Screening & Candidate Ranking System
Develop an AI-based Resume Screening application that analyses candidate resumes and ranks them according to a given engineering job description.
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def rank_resumes(job_description: str, resumes: dict) -> pd.DataFrame:
    documents = [job_description] + list(resumes.values())
    candidate_names = list(resumes.keys())
    
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(documents)
    
    # Calculate Cosine Similarity between Job Description (index 0) and Resumes (index 1..)
    scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    
    results = []
    for name, score in zip(candidate_names, scores):
        results.append({
            "Candidate Name": name,
            "Match Score": f"{round(score * 100, 2)}%",
            "Raw Similarity": round(score, 4)
        })
        
    df = pd.DataFrame(results).sort_values(by="Raw Similarity", ascending=False)
    return df

if __name__ == "__main__":
    print("=== Unit 04 Exercise 09: AI-based Engineering Resume Screening System ===")
    
    jd = """
    Target Position: Senior DevOps & Cloud Infrastructure Engineer
    Required Skills: Python, Docker, Kubernetes, AWS, Terraform, CI/CD pipelines, Linux kernel, monitoring tools.
    """
    
    candidates = {
        "Alice Smith": "Experienced DevOps Engineer proficient in Docker, Kubernetes, AWS cloud architectures, Terraform, and Python automation.",
        "Bob Jones": "Frontend developer specializing in React.js, HTML5, CSS3, JavaScript, web design, and UI components.",
        "Charlie Brown": "Cloud administrator skilled in Linux system administration, Python scripting, AWS infrastructure, CI/CD, and Docker."
    }
    
    print(f"Job Description:\n{jd.strip()}\n")
    ranked_df = rank_resumes(jd, candidates)
    print("=== Candidate Ranking Results ===")
    print(ranked_df[["Candidate Name", "Match Score", "Raw Similarity"]].to_string(index=False))
