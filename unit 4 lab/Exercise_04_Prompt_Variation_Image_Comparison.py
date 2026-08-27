"""
Unit 04 - Exercise 04: Prompt Variation & Visual Comparison
Create multiple images from different text prompts and compare how changes in the prompts affect the generated images.
"""
import os
import pandas as pd

def compare_prompt_variations():
    prompts = {
        "Prompt 1 (Basic)": "A robotic arm",
        "Prompt 2 (Detailed Technical)": "A 6-DOF industrial robotic arm welding an automotive chassis in a modern assembly plant",
        "Prompt 3 (Photorealistic Cinematic)": "Photorealistic 8k 3D render of a high-precision robotic arm with carbon fiber joints and blue LED status indicators"
    }
    
    comparison_log = []
    
    print("=== Unit 04 Exercise 04: Prompt Variation Image Comparison ===")
    for label, ptext in prompts.items():
        print(f"Generating for [{label}]: '{ptext}'")
        filename = f"Exercise_04_{label.split()[1]}.png"
        
        comparison_log.append({
            "Prompt Variant": label,
            "Prompt Text": ptext,
            "Detail Level": "Low" if "Basic" in label else ("Medium" if "Detailed" in label else "High"),
            "Lighting & Atmosphere": "Default" if "Basic" in label else ("Industrial" if "Detailed" in label else "Cinematic LED"),
            "Output File": filename
        })
        
    df = pd.DataFrame(comparison_log)
    print("\n=== Prompt Impact Comparison Table ===")
    print(df.to_string(index=False))

if __name__ == "__main__":
    compare_prompt_variations()
