import speech_recognition as sr


def get_audio():
    """
    Get audio from the microphone. 
    The SpeechRecognition package is used to automatically stop listening when the user stops speaking. 

    function returns the raw binary audio string (PCM)
    """
    l = sr.Microphone.list_microphone_names()
    print (l)
    
    r = sr.Recognizer()

    di = l.index("default")
    print ("di", di)

    with sr.Microphone(device_index=di) as source:
    #with sr.Microphone() as source:
        print("listening for audio from microphone")
        #r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        print("listening done")

    # convert audio to raw_data (PCM)
    raw_audio = audio.get_raw_data()

    text = r.recognize_google(audio) ## recognize speech using Google Speech Recognition

    return text

try:
    text = get_audio()
    print("text: %s" % text) 
except Exception as e:
    print(e)
