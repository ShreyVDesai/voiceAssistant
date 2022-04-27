from functions import *

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')

print("Loading your AI personal assistant Smiti")
speak("Loading your AI personal assistant Smiti")
wish_me()


def main():
    if __name__ == '__main__':

        while True:
            speak("Tell me how can I help you now?")
            statement = take_command()
            if type(statement) == str:
                statement.lower()
                if statement == 0:
                    continue

                if "goodbye" in statement or "ok bye" in statement or "stop" in statement:
                    goodbye()
                    return 0

                if 'wikipedia' in statement:
                    wikisearch(statement)

                elif 'open youtube' in statement:
                    youtube()

                elif 'open google' in statement:
                    google_search()

                elif 'open gmail' in statement:
                    gmail()

                elif 'time' in statement:
                    time_check()

                elif 'news' in statement:
                    news_search()

                elif "camera" in statement or "photo" in statement or 'click' in statement:
                    click()

                elif 'search' in statement:
                    search(statement)

                elif 'ask' in statement:
                    ask()

                elif 'who are you' in statement or 'what can you do' in statement:
                    identify()

                elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
                    maker()

                elif "weather" in statement:
                    weather()

                elif "shopping" in statement:
                    shopping_list(statement)

                else:
                    print("This functionality hasn't been programmed yet")
                    speak("This functionality hasn't been programmed yet")
            else:
                main()


main()
