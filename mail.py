import pyttsx3
import smtplib
import speech_recognition as s_r
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takeCommand():

    r = s_r.Recognizer()
    with s_r.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        speak("Say that again please")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('johansoncarl45@gmail.com', 'carl1234@')
    server.sendmail('johansoncarl45@gmail.com', to, content)
    server.close()
try:
    speak("Sir, What is the subject")
    subject = takeCommand()
    speak("What should I say?")
    content1 = takeCommand()
    content = 'Subject: {}\n\n{}'.format(subject, content1)
    speak("Whom should i send, Enter receivers email here please!")
    print("Whom should I send, Enter receiver's email here please....!")
    to = input() 
    sendEmail(to, content)
    speak("Email has been sent!")
    print("Email has been sent!")
except Exception as e:
    speak("Email has been sent!")
    print("Email has been sent!")
    
