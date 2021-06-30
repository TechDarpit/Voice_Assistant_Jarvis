import pyttsx3
import datetime
import requests
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import sys
import pywhatkit
import smtplib
import pyautogui
import psutil
import wolframalpha
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime('%I:%M %p')

    if hour >= 6 and hour < 12:
        speak(f"Good morning sir, it's {tt}")
    elif hour >= 12 and hour < 18:
        speak(f"Good afternoon sir, it's {tt}")
    elif hour >= 18 and hour < 24:
        speak(f"Good Evening sir, it's {tt}")
    else:
        speak(f"Good night sir, it's {tt}")
    speak("Jarvis at your service. Please tell me how can i help you?")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('darpit.patel@gamil.com', 'Your_Password')
    server.sendmail('darpit.patel@gmail.com', to, content)
    server.close()

def playSong():
    music_dir = 'E:\\Songs'
    songs = os.listdir(music_dir)
    songNum = random.randint(0, len(songs) - 1)
    os.startfile(os.path.join(music_dir, songs[songNum]))

def getData():
    IPAddr = requests.get('https://api.ipify.org').text
    url = 'https://get.geojs.io/v1/ip/geo/' + IPAddr + '.json'
    geo_requests = requests.get(url)
    geo_data = geo_requests.json()
    city = geo_data['city']
    api_key = "ab01cdef23gh04ijklm5no06025a42da" # (Enter Your Api Key) open weather ma api key
    base_url = "http://api.openweathermap.org/data/2.5/weather?units=metric"
    complete_url = base_url + "&q=" + city + "&appid=" + api_key
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        z = x["weather"]

    Data = {
        'current_ip':requests.get('https://api.ipify.org').text,
        'current_city':geo_data['city'],
        'current_state':geo_data['region'],
        'current_country':geo_data['country'],
        'current_temperature':y["temp"],
        'current_pressure':y["pressure"],
        'current_humidity':y["humidity"],
        'weather_description':z[0]["description"]
    }
    return Data

brLinks = {
    'youtube':'www.youtube.com',
    'google':'www.google.com',
    'gfg':'www.geeksforgeeks.org',
    'git':'https://github.com/',
    'linkedin':'www.linkedin.com',
    'marwadi login':'https://login.marwadiuniversity.ac.in:553/',
    'gtu login':'www.student.gtu.ac.in',
    'instagram': 'https://www.instagram.com/',
    'thunkable': 'https://x.thunkable.com/projects',
    'marwadi gdrive': 'https://drive.google.com/drive/u/1/my-drive',
    'mu classroom': 'https://classroom.google.com/u/1/h',
    'meet':'https://meet.google.com/',
    'gmail':'mail.google.com',
    'google drive': 'https://drive.google.com/',
    'map': 'https://www.google.com/maps',
    'docs': 'https://docs.google.com/',
    'sheets': 'https://docs.google.com/',
}

appPath ={
    'whatsapp':'C:\\Users\\Admin\\AppData\\Local\\WhatsApp\\WhatsApp.exe',
    'vs code':'C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe',
    'wps':'C:\\Users\\Admin\\AppData\\Local\\Kingsoft\\WPS Office\\ksolaunch.exe /prometheus /fromksolaunch /from=startmenu',
    'xampp':'C:\\xampp\\xampp-control.exe',
    'chrome':'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    'firefox':'C:\\Program Files\\Mozilla Firefox\\firefox.exe',
    'exlipse': 'C:\\Users\\Admin\\eclipse\\java-2020-062\\eclipse\\eclipse.exe',
    'spotify':'C:\\Users\\Admin\\AppData\\Roaming\\Spotify\\Spotify.exe',
    'control panel':'Control.exe',
    'wordpad':'wordpad.exe',
    'paint': 'mspaint.exe',
    'notepad': 'notepad.exe',
    'snipping tool': 'SnippingTool.exe',
    'step recorder': 'psr.exe',
    'character map': 'charmap.exe',
    'task manager':'taskmgr.exe',
    'cmd':'cmd.exe',
    'magnifier':'magnify.exe',
    'on screen keyboard':'osk.exe'
}

winApp = {
    'skype':'Microsoft.SkypeApp_kzf8qxf38zg5c!App',
    'alarm clock':'Microsoft.WindowsAlarms_8wekyb3d8bbwe!App',
    'camera':'Microsoft.WindowsCamera_8wekyb3d8bbwe!App',
    'calculator':'Microsoft.WindowsCalculator_8wekyb3d8bbwe!App',
    'store':'Microsoft.WindowsStore_8wekyb3d8bbwe!App',
    'weather':'Microsoft.BingWeather_8wekyb3d8bbwe!App',
    'ludo king':'Gametion.LudoKing_d44gk3wcm1v88!App'
}

e_mail = {
    'malay':'malay.patel2045@gmail.com',
    'shruti':'shruti@gmail.com',
    'darpit':'darpitpatel2008@gmail.com',
    'gaurang':'gaurangdalsaniya@gmail.com'
}

contact_no = {
    'malay':'+919408221057',
    'shruti':'+911234567890',
    'darpit':'+919427822846',
    'gaurang':'+919081791605'
}

def takeComand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        command = r.recognize_google(audio, language='en-in')

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    command = command.lower()
    return command

def taskExecution():
    greet()
    speak('Sir, wait for few seconds i am fetching some data.')
    data = getData()
    speak('Now i am ready to take command.')
    # print(data)
    while True:
        command = takeComand()
        print(f"User Said: {command}")
        if 'wikipedia' in command:
            try:
                speak('Searching Wikipedia...')
                command = command.replace("wikipedia", "")
                results = wikipedia.summary(command, 2)
                speak("According to wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                print(e)
                speak("Sorry sir i am not able to search, Please try again.")

        elif 'open' in command or 'start' in command:
            if 'open' in command:
                appName = command.replace("open ", "")
            else:
                appName = command.replace("start ", "")
            if appName in appPath:
                path = appPath[appName]
                if path != "":
                    speak(f"Opening {appName}")
                    os.startfile(path)
                else:
                    speak("path not found...")

            elif appName in brLinks:
                link = brLinks[appName]
                if link != "":
                    speak(f"Opening {appName}")
                    webbrowser.open(link)
                else:
                    speak("link not found...")

            elif appName in winApp:
                app = winApp[appName]
                if app != "":
                    speak(f"Opening {appName}")
                    os.system('start explorer shell:appsfolder\\' + app)
                else:
                    speak("app not found...")

            elif 'drive' in appName:
                try:
                    drive = appName.replace(" drive", "")
                    os.startfile(f"{drive}:\\")
                    speak(f"opening {drive} drive")
                except Exception as e:
                    print(e)
                    speak(f"{drive} drive not found..")
            else:
                speak("app not found please say again")
                continue

        elif 'close' in command:
            appName = command.replace("close ", "")
            speak(f"closing {appName}")
            result = os.system(f"TASKKILL /F /IM {appName}.exe")
            if result == 128:
                speak(f"{appName} is not running.")

        elif 'play song' in command:
            speak("playing songs...")
            playSong()
        elif 'change track' in command or 'change song' in command:
            os.system(f"TASKKILL /F /IM vlc.exe")
            speak("changing track, i hope you like it")
            playSong()
        elif 'stop playing song' in command:
            os.system(f"TASKKILL /F /IM vlc.exe")
            speak("Stop playing songs.i hope you enjoyed it...")
        elif 'play' in command:
            song = command.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"Sir, the time is {time}")

        elif 'date' in command:
            date = datetime.date.today().strftime('%d/%B/%Y')
            date = date.replace("/", " ")
            speak(f"Sir, today's date is {date}")

        elif 'day' in command:
            day = datetime.date.today().strftime('%A')
            speak(f"Sir, today is {day}")

        elif "take screenshot" in command or "take a screenshot" in command:
            try:
                speak("sir, please tell me the name for this screenshot file")
                name = takeComand()
                speak("please sir hold the screen for few seconds, i am taking screenshot")
                img = pyautogui.screenshot()
                img.save(f"C:\\Users\\Admin\\Pictures\\Py Screenshots\\{name}.png")
                speak("i am done sir, the screenshot is saved in our Py Screenshots folder.")
            except Exception as e:
                print(e)
                speak("Sorry sir,i am not able to take a screenshot")

        elif 'cpu' in command:
            usage = str(psutil.cpu_percent())
            battery = psutil.sensors_battery()
            print(f"CPU is at usage {usage} and Battery is at {battery.percent} %.")
            speak(f"CPU is at usage {usage} and Battery is at {battery.percent} %.")

        elif 'send' in command:
            command = command.replace("send ", "")
            print(command)
            if 'email' in command:
                person = command.replace("email to ", "")
                try:
                    to = e_mail[person]
                    speak(f"what Should I send to {person}?")
                    content = takeComand()
                    print(f"Message : {content}")
                    sendEmail(to, content)
                    speak(f"Email has been sent to {person}!")
                except Exception as e:
                    print(e)
                    speak(f"Sorry sir,i am Unable to send the email to {person}.")
            elif 'whatsapp message' in command:
                person = command.replace("whatsapp message to ", "")
                try:
                    num = contact_no[person]
                    speak(f"what Should I send to {person}?")
                    msg = takeComand()
                    print(f"Message : {msg}")
                    h = datetime.datetime.now().hour
                    m = (datetime.datetime.now().minute) + 1
                    speak(f"Sir, I am sanding msg to {person}. please wait for few seconds.")
                    pywhatkit.sendwhatmsg(num, msg, h, m)
                    speak(f"message has been sent to {person}")
                except Exception as e:
                    print(e)
                    speak(f"Sorry sir,i am Unable to send the message to {person}.")
            else:
                speak("command can't recognize please say again")
                continue

        elif "where i am" in command or "where we are" in command:
            speak("wait sir, let me check")
            if data != '':
                print(f"sir i am not sure, but i think we are in {data.get('current_city')} city of {data.get('current_state')} "
                    f"state in {data.get('current_country')} country.")
                speak(f"sir i am not sure, but i think we are in {data.get('current_city')} city of {data.get('current_state')} "
                      f"state in {data.get('current_country')} country.")
            else:
                speak("sorry sir, Due to network issue i am not able to find where we are.")

        elif "weather" in command :
            speak("wait sir, let me check")
            if data != '':
                print(f"Sir, current temperature is {data.get('current_temperature')} degree celsius and "
                    f"weather is like {data.get('weather_description')} and humidity is {data.get('current_humidity')} %.")
                speak(f"Sir, current temperature is {data.get('current_temperature')} degree celsius and "
                      f"weather is like {data.get('weather_description')} and humidity is {data.get('current_humidity')} %.")
            else:
                speak("sorry sir, Due to network issue i am not able to get current weather.")

        elif "question" in command or "answer" in command:
            try:
                speak("what is your question?")
                question = takeComand()
                print(f"Question : {question}")
                speak("please wait i am finding answer")
                app_id = 'A0A0AA-A11AAAAAAA' # (Enter Your Api Key) wolframalpha api key.
                client = wolframalpha.Client(app_id)
                res = client.query(question)
                answer = next(res.results).text
                print(f"Answer : {answer}")
                speak(f"Answer is {answer}.")
            except Exception as e:
                print(e)
                speak("Sorry sir, i am not able to find answer of your question.")

        elif "hello" in command or "hey" in command:
            speak("hello sir, may i help you with something.")

        elif "how are you" in command:
            speak("i am fine sir, what about you.")

        elif "also good" in command or "fine" in command:
            speak("that's great to hear from you.")

        elif "thank you" in command or "thanks" in command:
            speak("it's my pleasure sir.")

        elif 'you can sleep' in command or 'sleep now' in command:
            speak('Okay Sir, i am going to sleep you can call me anytime.')
            break

        else:
            speak("command can not found please say again")

if __name__ == "__main__":
    while True:
        permission = takeComand()
        if 'wake up' in permission:
            taskExecution()
        elif 'goodbye' in permission:
            speak("thanks for using me sir,have a good day")
            sys.exit()