import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    listener = sr.Recognizer()
    instruction = ""
    try:
        with sr.Microphone() as origin:  # Fixed spelling of Microphone
            print("Listening...")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "jarvis" in instruction:
                instruction = instruction.replace('jarvis', '')
                print(instruction)
    except Exception as e:
        print("Error:", e)
    return instruction.strip()  # Trim whitespace

def play_jarvis():
    instruction = input_instruction()
    print(instruction)
    
    if 'play' in instruction:
        song = instruction.replace("play", "").strip()  # Trim whitespace
        talk("Playing " + song)
        pywhatkit.playonyt(song)
    elif 'time' in instruction:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'date' in instruction:
        date = datetime.datetime.now().strftime('%d/%m/%y')  # Fixed strf to strftime
        talk("Today's date is " + date)
    elif 'how are you' in instruction:
        talk("I am fine, how about you?")
    elif 'what is your name' in instruction:
        talk("I am Jarvis, what can I do for you?")
    elif 'who is' in instruction:
        human = instruction.replace('who is', "").strip()  # Trim whitespace
        info = wikipedia.summary(human, 1)
        print(info)
        talk(info)
    else:
        talk("Please repeat.")

if __name__ == "__main__":
    talk("Hello! I am Jarvis. How can I assist you?")
    play_jarvis()

