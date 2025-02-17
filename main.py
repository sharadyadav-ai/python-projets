import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library
recogniser=sr.Recognizer()
engine= pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def process(c):
    print("opening google")
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif(c.lower()=="skyfall"):
        webbrowser.open("https://www.youtube.com/watch?v=DeumyOzKqgI&pZmFsbA%3D%3Dp=ygUHc2t5")
        print("skyfall")
        
if __name__== "__main__":
    speak("Initializing jarvis.....")
    while True:
        # obtain audio from the microphone
        r = sr.Recognizer()
        # recognize speech using Google Speech Recognition
        try:
        # listening for the wake keyword
            with sr.Microphone() as source:             
                print("listening....")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
                word=r.recognize_google(audio)
            print(r.recognize_google(audio))
            if word.lower()=="hello":
                speak("ya")
                print("jarvis active...")
                #listen for command
                with sr.Microphone() as source:             
                    print("listening....")
                    audio = r.listen(source)
                    command=r.recognize_google(audio)
                    process(command)
        except Exception as e:
            print("Could not request results; {0}".format(e))
