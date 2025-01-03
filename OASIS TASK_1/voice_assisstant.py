import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

def speak(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source,timeout=5)
            query = recognizer.recognize_google(audio, language="en-US")
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Could you repeat?")
            return ""
        except sr.RequestError:
            print("Network Error. Please check your connection.")
            return ""
def tell_time():
    now = datetime.datetime.now()
    time_str = now.strftime("%I:%M %p")
    print("The time is "+ time_str+".")
    speak("The time is "+ time_str+".")
def tell_date():
    today=datetime.date.today()
    date_str= today.strftime("%B %d, %Y")
    print("Today's date is"+ date_str+".")
    speak("Today's date is"+ date_str+".")
def search_web(query):
    print("Searching the web for "+query)
    speak("Searching the web for "+query)
    webbrowser.open(f"https://www.google.com/search?q={query}")
def main():
    print("Hello! I am your voice assistant. How can I help you today?")
    speak("Hello! I am your voice assistant. How can I help you today?")
    while True:
        query = recognize_speech()
        if not query:
            continue

        if "hello" in query:
            print("Hello! How can I assist you?")
            speak("Hello! How can I assist you?")
        elif "time" in query:
            tell_time()
        elif "date" in query:
            tell_date()
        elif "search for" in query:
            search_query=query.replace("search for","").strip()
            search_web(search_query)
        elif "exit" in query or "quit" in query:
            print("Goodbye! Have a great day!")
            speak("Goodbye! Have a great day!")
        else:
            print("I'm not sure how to help you with that. Please try again.")
            speak("I'm not sure how to help you with that. Please try again.")
if __name__=="__main__":
    main()