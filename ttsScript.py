# TEXT FILE reading
import time 
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 180) 

"""VOICE"""
#getting details of current voice
voices = engine.getProperty('voices')     
#changing index, changes voices. 1 for female 
engine.setProperty('voice', voices[1].id)   


# READ FILE
with open('text.txt', 'r') as f:
    # for first_character in f:
    #     first_character = f.readline(5)
    #     print(first_character)

    # READ AND SAY EACH LINE
    for line in f:
        print(line, end='')
        engine.say(line)
        engine.runAndWait()
        engine.stop()



