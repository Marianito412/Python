import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init()

r = sr.Recognizer()
mic = sr.Microphone(device_index=1)

a = sr.Microphone.list_microphone_names()
for i in a:
    print(i, a.index(i))
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

j = r.recognize_google(audio)
engine.say(j)
engine.runAndWait()
