#
# a quick test for speech to text
#

import speech_recognition as sr


def main():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print ('say something')
        audio = r.listen(source)
        print ('done')
    try:
        text = r.recognize_google(audio)
        print('Neo said:\n' + text)
    except Exception as e:
        print (e)


if __name__ == "__main__":
    main()
