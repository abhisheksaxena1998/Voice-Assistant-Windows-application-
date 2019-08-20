import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import geocoder
import reverse_geocoder as rg 
import pprint 
import random
import csv

g = geocoder.ip('me')
#print(g.latlng)
#print (g.latlng[0])



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print (voices)
#print (voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak (audio):
    engine.say(audio)
    engine.runAndWait()

def reverseGeocode(coordinates): 
    result = rg.search(coordinates)       
    # result is a list containing ordered dictionary. 
    pprint.pprint(result)  

def wishMe():
    #speak ("Hello abhishek")
    hour=int(datetime.datetime.now().hour  ) 
    if hour>=0 and hour<12:
        speak ("Good Morning!")

    elif hour>=12 and hour<18:
        speak ("Good Afternoon!")

    else:
        speak ("Good Evening!")   
    speak ("I am Ready to process your commands ")  

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Set minimum energy threshold to {} for adjusting background noise".format(r.energy_threshold))
        # obtain audio from the microphone
        print ("Listening your commands ... ")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print ("Recognizing ...")
        query=r.recognize_google(audio,language='en-in')   
        print (f"You just said : {query}\n") 
    except Exception as e:
        #print(e)
        print ("Say that again please ...")
        speak ("I am sorry about that, please say again ...  ") 
        return "None"        
    return query

if __name__ == "__main__":
    speak("Welcome abhe ")
    wishMe()
    while True: 
        query=takeCommand().lower()

        if 'wikipedia' in query:
            speak ('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results=wikipedia.summary(query,sentences=2)
                speak("According to wikipedia")
                print (results)
                speak(results)
            except:
                print (f"Page id {query}wikipedia does not match any pages.\n")    
                speak (f"Page id {query}wikepedia does not match any pages.\n")     

        if 'what is' in query:
            speak ('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results=wikipedia.summary(query,sentences=2)
                speak("According to wikipedia")
                print (results)
                speak(results)
            except:
                print (f"Page id {query}wikipedia does not match any pages.\n")    
                speak (f"Page id {query}wikepedia does not match any pages.\n")            

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
            speak("Opening Youtube")

        elif 'open facebook' in query:
            webbrowser.open("www.facebook.com")
            speak("Opening Facebook")

        elif 'open twitter' in query:
            webbrowser.open("www.twitter.com/login")
            speak("Opening Twitter")            

        elif 'open google' in query:
            webbrowser.open("www.google.com")
            speak("Opening Google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("www.stackoverflow.com")
            speak("Opening StackOverflow ...") 

        elif 'open netflix' in query:
            webbrowser.open("www.netflix.com/in/")
            speak("Opening Netflix ...")

        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com/accounts/login/?hl=en")       
            speak("Opening enstagram ...") 

        elif 'open amazon' in query:
            webbrowser.open("https://www.amazon.in/")       
            speak("Opening Amazon.in ...")     

        elif 'open cricbuzz' in query:
            webbrowser.open("https://www.cricbuzz.com/")       
            speak("Opening Crickbuzz.com for World Cup 2019, Cricket Score, Schedule, Latest News ...")      

        elif 'my location' in query:
            coordinates =(g.latlng[0], g.latlng[1])   
            speak("Loading formatted geocoded file")
            reverseGeocode(coordinates)
            speak("showing your location information inferred from Your current ip address")

        elif 'play music' in query:
            music_dir='E:\\MusiC'
            songs = os.listdir(music_dir)
            #print(songs)    
            temp=random.randint(0,66)
            os.startfile(os.path.join(music_dir,songs[temp]))
            print ("Playing music ...")
            speak ("Playing music ...")

        elif 'play video' in query:
            music_dir='E:\\MusiC'
            songs = os.listdir(music_dir)
            #print(songs)    
            #temp=random.randint(0,66)
            os.startfile(os.path.join(music_dir,songs[13]))
            print ("Playing video songs ...")
            speak ("Playing video songs ...")

        elif "the time" in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            #print(f"The Time is {strTime} ")
            #speak(f"The Time is {strTime} ")   
            x = datetime.datetime.now()
            print(x.strftime("%c"))
            speak(x.strftime("%c"))


        elif 'open calendar' in query:
            mycmd="start outlookcal:"
            print ("Opening calendar app ...")
            speak ("Opening calendar app ...")    
            os.system(mycmd)

        elif 'open windows store' in query:
            mycmd="start ms-windows-store:"
            print ("Opening Windows store ...")
            speak ("Opening Windows store ...")    
            os.system(mycmd)    

        elif 'update apps from windows store' in query:
            mycmd="start ms-windows-store:updates"
            print ("Opening Windows store's update menu ...")
            speak ("Opening Windows store's update menu ...")    
            os.system(mycmd)    

        elif 'open maps' in query:
            mycmd="start bingmaps:"
            print ("Opening Maps app ...")
            speak ("Opening Maps app ...")    
            os.system(mycmd)        

        elif 'open news' in query:
            mycmd="start bingnews:"
            print ("Opening News app ...")
            speak ("Opening News app ...")    
            os.system(mycmd)   

        elif 'security status' in query:
            mycmd="start windowsdefender:"
            print ("Showing Security status ...")
            speak ("Showing Security status ...")    
            os.system(mycmd)        

        elif 'open control panel' in query:
            mycmd="control panel"
            print ("Opening control panel ...")
            speak ("Opening control panel ...")    
            os.system(mycmd)        

        elif 'open task manager' in query:
            mycmd="taskmgr"
            print ("Opening Task manager ...")
            speak ("Opening Task manager ...")    
            os.system(mycmd)       

        elif 'show weather' in query:
            mycmd="start bingweather:"
            print ("Opening Weather app ...")
            speak ("Opening Weather app ...")    
            os.system(mycmd)       

        elif 'open calculator' in query:
            mycmd="start calculator:"
            print ("Opening Calculator ...")
            speak ("Opening Calculator ...")    
            os.system(mycmd)            

        elif 'open camera' in query:
            mycmd="start microsoft.windows.camera:"
            os.system(mycmd)
            print ("Opening camera app ...")
            speak ("Opening camera app...")

        elif 'windows update' in query:
            mycmd="start ms-settings:windowsupdate-action"
            os.system(mycmd)
            print ("Opening Windows Update in settings ...")
            speak ("Opening Windows Update in settings...")    

        elif 'open settings' in query:
            mycmd="start ms-settings:"
            os.system(mycmd)
            print ("Opening Settings app ...")
            speak ("Opening Settings app...")    
        
        elif 'shutdown windows' in query:
            mycmd="shutdown /s"
            os.system(mycmd)
            print ("Shutting Down Windows ...")
            speak ("Shutting Down Windows...")

        elif 'open code' in query:
            cpath="E:\\##installed\\Microsoft VS Code\\Code.exe"
            os.startfile(cpath)
            print ("Opening Visual Studio Code ...")
            speak ("Opening Visual Studio Code ...")

        elif 'open chrome' in query:
            copath="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            os.startfile(copath)
            print ("Opening Google Chrome ...")
            speak ("Opening Google Chrome ...")        

        elif 'search youtube' in query:
            print ("What you want to search in Youtube (Say) ...")
            nquery=takeCommand().lower()
            webbrowser.open(f"www.youtube.com/results?search_query={nquery}")
            speak (f"Searching Youtube for{nquery}")

        elif 'search google' in query:
            print ("What you want to search in Google (Say) ...")
            gquery=takeCommand().lower()
            webbrowser.open(f"www.google.com/search?q={gquery}")   

        elif 'set to do' in query:
            print ("Enter to-do task ...")
            task= takeCommand().lower()
            with open("testt.txt",'a') as f:                
                f.write(task + "\n")
                speak (f"To-do taken as{task}")

        elif 'start need for speed' in query:
            cpath="E:\\NFS MOST WANTED\\speed.exe"
            os.startfile(cpath)
            print ("Starting Need For speed most wanted ...")
            speak ("Starting need for speed most wanted ...")        

        elif 'view to do' in query:
            print ("Find your to-do's below ...")
            with open("testt.txt",'r') as f:
                content=f.read()
                print (f"I will be reading the list of your set to-do's: {content}") 
                speak (f"I will be reading the list of your set to-do's: {content}")         

        elif 'shutdown engine' in query:
            speak ("Shut down protocol initiated ... powering myself down")       
            print ("Shutting down engine ...")   
            exit()

        elif 'change your voice' in query:
            speak("Switching my default voice")
            engine.setProperty('voice',voices[0].id)
            speak("Changed my default voice")

        elif 'search text file on computer' in query:
            mi_cmd="cd Desktop" 
            os.system(mi_cmd) 
            #os.system(mi_cmd) 
            #os.system(mi_cmd) 
            print ("What is the file name (Say) ...")
            squery=takeCommand().lower()
            print (f"You want to search for {squery}")
            my_cmd="dir" + " " + squery+ ".txt" + " " + "/s /p"
            print (f"Searching {squery}.txt Status will be shown below...")
            speak (f"Searching {squery}.txt Status will be shown below...")
            os.system(my_cmd)
        
        elif 'search doc file on computer' in query:
            mi_cmd="cd .." 
            #os.system(mi_cmd) 
            #os.system(mi_cmd) 
            #os.system(mi_cmd) 
            print ("What is the file name (Say) ...")
            squery=takeCommand().lower()
            print (f"You want to search for {squery}")
            my_cmd="dir" + " " + squery+ ".docx" + " " + "/s /p"
            print (f"Searching {squery}.docx Status will be shown below...")
            speak (f"Searching {squery}.docx Status will be shown below...")
            os.system(my_cmd)

        elif 'search python file on computer' in query:
            mi_cmd="cd .." 
            #os.system(mi_cmd) 
            #os.system(mi_cmd) 
            #os.system(mi_cmd) 
            print ("What is the file name (Say) ...")
            squery=takeCommand().lower()
            print (f"You want to search for {squery}")
            my_cmd="dir" + " " + squery+ ".py" + " " + "/s /p"
            print (f"Searching {squery}.py Status will be shown below...")
            speak (f"Searching {squery}.py Status will be shown below...")
            os.system(my_cmd)    

        elif 'disk cleanup' in query: 
            cmd="cleanmgr"
            print (f"Opening disk cleanup utility ...")
            speak (f"Opening disk cleanup utility ...")
            os.system(cmd)   

        elif 'file explorer' in query: 
            cmd="explorer.exe"
            print (f"Opening File Explorer ...")
            speak (f"Opening File Explorer ...")
            os.system(cmd)   

        elif 'defragment' in query: 
            cmd="dfrgui.exe"
            print (f"Opening Disk Defragment tool ...")
            speak (f"Opening Disk Defragment tool ...")
            os.system(cmd)         
        
             






