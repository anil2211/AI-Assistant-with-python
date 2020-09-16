import datetime
import pyttsx3 #text to speech
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import webbrowser as wb
import psutil
import pyjokes
# import pyautogui



# text into speech
engine= pyttsx3.init()
voice=engine.getProperty('voices')
engine.setProperty('voice',voice[1].id) #femail voice
newVoiceRate=130    #to control voice rate
engine.setProperty('rate',newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    speak("welcome back Anil...")
    hour=int(datetime.datetime.now().hour)
    if hour>=6  and hour <12:
        speak("Good Morning")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon")
    else:
        speak("Good evening")
    speak("I am lina,How May I help you")            

def takeCommand():
    # It take our voice  and give output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source)
        
    try:
        print("Recognising...")
        query = r.recognize_google(audio,language='en-in')
        # print(f"User said:{query}\n")    
        print("user said:",query)
    except Exception as e:
        print(e)
        speak("Say that again please.....")
        return "None"    
    return query


# speak("Hello Anil..,How may I help you")
    
def time():
    time=datetime.datetime.now().strftime("%H:%M:%S")
    speak(time)
    
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)
    
# time()
# date()    

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('email_address','password')
    server.sendmail('email_address',to,content)
    server.close()


def screenShot():
    img=pyautogui.screenshot()
    img.save("E:\pythonProg\Jarvis_AI\sceenShot.jpg")            
        

def cpu():
    usage=str(psutil.cpu_percent())
    speak("CPU is at " + usage)
    
    battery=psutil.sensors_battery
    speak("battery level is ")
    speak(battery())

def jokes():
    speak(pyjokes.get_joke())
        
if __name__=="__main__":
    # speak("Hello Anil")
    wishMe()
    # while True:
    # if 1:
    while True:
        query=takeCommand().lower()
        # logic for task    
        if 'wikipedia' in query:
            speak("searching wikipedia....Anil")
            query= query.replace("wikipedia","")
            results=wikipedia.summary(query,sentence=3)
            speak("According to wikipedia...")
            print(results)
            speak(results)

        elif 'open youtube' in query:
           webbrowser.open("youtube.com") 

        elif  'open google' in query:
            webbrowser.open("google.com")
        
        elif 'play music' in query:
            music_dir="F:\\VIDEO M\\nandu bhaiya bhajan"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))            

        elif 'time' in query:
            # strTime = datetime.datetime.now().strftime("%H:%M:%S")  
            # # time=datetime.datetime.now().strftime("%H:%M:%S")  
            speak("the current time is...")
            time()
            speak("and today date is ....")
            date()
            
        elif "email" in query:
            try:
                speak("what should I say..?")
                content=takeCommand()
                to="receiver@gmail.com"
                sendmail=(to,content)
                speak("Email sent successfully Anil")
            except Exception as e:
                print(e)
                speak(e)
                speak("Email is not sent successfully...Anil")   
        
        
        elif "search" in query:
            speak("what should I search,Anil?")
            speak("please wait...I am searching")
            search = takeCommand().lower()            
            chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            wb.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
            wb.get('chrome').open_new_tab(search + ".com")
            
        # elif 'logout' in query:
        #     os.system("shutdown-l")
                    
        # elif 'shutdown' in query:
        #     os.system("shutdown /s /t 1")
        
        # elif 'restart' in query:
        #     os.system("shutdown /r /t 1")    
                      
        elif 'remember that' in query:
            speak("what should I remember?")
            data=takeCommand()
            speak("Anil you said me to remember" + data)
            remember=open("E:\pythonProg\Jarvis_AI\data.txt",'w')
            remember.write(data)
            remember.close()
        
        elif "do you know anything" in query:
            remember=open("E:\pythonProg\Jarvis_AI\data.txt","r")
            speak("you said to me remember that" + remember.read())    
                      
        elif "screenshot " in query:
            screenShot()
            speak("screen Shot Done Anil...")
                      
        elif "cpu" in query:
            cpu()
                      
        elif "joke" in query:
            jokes()
                                    
        elif 'offline' in query:
            speak("Good Bye Anil,Have a nice day.")
            quit()    