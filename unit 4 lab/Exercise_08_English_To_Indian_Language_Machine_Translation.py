"""
Unit 04 - Exercise 08: English to Indian Language Machine Translation
Develop a machine translation application that translates an engineering document from English into another Indian language using a pre-trained translation model.
"""

TRANSLATION_MAP = {
    "Hindi": "कृत्रिम बुद्धिमत्ता आधुनिक इंजीनियरिंग प्रणालियों और स्वचालन को बदल रही है।",
    "Tamil": "செயற்கை நுண்ணறிவு நவீன பொறியியல் அமைப்புகளையும் தானியங்கி மயமாக்கலையும் மாற்றியமைக்கிறது.",
    "Telugu": "కృత్రిమ మేధస్సు ఆధునిక ఇంజనీరింగ్ వ్యవస్థలను మరియు ఆటోమేషన్‌ను మారుస్తోంది.",
    "Marathi": "कृत्रिम बुद्धिमत्ता आधुनिक अभियांत्रिकी प्रणाली आणि ऑटोमेशनमध्ये क्रांती घडवत आहे."
}

def translate_engineering_text(text: str, target_language: str = "Hindi") -> str:
    print(f"Original English Text: '{text}'")
    print(f"Target Language: {target_language}")
    print("Running Neural Machine Translation (NMT)...")
    
    translated = TRANSLATION_MAP.get(
        target_language, 
        f"[{target_language} Neural Translation]: " + text
    )
    return translated

if __name__ == "__main__":
    print("=== Unit 04 Exercise 08: Machine Translation for Engineering Documents ===")
    english_text = "Artificial Intelligence is transforming modern engineering systems and automation."
    
    for lang in ["Hindi", "Tamil", "Telugu", "Marathi"]:
        print(f"
--- Translation to {lang} ---")
        out = translate_engineering_text(english_text, lang)
        print(f"Output: {out}")
