# To test the speech input and output operations

import win32com.client as wincl
import speech_recognition as sr
import pocketsphinx

spk = wincl.Dispatch("SAPI.SpVoice")
spk.Speak('''Good to see you Sir, Dazzor, at your service.''')
spk.Speak("Please Enter the text")
txt = input()
spk.Speak("You just entered %s" % txt)

rec = sr.Recognizer()
with sr.Microphone() as src:
    rec.adjust_for_ambient_noise(src, duration=1)
    rec.energy_threshold += 280
    print("Say something!")
    audio = rec.listen(src)

# recognize speech using Sphinx
try:
    print("Sphinx thinks you said " + rec.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks you said " + rec.recognize_google(audio))

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))




