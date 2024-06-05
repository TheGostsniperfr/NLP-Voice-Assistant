import speech_recognition as sr
import pyttsx3
import random
from datetime import datetime
import os
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
import numpy as np
from AppOpener import open


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)

for voice in engine.getProperty('voices'):
    print(voice)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Now listening")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        print("Deciphering")   
        query = r.recognize_google(audio, language ='en-in')
        print("You Said: " + query)
  
    except Exception as e:
        print(e)
        print("Did not hear anything") 
        return "None"
     
    return query

conversation = [
    ["Hello", "Hi"],
    ["How are you?", "I'm good, thank you."],
    ["What's your name?", "My name is HAL."]]


#make corpus
corpus = []
for [q,_] in conversation:
    corpus.append(q)
print(corpus)   
#make TFIDF
corpus = [x.lower() for x in corpus]
nltk.download('stopwords', quiet=True)
stopwords = nltk.corpus.stopwords.words('english')
#vectorizer = TfidfVectorizer(stop_words = stopwords )
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
X_vect = np.array(X.todense().copy())
def cos_sim(v1, v2):
    costheta = np.dot(v1,v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))
    return(costheta)

def dontUnderstand():
    msg = "I don't understand your question."
    speak(msg)
    return msg

def openWhatsapp():
    msg = "Openning whatsapp"
    speak(msg)
    open("whatsapp")
    return msg    

def openTeams():
    msg = "Openning teams"
    open("teams")
    speak(msg)
    return msg

#REPL
def process(query: str) -> str:
    query = takeCommand()
    query = query.lower()
    if "None" in query:
        return dontUnderstand()

    if "quit" in query:
        return "Bye"
    
    if "whatsapp" in query:
        return openWhatsapp()

    if "teams" in query:
        return openTeams()
    
    q_vect = np.array(vectorizer.transform([query]).todense().copy())[0,:]
    match = [cos_sim(q_vect, v) for v in X_vect]
    
    maxMatch = max(match)
    if(str(maxMatch) == "nan" or max(match) < 0.5 ):
        return dontUnderstand()
    
    # print(match)
    #find max index
    indexMax = max([(v,i) for i,v in enumerate(match)])
    #print(indexMax)
    
    msg =  conversation[indexMax[1]][0]
    speak(msg)
    return msg

