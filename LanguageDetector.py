from langdetect import detect as detect_english
from langid import classify as detect_japanese


def detect_language(text):
    try:
        # Detect English
        lang_english = detect_english(text)
        if lang_english == 'en':
            return 'English'

        # Detect Japanese
        lang, confidence = detect_japanese(text)
        if lang == 'ja' and confidence > 0.1:  # Adjust confidence threshold as needed
            return 'Japanese'

        return 'Unknown'

    except Exception as e:
        print(f"Error while detecting language: {e}")
        return 'Unknown'


# Test the language detection
english_text = "This is an example sentence in English."
japanese_text = "これは日本語の例文です。"

print(detect_language(english_text))   # Output: English
print(detect_language(japanese_text))  # Output: Japanese
