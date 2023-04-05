import pyttsx3
import datetime 
import speech_recognition 
import wikipedia
import os 
import random
import psutil # get cpu information 
import pyautogui # used to take screenshot
import pyjokes 
import webbrowser as wb 
import requests
from newsapi import NewsApiClient
import json 

engine = pyttsx3.init()

def speak(audio):
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',160)
    engine.say(audio)
    engine.runAndWait()

def gettime():
    Time = datetime.datetime.now().strftime('%I:%M:%S')
    speak(f"Sir,now the time is {Time}")

def cpu():
    cpupercentage = str(psutil.cpu_percent())
    speak("The CPU is at:"+cpupercentage)
    battery = psutil.sensors_battery()
    speak("The Battery is at:")
    speak(battery.percent)

def getdate():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    speak(f"Today's date is:{day},{month},{year}")

def Wishme():
    speak("Welcome Back Sir!")
    hour = datetime.datetime.now().hour
    if hour>=6 and hour <=12:
        speak("Good Morning Sir!")
    elif hour>=12 and hour <=18:
        speak("Good Afternoon Sir!")
    elif hour>=18 and hour <=24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")
    gettime()
    getdate()
    speak("Veronika at your Service, please tell me how can i help you sir?")

def take():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source :
        print("Listening......")
        r.pause_threshold = 1 #wait for 2 seconds
       
        audio = r.listen(source)
    try:
        print("Recognizing......")
        query = r.recognize_google(audio,language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Say it Again Please?")
        return "None"
    return query


SCREENSHOT_DIR = "F:\\Python-projects\\Voice assistant\\screenshots"
def screenshot():
    img = pyautogui.screenshot()
    img.save(os.path.join(SCREENSHOT_DIR, 'ss.png'))
    speak("Screenshot has been taken, sir!")


def getjokes():
    joke = pyjokes.get_joke()
    speak(joke)

    
def getNews(topic=None):
    api_key = "5f6151e723ee450faeb1f0e68708755d"
    
    if topic:
        url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={api_key}"
    else:
        url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"

    response = requests.get(url)
    data = json.loads(response.text)

    if data["status"] == "ok":
        articles = data["articles"]
    
        for article in articles:
            title = article["title"]
            description = article["description"]
            url = article["url"]
            
            speak(title)
            print(title)
            speak(description)
            print(description)
            print(url)
    else:
        print("Error retrieving news articles")

def websearch(url):
    try:
        res = wb.open(url)
        speak("I found these results!")
        for r in res:
            print(res)
            speak(r)
    except Exception as e:
        speak("Sorry, I couldn't find any results for that search.")

def get_weather_forecast(city_name):
    
    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
    querystring = {"q": city_name, "days": "3"}
    headers = {
        "X-RapidAPI-Key": "613960fe5fmshf4c4db2fe555666p14620ejsncae73a3448c8",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    if "forecast" in data:
        forecast = data["forecast"]["forecastday"][0]["day"]
        condition = forecast["condition"]["text"]
        temp_c = forecast["avgtemp_c"]
        temp_f = forecast["avgtemp_f"]
        wind_speed = forecast["maxwind_kph"]
        speak(f"The weather forecast for {city_name} is {condition}.")
        speak(f"The average temperature for today is {temp_c} degrees Celsius or {temp_f} degrees Fahrenheit.")
        speak(f"The maximum wind speed for today is {wind_speed} kilometers per hour.")
    else:
        speak("Sorry, I couldn't find the weather forecast for that city.")


if __name__ =="__main__":
    # Wishme()
    while True:
        query = take().lower()

        if 'time' in query :
            gettime()
        elif 'date' in query:
            getdate()
        elif 'wikipedia' in query:
            speak("Searching....")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)
        elif 'logout' in query:
            os.system("shutdown -1")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif "play" in query or "play music" in query:
            song_dir = "E:\\songs"
            song_list = os.listdir(song_dir)
            random_num = random.randrange(0,len(song_list))
            os.startfile(os.path.join(song_dir,song_list[random_num]))
        
        elif "remember that" in query:
            speak("What should I remember!")
            data = take()
            speak("you said me to remember that"+data)
            remember = open("data.txt",'w')
            remember.write(data)
            remember.close()
   
        elif "do you know anything" in query:
            remember = open('data.txt','r')
            speak("you said me to remember that"+remember.read())

        elif "screenshot" in query:
            screenshot()
            speak("screen shot has been taken sir! ")
        
        elif "cpu" in query:
            cpu()
        
        elif "joke" in query:
            getjokes()

        elif "search" in query:
            search = take()
            speak("Searching...")
            websearch(search)
        
        elif "weather report" in query:
            speak("Sure, which city's weather report do you want to know?")
            city_name = take()
            get_weather_forecast(city_name)
        elif 'news' in query:
            speak("which type of news you want me to tell!")
            inp = take()
            getNews(inp)
        elif "thank you" in query:
            speak("You are most welcome sir!")

        elif "exit"or 'stop' or 'quit'or 'offline' in query:
            quit()

      
