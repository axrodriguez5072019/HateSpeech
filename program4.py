#(Sentiment and Emotion Analys)
# -*- coding: utf-8 -*-
import pymongo
from pymongo import MongoClient
import nltk
from vaderSentiment.vaderSentiment
import SentimentIntensityAnalyzer
import requests
import json
import time
import multiprocessing
from random import shuffle
from itertools import islice
# Connect to MongoDB and get collections
client = MongoClient('localhost', 27017)
db = client.facebook_database
page_data = db.page_data_collection
post_data = db.post_data_collection
comment_data = db.comment_data_collection
response_data = db.response_data_collection
# Helper functions
def count_unique(collection):
unique = {}
count = 0
for post in collection.find({ }):
if post["id"] not in unique:
unique[post["id"]] = post
else:
#print "Repeated "+post["id"]
count = count + 1
print (collection.count(), len(unique))
print ("Repeated %d"%count)
return (unique)
def count_unique_no_sa(collection):
unique = {}
count = 0
for post in collection.find({ "sentences" : { '$exists' :
False } }):
if post["id"] not in unique:
unique[post["id"]] = post
else:
#print "Repeated "+post["id"]
count = count + 1
print (collection.count(), len(unique))
print ("Repeated %d"%count)
return unique
def chunks(data, SIZE=10000):
it = iter(data)
for i in xrange(0, len(data), SIZE):
yield {k:data[k] for k in islice(it, SIZE)}
def jammin_emotion(text):
# Pre process text
text = text.replace('"','\\"')
text = text.replace("\n"," ")
payload = '{"text":"%s","lang":"en"}'%(text)
#print payload
headers = {'content-Type': 'application/json'}
url =
'http://1.34.96.63:8080/JamminTextEmotionAPI/webresources
/jammin/emotion'
#url =
'http://127.0.0.1:8080/JamminTextEmotionAPI/webresources/
jammin/emotion'
try:
r = requests.post(url, data=payload, headers=headers)
return r.json()
except ValueError:
print ("Error: ",payload)
return -1
def contains_a_d_or_b(response):
if "yes" in response["bullying"]:
#print "Contains bullying"
return True
for group in response["groups"]:
if "anger" in group["name"]:
#print "Contains anger"
return True
if "disgust" in group["name"]:
#print "Contains disgust"
return True
return False
# Get the unique elements of each collection
print ("Pages")
unique_pages = count_unique(page_data)
print ("Posts")
unique_posts = count_unique(post_data)
print ("Comments")
unique_comments = count_unique_no_sa(comment_data)
print ("Responses")
unique_responses = count_unique(response_data)
# Init the Vader analyzer
analyzer = SentimentIntensityAnalyzer()
def analyze(pid,comments_ids, comments, collection):
client = MongoClient('localhost', 27017)
db = client.facebook_database
if "comments" in collection:
collection = db.comment_data_collection
elif "responses" in collection:
collection = db.response_data_collection
else:
print ("Error: Wrong collection")
return
jammin_error_count = 0
print ("%d) Analyzing %d
comments"%(pid,len(comments_ids)))
for ID in comments_ids:
comment = comments[ID]
# List to store the sentences and their emotions
sentences = []
# Split into sentences
text = comment["message"]
#print text
tokenized_sentences = nltk.sent_tokenize(text)
for sentence in tokenized_sentences:
#print "-@-@- ",sentence
# Get Vader sentiment
sentence = sentence.encode('utf-8')
vs = analyzer.polarity_scores(sentence)
# Get Jammin emotions
je = jammin_emotion(sentence)
if je == -1:
je = {}
jammin_error_count = jammin_error_count + 1
# Add the sentence data to the list
sent_data = {"text":sentence,"vader":vs,"jammin":je}
sentences.append(sent_data)
# Update the comment
collection.update_one(
{'_id': comment['_id']},
{
"$set": {
"sentences":sentences
}
}
)
print ("%d) Done with Jammin
errors %d"%(pid,jammin_error_count))
comments_ids = unique_comments.keys()#[:100]
comments = unique_comments
collection = comment_data
start_time = time.time()
jobs = []
print ("Total comments %d"%len(comments_ids))
chunk_size = int(len(comments_ids)/10)
prev = 0
count = 0
for to in range(0, len(comments_ids), chunk_size):
count = count + 1
to = to + chunk_size
some_ids = comments_ids[prev:to]
p = multiprocessing.Process(target = analyze, args =
(count,some_ids,comments,"comments"))
jobs.append(p)
p.start()
prev = to
for p in jobs:
p.join()
print ("Done")
elapsed_time = time.time() - start_time
print ("Done in %s"%elapsed_time)
