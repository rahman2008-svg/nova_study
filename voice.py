import os

def speak(text):
    os.system(f'espeak "{text}"')

def listen():
    os.system("termux-speech-to-text > voice.txt")

    try:
        with open("voice.txt", "r") as f:
            text = f.read().strip()
    except:
        return ""

    # ❌ ERROR filter
    if "ERROR" in text:
        return ""

    return text.lower()
