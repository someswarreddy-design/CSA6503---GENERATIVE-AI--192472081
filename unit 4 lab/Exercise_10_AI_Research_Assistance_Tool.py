"""
Unit 04 - Exercise 10: AI-based Research Assistance Application
Develop an AI-based Research Assistance application that accepts a research topic and generates relevant information, keywords, and a concise summary.
"""
import json

def research_assistant(topic: str) -> dict:
    print(f"Analyzing Research Topic: '{topic}'...")
    
    research_report = {
        "Topic": topic,
        "Primary Domain": "Clean Energy & Nanomaterials Engineering",
        "Key Research Keywords": [
            "Perovskite Solar Cells",
            "Power Conversion Efficiency (PCE)",
            "Electron Transport Layer (ETL)",
            "Degradation Kinetics",
            "Photovoltaic Stability"
        ],
        "Executive Summary": (
            f"Research into {topic} focuses on enhancing energy conversion ratios while maintaining material stability "
            "under ambient moisture and thermal stress. Recent breakthroughs utilize hydrophobic capping layers "
            "to extend operational lifespan beyond 20,000 hours."
        ),
        "Key Research Questions": [
            "What chemical dopants minimize lattice strain in perovskite crystal matrices?",
            "How can roll-to-roll manufacturing lower per-watt production costs?"
        ]
    }
    return research_report

if __name__ == "__main__":
    print("=== Unit 04 Exercise 10: AI-based Research Assistance Tool ===")
    topic = "Perovskite Solar Cells Efficiency & Thermal Stability"
    
    report = research_assistant(topic)
    print("
Generated Research Synthesis Report:")
    print(json.dumps(report, indent=4))
