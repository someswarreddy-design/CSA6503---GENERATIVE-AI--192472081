"""
Unit 02 - Exercise 10: SQL Query Generation using Structured Prompting
Design structured prompts that provide database schema, table details, and requirements to an LLM and generate appropriate SQL queries.
"""

def generate_sql_prompt(db_schema: str, user_query: str) -> str:
    structured_prompt = f"""
[ROLE]: Senior SQL Database Administrator
[DATABASE SCHEMA]:
{db_schema}

[USER REQUIREMENT]: {user_query}

[INSTRUCTIONS]:
- Generate an optimized SQL query matching the database schema.
- Use explicit JOIN syntax where required.
- Do NOT modify table or column names.

[SQL QUERY]:
"""
    return structured_prompt.strip()

if __name__ == "__main__":
    print("=== Unit 02 Exercise 10: SQL Query Generation via Structured Prompting ===")
    
    schema = """
    Table: Students (student_id INT PRIMARY KEY, name VARCHAR, dept_id INT)
    Table: Departments (dept_id INT PRIMARY KEY, dept_name VARCHAR)
    Table: Grades (grade_id INT PRIMARY KEY, student_id INT, course_name VARCHAR, marks INT)
    """
    
    query_req = "Retrieve student names and their department names who scored more than 85 marks in 'Generative AI'."
    
    prompt = generate_sql_prompt(schema, query_req)
    print("Constructed Structured Prompt:\n" + "-"*50 + f"\n{prompt}\n" + "-"*50)
    
    generated_sql = """SELECT s.name, d.dept_name
FROM Students s
JOIN Departments d ON s.dept_id = d.dept_id
JOIN Grades g ON s.student_id = g.student_id
WHERE g.course_name = 'Generative AI' AND g.marks > 85;"""
    
    print("\nGenerated SQL Query Output:")
    print(generated_sql)
