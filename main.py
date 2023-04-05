import pyttsx3 # converts text to speech 
import speech_recognition as sr 
import webbrowser as wb 
import datetime 
import pyjokes 


def speechtext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listenning------->")
        recognizer.adjust_for_ambient_noise(source)# cancell the background noise
        audio = recognizer.listen(source)#listen the voice
        try:
            print("recognizing------>")
            data = recognizer.recognize_google(audio)# it recognize your audio by google 
            return data
        except Exception as e:
            print(e)

# speechtext()

def speak(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')#getting the voice from your system
    engine.setProperty('voice',voices[1].id)# 0 - for male voice 1 for female
    rate = engine.getProperty('rate') #getting speed of voice
    engine.setProperty('rate',140)
    engine.say(x)
    engine.runAndWait()

# speak("hello vijaykumar chauhan , you are my tuter")

if __name__ == "__main__":
    commands = ["jarvis","jarves",'jarvece',"edheeth","google"]

    data1 = speechtext().lower() 
    if data1 ==any[commands]:
        if "your name" in data1 :
            name = "my name is Jarvis"
            speak(name)
        elif "old are you" in data1:
            age = "iam 5 year old"
        elif "created you" in data1:
            speak("I was created by Mr Vijaykumar Chauhan, Who is very good guy")
        elif "time now" in data1:
            time = datetime.datetime.now().strftime("%I%M%p") # i for hour , m for minute , p for am or pm 
            speak(time)


        elif "youtube" in data1:
            wb.open("https://www.youtube.com/")  

        elif "joke" in data1 :
            jokes = pyjokes.get_joke(language="en",category="neutral")
            print(jokes)
            speak(jokes)


    else:
        print("Thankyou")
    
