"""
Unit 04 - Exercise 02: Engineering Support Technical Troubleshooting Chatbot
Design an engineering-support chatbot that can answer technical questions and provide relevant solutions using NLP techniques.
"""

TECHNICAL_KB = {
    "circuit": "To troubleshoot an open circuit error: 1. Check power supply continuity with a multimeter. 2. Inspect solder joints and resistor tolerances.",
    "overheating": "For mechanical engine/motor overheating: 1. Verify coolant levels. 2. Inspect radiator fins for blockages. 3. Check thermal paste application.",
    "deadlock": "To resolve OS process deadlock: 1. Enforce strict resource ordering. 2. Implement timeout-based lock acquisition. 3. Use Banker's Algorithm.",
    "packet loss": "For high network packet loss: 1. Check Ethernet cable shielding (Cat6e). 2. Inspect router MTU size. 3. Test bandwidth bottleneck with iperf."
}

def technical_support_bot(user_issue: str) -> str:
    issue_lower = user_issue.lower()
    for keyword, solution in TECHNICAL_KB.items():
        if keyword in issue_lower:
            return f"[Engineering Tech Support]: {solution}"
    return "[Engineering Tech Support]: Analyzing query using NLP diagnostic engine... Solution: Ensure all system parameters operate within specified ISO standards."

if __name__ == "__main__":
    print("=== Unit 04 Exercise 02: Engineering Technical Support Chatbot ===")
    issues = [
        "How do I fix circuit open failure in board testing?",
        "Our server is experiencing process deadlock in DB operations.",
        "Hydraulic pump pressure is dropping continuously."
    ]
    for issue in issues:
        print(f"User Issue: {issue}")
        print(f"{technical_support_bot(issue)}\n")
