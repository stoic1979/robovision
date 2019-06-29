import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source,timeout=1,phrase_time_limit=10)
    print('Done, Please wait while we are processing what you said...')
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("Sorry we could not recognize what you said. You can try again.")




