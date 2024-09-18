import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os




engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice

engine.setProperty('voice', voices[0].id)

def speak(audio):

    engine.say(audio) 

    engine.runAndWait() 
'''Without this command, speech will not be audible to us'''
def wishme():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning..")
    elif hour>=12 and hour<18:
        speak("good afternoon..")
    else:
        speak("good evening..")
    speak("i am siri please tell me how can i help you")            
def takeCommand():
    '''It takes microphone input from the user and returns string output'''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5 # Adjust pause threshold
        try:
            audio = r.listen(source, timeout=5)  # Listen for 1 second
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start.")
            return "None"
        
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        #print(e)    
        #print("Say that again please...")   
        return "None" 
    return query  
if __name__ == "__main__":
    wishme()
    while True:
        # if 1:
        query = takeCommand().lower() 
        if 'wikipedia' in query: 
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)  

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
    
            
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open chrome' in query:
            webbrowser.open("chrome.com")    
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            
        elif 'open notepad' in query:
            speak("Opening Notepad")
            os.startfile("notepad.exe") 
        elif 'open code' in query:
            codepath = "C:\\Users\\admin\\Desktop\\miniprojects\\vs code\\desktop_assistant.py"
            if os.path.isfile(codepath):
               os.startfile(codepath)
               speak("Opening your code file in vs code.")
            else:
                speak("Sorry, I could not find that file.")









 
     

     

    

   

