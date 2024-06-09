import speech_recognition as sr
import pyttsx3
import random
from datetime import datetime
import os
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
import numpy as np
from AppOpener import open
import os
from utils import startSpeaking, stopSpeaking



conversation = [
    ["Hello", "Hi"],
    ["How are you?", "I'm good, thank you."],
    ["What's your name?", "My name is HAL."]]




class ChatBotLogic:
    def __init__(self, conversation):
        self.conversation = conversation
        
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)
        
        #make corpus
        self.corpus = []
        for [q,_] in conversation:
             self.corpus.append(q)
        # print(corpus)   
        #make TFIDF
        self.corpus = [x.lower() for x in  self.corpus]
        nltk.download('stopwords', quiet=True)
        self.stopwords = nltk.corpus.stopwords.words('english')
        #vectorizer = TfidfVectorizer(stop_words = stopwords )
        self.vectorizer = TfidfVectorizer()
        self.X = self.vectorizer.fit_transform(self.corpus)
        self.X_vect = np.array(self.X.todense().copy())
    
    def cos_sim(self, v1, v2):
            costheta = np.dot(v1,v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))
            return(costheta)
        
    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()
        
    def takeCommand(self, verbose = False, page = None):
        r = sr.Recognizer()
        
        if page != None : startSpeaking(page)

        with sr.Microphone() as source:
            
            if verbose : print("Now listening")
            r.pause_threshold = 1
            audio = r.listen(source)
    
        try:
            if verbose : print("Deciphering")   
            query = r.recognize_google(audio, language ='en-in')
            if page != None : stopSpeaking(page)
            if verbose : print("You Said: " + query)
    
        except Exception as e:
            if verbose : print(e)
            if verbose : print("Did not hear anything") 
            return "None"
        
        return query
    
    def dontUnderstand(self):
        msg = "I don't understand your question."
        self.speak(msg)
        return msg

    def openWhatsapp(self):
        msg = "Openning whatsapp"
        self.speak(msg)
        open("whatsapp")
        return msg

    def openSpotify(self):
        msg = "Openning Spotify"
        open("spotify")
        self.speak(msg)
        return msg

    def process(self, verbose = False, query = "") -> str:
        #query = self.takeCommand(verbose)
        query = query.lower()
        if "None" in query:
            return self.dontUnderstand()

        if "quit" in query:
            return "Bye"
        
        if "whatsapp" in query:
            return self.openWhatsapp()

        if "spotify" in query:
            return self.openSpotify()
        
        q_vect = np.array(self.vectorizer.transform([query]).todense().copy())[0,:]
        match = [self.cos_sim(q_vect, v) for v in self.X_vect]
        
        maxMatch = max(match)
        if(str(maxMatch) == "nan" or max(match) < 0.5 ):
            return self.dontUnderstand()
        
        if verbose : print(match)
        
        #find max index
        indexMax = max([(v,i) for i,v in enumerate(match)])
        if verbose : print(indexMax)
        
        msg =  conversation[indexMax[1]][1]
        self.speak(msg)
        return msg



# e = ChatBotLogic(conversation)

# while(True):
#    print(e.process())
