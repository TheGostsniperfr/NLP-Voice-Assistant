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


conversation = [["Hello", "Hi"],["How are you?", "私はいいっです"], ["What is your name?", "My name is HAL"]]
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
#print(X_vect)
#print(vectorizer.get_feature_names())
#cosine similarity
def cos_sim(v1, v2):
    costheta = np.dot(v1,v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))
    return(costheta)

def dontUnderstand():
    speak("I don't understand your question.")    

#REPL
while True:
    query = takeCommand()
    query = query.lower()
    if "None" in query:
        dontUnderstand()
        continue

    if "quit" in query:
        break
    
    if "whatsapp" in query:
        speak("Openning whatsapp")
        open("whatsapp")
        break
    
    
    if "teams" in query:
        speak("Openning teams")
        open("teams")
        break
    
    q_vect = np.array(vectorizer.transform([query]).todense().copy())[0,:]
    #print(q_vect)
    match = [cos_sim(q_vect, v) for v in X_vect]
    
    maxMatch = max(match)
    if(str(maxMatch) == "nan" or max(match) < 0.5 ):
        dontUnderstand()
        continue
    
    print(match)
    #find max index
    indexMax = max([(v,i) for i,v in enumerate(match)])
    #print(indexMax)
    speak(conversation[indexMax[1]][1])



# while True:
#     command = takeCommand()
#     #Conversational
#     if 'how are you' in command:
#         speak("I'm doing well")
#     if 'thank you' in command:
#         speak("Anytime")

#     #Tasks
#     if 'time' in command:
#         now = datetime.now()
#         current_time = now.strftime("%H:%M:%S")
#         speak("The Current Time is " + current_time)  
#     if 'random number' in command:
#         randInt = random.randint(0, 10) 
#         speak("A random number between 0 and 10 is " + str(randInt))
