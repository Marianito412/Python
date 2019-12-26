import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak Anything :")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source, timeout=5, phrase_time_limit=5)
    r.adjust_for_ambient_noise(source)
    try:
        text = r.recognize_google(source)
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize what you said")