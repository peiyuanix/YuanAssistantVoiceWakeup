from google_speech import Speech

def say(text, speed="1.1"):
    lang = 'zh-cn'
    speech = Speech(text, lang)
    sox_effects = ("speed", speed)
    speech.play(sox_effects=sox_effects)