import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import time
from ecapture import ecapture as ec
import wolframalpha
import requests

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif 12 <= hour < 18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said:{statement}\n")
            return statement
        except sr.UnknownValueError:
            print('UVE')
            speak("I couldn't understand. Please repeat")
            return 0
        except sr.RequestError:
            print('RE')
            speak('There was an error. Please try again later.')
            return 0


def goodbye():
    speak('your personal assistant Smiti is shutting down,Good bye')
    print('your personal assistant Smiti is shutting down,Good bye')


def wikisearch(statement):
    speak('Searching Wikipedia...')
    statement = statement.replace("wikipedia", "")
    results = wikipedia.summary(statement, sentences=3)
    speak("According to Wikipedia")
    print(results)
    speak(results)


def youtube():
    webbrowser.open_new_tab("https://www.youtube.com")
    speak("youtube is open now")
    time.sleep(5)


def google_search():
    webbrowser.open_new_tab("https://www.google.com")
    speak("Google chrome is open now")
    time.sleep(5)


def gmail():
    webbrowser.open_new_tab("gmail.com")
    speak("G Mail open now")
    time.sleep(5)


def time_check():
    string_time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"the time is {string_time}")


def news_search():
    news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
    speak('Here are some headlines from the Times of India,Happy reading')
    time.sleep(6)


def click():
    ec.capture(0, "robo camera", "img.jpg")


def search(statement):
    statement = statement.replace("search", "")
    webbrowser.open_new_tab(statement)
    time.sleep(5)


def ask():
    speak('I can answer to computational and geographical questions  and what question do you want to ask now')
    question = take_command()
    app_id = "5PJJH3-4HWR7WTV24"
    client = wolframalpha.Client(app_id)
    res = client.query(question)
    answer = next(res.results).text
    speak(answer)
    print(answer)


def identify():
    speak('I am Smiti version 1 point O, your personal assistant.')
    speak(' I am programmed to minor tasks like opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather In different cities, get top headline news from times of india and you can ask me computational or geographical questions too!')


def maker():
    speak("I was built by Shrey")
    print("I was built by Shrey")


def weather():
    api_key = "3108b59c062d4e6db6887c16d2ea7f7c"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    speak("what is the city name")
    city_name = take_command()
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        speak(" Temperature in kelvin unit is " +
              str(current_temperature) +
              "\n humidity in percentage is " +
              str(current_humidity) +
              "\n description  " +
              str(weather_description))
        print(" Temperature in kelvin unit = " +
              str(current_temperature) +
              "\n humidity (in percentage) = " +
              str(current_humidity) +
              "\n description = " +
              str(weather_description))


def shopping_list(statement):
    shopping = []
    statement.drop('add', 'to the shopping list')
    shopping = shopping.append(statement)
    return shopping


