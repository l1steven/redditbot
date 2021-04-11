#!/usr/bin/python
import praw
import sched
import time
from praw.models import Message
#Enter your correct Reddit information into the variable below
from PyDictionary import PyDictionary
from vocabulary.vocabulary import Vocabulary as vb

dictionary=PyDictionary()

def synonymSentence(str):
    words = str.split()
    mod_sentence = ""

    for i in words:
        print(words)
        speech = vb.part_of_speech(i)
        partOfSpeech = speech[speech.find("text")+8: speech.find('"',speech.find("text")+8)]
        if partOfSpeech == "noun" or partOfSpeech == "adjective":
            mod_sentence += dictionary.synonym(i)[0] + " "
        else:
            mod_sentence += i + " "
    return mod_sentence

userAgent = 'ReplyBot'

cID = 'HFud_kbNJBskAQ'

cSC= 'epD9ZnGonUhI1iaSDqFk-4cKR7Me5g'


userN = 'surajburnerbot'

userP ='suraj123'

numFound = 0

reddit = praw.Reddit(user_agent=userAgent, client_id=cID, client_secret=cSC, username=userN, password=userP)

subreddit = reddit.subreddit('Suraj123TestingBot') #any subreddit you want to monitor

bot_phrase = 'Aw shucks, looks like I am staying in >:(' #phrase that the bot replies with

unread=[]
#print(synonymSentence("the dog just ate a bunch of pizza and snacks"))
event_schedule=sched.scheduler(time.time,time.sleep)
def do_something():
   print("hi")
   for item in reddit.inbox.unread(limit=None):
      print(item.body)
      message = item.body
      if message.find('u/')!=-1:
         message = message[:message.find('u/')] + message[message.find('u/')+len(userN)+2:]
      print("heloooooooooooooooooooooooooooooooooooooooo")
      print(message)
      item.reply(synonymSentence(message))
      #if isinstance(item,Message):
      item.mark_read()
   event_schedule.enter(10,1,do_something)
event_schedule.enter(10,1,do_something)
event_schedule.run()

if numFound == 0:

   print()

   print("Sorry, didn't find any posts with those keywords, try again!")