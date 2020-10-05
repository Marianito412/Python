import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty("voices")

for voice in voices:
    print(f"Voice: {voice}")
    print(f"Id: {voice.id}")
    engine.setProperty("voice", voice.id)
    engine.say("Hello")
    engine.runAndWait()