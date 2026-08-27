"""
Unit 02 - Exercise 09: Python Code Generation using Structured Prompting
Design structured prompts to instruct an LLM to generate Python programs for specified computational problems and validate the generated code.
"""
import ast

def build_structured_code_prompt(problem_description: str) -> str:
    prompt_template = f"""
[ROLE]: You are an expert Python Software Engineer.
[TASK]: Write a clean, self-contained Python function for the following problem.
[PROBLEM]: {problem_description}
[CONSTRAINTS]:
- Include type hints and docstrings.
- Output ONLY valid executable Python code.
- Do NOT include markdown code blocks or explanatory text.
[OUTPUT SCHEMA]:
def solution():
    ...
"""
    return prompt_template.strip()

def validate_python_code(code_string: str) -> bool:
    try:
        ast.parse(code_string)
        return True
    except SyntaxError as e:
        print(f"Syntax Error in generated code: {e}")
        return False

def generate_and_validate_code(problem: str) -> str:
    prompt = build_structured_code_prompt(problem)
    print("Generated Structured Prompt:\n" + "="*40 + f"\n{prompt}\n" + "="*40)
    
    generated_code = (
        "def is_prime(n: int) -> bool:\n"
        "    \"\"\"Check if a number n is a prime number.\"\"\"\n"
        "    if n <= 1:\n"
        "        return False\n"
        "    for i in range(2, int(n**0.5) + 1):\n"
        "        if n % i == 0:\n"
        "            return False\n"
        "    return True"
    )
    
    is_valid = validate_python_code(generated_code)
    print(f"\nAST Code Validation Result: {'VALID SYNTAX' if is_valid else 'INVALID SYNTAX'}")
    return generated_code

if __name__ == "__main__":
    print("=== Unit 02 Exercise 09: Python Code Generation via Structured Prompting ===")
    problem = "Write a function to check if an integer n is prime."
    code = generate_and_validate_code(problem)
    print("\nGenerated & Validated Python Code:")
    print(code)
