import speech_recognition as sr
import pyttsx3 as pt
import subprocess as sp
import pywhatkit as pwk
import datetime
# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
speech = pt.init()
def speak(text):
    speech.say(text)
    speech.runAndWait()
# Function to recognize speech
def listen():
    with sr.Microphone() as source:
        print("Speak...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for noise
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print(f"User said: {query}\n")
        except Exception as e:
            print("Sorry Dhruv, I could not understand. Can you please repeat?")
            query = None

    return query
# Function to greet the user based on the time of the day
def greet():
    current_hour = datetime.datetime.now().hour
    if 0 <= current_hour < 12:
        speak("Good morning Dhruv!")
    elif 12 <= current_hour < 18:
        speak("Good afternoon Dhruv!")
    else:
        speak("Good evening Dhruv!")

# Main function
def main():
    print("WELCOME TO YOUR DOST")
    speak("WELCOME TO YOUR DOST")
    greet()
    speak("I am your voice assistant. How can I help you ?")

    while True:
        query = listen()

        if query:
            if "hello" in query.lower():
                print("Hello! How can I help you Dhruv?")
                speak("Hello! How can I help you Dhruv?")
            elif "what is the time" in query.lower()or "current time" in query.lower():
                current_time = datetime.datetime.now().strftime("%H:%M")
                print(f"The time is {current_time}")
                speak(f"The time is {current_time}")
            elif "open chrome" in query.lower():
                print("Opening Chrome...")
                speak("Opening Chrome")
                sp.Popen([r"C:\Program Files\Google\Chrome\Application\chrome.exe"])
            elif "open youtube" in query.lower():
                print("Opening Youtube...")
                speak("Opening Youtube")
                pwk.playonyt("Play Despacito")
            elif "thank you" in query.lower():
                print("you're welcome")
                speak("you're welcome")
            elif "exit" in query.lower() or "quit" in query.lower() or "bye" in query.lower():
                print("Goodbye Dhruv!")
                print("Have a nice day!")
                speak("Goodbye Dhruv!")
                speak("Have a nice day!")
                break
            else:
                speak("Sorry, I don't understand. Can you please repeat?")

if __name__ == "__main__":
    main()
