import speech_recognition as sr
import pyttsx3
import webbrowser
import os
from namesofsites import sites, songs

zira_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

def say(text, voice_id=None):
    engine = pyttsx3.init()
    
    # Optional: Set the voice (accent)
    if voice_id:
        engine.setProperty('voice', voice_id)
    
    engine.say(text)
    engine.runAndWait()

def take():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-IN")
            print(f"user said: {query}")
            return query
        except Exception as e:
            return "Some error occured! Please try again."
        
def open_web(sitename, site_url):
    say(f"Opening {sitename}", zira_id)
    webbrowser.open(site_url)  
        

def play_song(songname, song_address):
    say(f"Playing {songname}", zira_id)
    os.startfile(song_address)

if __name__ == '__main__':
    '''
    to set different voice: 
    # List available voices
    voices = pyttsx3.init().getProperty('voices')
    
    # Print available voices and their IDs
    for voice in voices:
        print(f"Voice ID: {voice.id}, Name: {voice.name}")
    
    # Change the voice using the voice ID (replace 'voice_id_here' with the desired ID)
    
    '''
    

    say("Hello, I am Violet", zira_id)

    query = take()
    say(query, zira_id)


    site_found = False  
    for site in sites:
        ini_command = "open site "
        sitename = f"{site[0]}"
        user_command = ini_command + sitename.lower()
        if user_command.lower() in query.lower():
            open_web(site[0], site[1])
            site_found = True
            


    user_command = "play songs".lower()
    if user_command in query.lower():
        filepath = "C:\\Users\\omkar\\OneDrive\\Desktop\\NCS_Songs"
        try:
            say("Opening songs folder that I found", zira_id)
            os.startfile(filepath)
        except Exception as ex:
            say(f"No folder found for playing songs!", zira_id)
        

    song_found = False     
    for song in songs:
        user_command = f"play song {song[0].lower()}"
        if user_command in query.lower():
                play_song(song[0], song[1])
                song_found = True

    if (song_found == False and site_found == False):
        say("No such thing found in saved list.", zira_id)

