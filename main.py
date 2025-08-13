import speech_recognition as sr
import webbrowser 
import pyttsx3
import musiclibrary

r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "Open Google" in c.lower():
        webbrowser.open("https://google.com")
    elif "Open youtube" in c.lower():
         webbrowser.open("https://youtube.com")
    elif "Open linkedin" in c.lower():
         webbrowser.open("https://linkedin.com")
    elif "Open facebook" in c.lower():
         webbrowser.open("https://facebook.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    


if __name__=="__main__":
    speak("Initianlizing Jarvis....")
    while True:
    # listen for the wake word jarvis
    # get audio from microphone
        r = sr.Recognizer()
       
# recognize speech using Sphinx
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("listening")
                audio = r.listen(source, timeout=2 , phrase_time_limit=1)
            command = r.recognize_google(audio)
            if(command.lower() == "Jarvis"):
                speak("ya")
                #listen for command

                with sr.Microphone() as source:
                    print("jarvis active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("error; {0}".format(e))

    