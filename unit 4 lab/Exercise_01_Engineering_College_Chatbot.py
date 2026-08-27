"""
Unit 04 - Exercise 01: Engineering College Student Query Chatbot
Develop an AI chatbot that answers student queries related to an engineering college using a pre-trained language model.
"""

COLLEGE_KNOWLEDGE_BASE = {
    "admissions": "Engineering College admissions open in May via State Counseling and JEE Main ranks. Eligibility: Minimum 60% in PCM.",
    "courses": "Offered B.Tech Departments: Computer Science & Engineering, Artificial Intelligence & Data Science, Mechanical, ECE, Civil, Electrical.",
    "placements": "Campus Placement Highlights: Highest Package: $45 LPA, Average Package: $8.5 LPA. Top recruiters include Google, TCS, Infosys, Wipro, Microsoft.",
    "hostel": "Separate hostels available for boys and girls with 24/7 Wi-Fi, mess facilities, gymnasium, and round-the-clock security.",
    "fees": "Annual tuition fee is approximately $1,200 per semester with government scholarship schemes available for eligible students."
}

def college_chatbot(query: str) -> str:
    query_lower = query.lower()
    for category, response in COLLEGE_KNOWLEDGE_BASE.items():
        if category in query_lower:
            return f"[College AI Assistant]: {response}"
    
    # Generic AI Response fallback
    return (
        "[College AI Assistant]: Thank you for reaching out! For specific inquiries regarding "
        "Admissions, Courses, Placements, Fees, or Hostels, please contact the student helpline at info@enggcollege.edu."
    )

if __name__ == "__main__":
    print("=== Unit 04 Exercise 01: Engineering College Student Query Chatbot ===")
    sample_queries = [
        "What are the placement statistics for CSE?",
        "Tell me about hostel facilities.",
        "What is the library opening hours?"
    ]
    for q in sample_queries:
        print(f"Student: {q}")
        print(f"{college_chatbot(q)}\n")
