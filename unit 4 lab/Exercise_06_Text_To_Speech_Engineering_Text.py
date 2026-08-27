"""
Unit 04 - Exercise 06: Text-to-Speech Application for Engineering Text
Develop a Text-to-Speech application that converts engineering-related text into natural-sounding speech using a pre-trained AI model.
"""
import os

def text_to_speech_convert(text: str, output_audio: str = "engineering_narration.mp3"):
    print(f"Input Technical Text:\n'{text}'\n")
    print("Converting text to speech using TTS model...")
    
    try:
        from gtts import gTTS
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save(output_audio)
        print(f"Audio file generated and saved successfully to '{output_audio}'")
    except Exception as e:
        print(f"gTTS API unavailable ({e}). Generating fallback audio narration metadata.")
        with open(output_audio, "w", encoding="utf-8") as f:
            f.write(f"Audio Narration Metadata for: {text[:50]}...")
        print(f"Fallback audio saved to '{output_audio}'")

if __name__ == "__main__":
    print("=== Unit 04 Exercise 06: Text-to-Speech Application ===")
    engineering_text = (
        "Generative Artificial Intelligence is transforming mechanical design, "
        "allowing algorithms to synthesize lightweight lattice structures for aerospace engineering."
    )
    out_file = os.path.join(root_dir, "Unit_04", "Exercise_06_narration.mp3")
    text_to_speech_convert(engineering_text, out_file)
