import facebook
import requests
import re
import time
import pymongo
from pymongo import MongoClient
# Use your own Facebook access token here
ACCESS_TOKEN =
'EAACEdEose0cBAMWlfbjK8ZA7IOGk3kI8NYAc40bdZC
XPHo8J1mBFE6a6lpkQJYfohZACbZB21Ab2upZAytCHSRS
NbpPrcn6W910db3HpaBKZCwdiaimrXUQTEXOkcZCKFLi
9TbVuZAzZBsIfEVe7BHIc54niO1olktqMS9uYfLFFvk9tiQd
vHUcxThKXZCDDAgyssrd6VYPz7aZBgZDZD'
# Create a connection to the Graph API with your access token
g = facebook.GraphAPI(ACCESS_TOKEN, version='2.7')
# IDs of top 50 Facebook pages based on betweenness
centrality of Depth-3 graph
# SKIPPED 187358377963857, feed =
g.get_connections(post_id, 'comments')
# SKIPPED {u'name': u'Tom Colicchio', u'id':
u'134049266672525'} feed = g.get_connections(post_id,
'comments') facebook.GraphAPIError: Unsupported get
request. Object with ID
'134049266672525:158551934222258:10104708160425561_
10105912586570920' does not exist, cannot be loaded due to
missing permissions, or does not support this operation.
# 15704546335,
#153080620724,
#36019593759,
#80256732576,
#69813760388,
'''95475020353,
29616434571,
467133963318685,
123999957647509,
6470828395,
695526053890545,
21375324480,
303994289775267,
237881946323178,
141513472571212,
129255907131113,
189531267729007,
92925746942,
124016042296,
39432041915,
182556315119442,
105838869677,
208457102639014,
301650956713,
149475666523,
140942967206,
26144134130,
134325379926458,
228347177179434,
218505224686,
241711025855990,
161355253917286,
128447305670,
36400348187,
19182454196,
220435664663136,
1133625796661853,
128238827227272,
315496455229328,
280621698709756,
111491070950,
14863629315,'''
top50 = [
125200204167114,
731890386871274,
296231886728,
312520783138,
401933139867923,
120745732681,
]
print ("Checking top %d FB Pages"%len(top50))
# Swearing words 1
swearing1 = [
'2g1c',
'2 girls 1 cup',
'acrotomophilia',
'anal',
'anilingus',
'anus',
'arsehole',
'ass',
'asshole',
'assmunch',
'auto erotic',
'autoerotic',
'babeland',
'baby batter',
'ball gag',
'ball gravy',
'ball kicking',
'ball sack',
'ball sucking',
'bangbros',
'bareback',
'barely legal',
'barenaked',
'bastardo',
'bastinado',
'bbw',
'bdsm',
'beaver cleaver',
'beaver lips',
'bestiality',
'bi curious',
'big black',
'big breasts',
'big knockers',
'big tits',
'bimbos',
'birdlock',
'bitch',
'black cock',
'blonde action',
'blonde on blonde action',
'blow j',
'blow your l',
'blue waffle',
'blumpkin',
'bollocks',
'bondage',
'boner',
'boob',
'boobs',
'booty call',
'brown showers',
'brunette action',
'bukkake',
'bulldyke',
'bullet vibe',
'bung hole',
'bunghole',
'busty',
'butt',
'buttcheeks',
'butthole',
'camel toe',
'camgirl',
'camslut',
'camwhore',
'carpet muncher',
'carpetmuncher',
'chocolate rosebuds',
'circlejerk',
'cleveland steamer',
'clit',
'clitoris',
'clover clamps',
'clusterfuck',
'cock',
'cocks',
'coprolagnia',
'coprophilia',
'cornhole',
'cum',
'cumming',
'cunnilingus',
'cunt',
'darkie',
'date rape',
'daterape',
'deep throat',
'deepthroat',
'dick',
'dildo',
'dirty pillows',
'dirty sanchez',
'dog style',
'doggie style',
'doggiestyle',
'doggy style',
'doggystyle',
'dolcett',
'domination',
'dominatrix',
'dommes',
'donkey punch',
'double dong',
'double penetration',
'dp action',
'eat my ass',
'ecchi',
'ejaculation',
'erotic',
'erotism',
'escort',
'ethical slut',
'eunuch',
'faggot',
'fecal',
'felch',
'fellatio',
'feltch',
'female squirting',
'femdom',
'figging',
'fingering',
'fisting',
'foot fetish',
'footjob',
'frotting',
'fuck',
'fucking',
'fuck buttons',
'fudge packer',
'fudgepacker',
'futanari',
'g-spot',
'gang bang',
'gay sex',
'genitals',
'giant cock',
'girl on',
'girl on top',
'girls gone wild',
'goatcx',
'goatse',
'gokkun',
'golden shower',
'goo girl',
'goodpoop',
'goregasm',
'grope',
'group sex',
'guro',
'hand job',
'handjob',
'hard core',
'hardcore',
'hentai',
'homoerotic',
'honkey',
'hooker',
'hot chick',
'how to kill',
'how to murder',
'huge fat',
'humping',
'incest',
'intercourse',
'jack off',
'jail bait',
'jailbait',
'jerk off',
'jigaboo',
'jiggaboo',
'jiggerboo',
'jizz',
'juggs',
'kike',
'kinbaku',
'kinkster',
'kinky',
'knobbing',
'leather restraint',
'leather straight jacket',
'lemon party',
'lolita',
'lovemaking',
'make me come',
'male squirting',
'masturbate',
'menage a trois',
'milf',
'missionary position',
'motherfucker',
'mound of venus',
'mr hands',
'muff diver',
'muffdiving',
'nambla',
'nawashi',
'negro',
'neonazi',
'nig nog',
'nigga',
'nigger',
'nimphomania',
'nipple',
'nipples',
'nsfw images',
'nude',
'nudity',
'nympho',
'nymphomania',
'octopussy',
'omorashi',
'one cup two girls',
'one guy one jar',
'orgasm',
'orgy',
'paedophile',
'panties',
'panty',
'pedobear',
'pedophile',
'pegging',
'penis',
'phone sex',
'piece of shit',
'piss pig',
'pissing',
'pisspig',
'playboy',
'pleasure chest',
'pole smoker',
'ponyplay',
'poof',
'poop chute',
'poopchute',
'porn',
'porno',
'pornography',
'prince albert piercing',
'pthc',
'pubes',
'pussy',
'queaf',
'raghead',
'raging boner',
'rape',
'raping',
'rapist',
'rectum',
'reverse cowgirl',
'rimjob',
'rimming',
'rosy palm',
'rosy palm and her 5 sisters',
'rusty trombone',
's&m',
'sadism',
'scat',
'schlong',
'scissoring',
'semen',
'sex',
'sexo',
'sexy',
'shaved beaver',
'shaved pussy',
'shemale',
'shibari',
'shit',
'shota',
'shrimping',
'slanteye',
'slut',
'smut',
'snatch',
'snowballing',
'sodomize',
'sodomy',
'spic',
'spooge',
'spread legs',
'strap on',
'strapon',
'strappado',
'strip club',
'style doggy',
'suck',
'sucks',
'suicide girls',
'sultry women',
'swastika',
'swinger',
'tainted love',
'taste my',
'tea bagging',
'threesome',
'throating',
'tied up',
'tight white',
'tit',
'tits',
'titties',
'titty',
'tongue in a',
'topless',
'tosser',
'towelhead',
'tranny',
'tribadism',
'tub girl',
'tubgirl',
'tushy',
'twat',
'twink',
'twinkie',
'two girls one cup',
'undressing',
'upskirt',
'urethra play',
'urophilia',
'vagina',
'venus mound',
'vibrator',
'violet blue',
'violet wand',
'vorarephilia',
'voyeur',
'vulva',
'wank',
'wet dream',
'wetback',
'white power',
'women rapping',
'wrapping men',
'wrinkled starfish',
'xx',
'xxx',
'yaoi',
'yellow showers',
'yiffy',
'zoophilia']
# Swearing + Sensitive words dictionary
swearing = {}
# Add swearing list 1 to dictionary
for word in swearing1:
word = word.strip()
if len(word) > 0:
swearing[word] = word
# Load file with swearing words and add to dictionary
f = open("swearing.txt")
for word in f:
word = word.strip()
if len(word) > 0:
swearing[word] = word
f.close()
# Load second file with swearing words and add to dictionary
f = open("swearing2.txt")
for word in f:
word = word.strip()
if len(word) > 0:
swearing[word] = word
f.close()
# Load file with sensitive words and add to dictionary
f = open("sensitive.txt")
for word in f:
word = word.strip()
if len(word) > 0:
swearing[word] = word
f.close()
print ("Loaded %d swearing words"%len(swearing))
# Make a regular expression out of the dictionary
words = swearing.keys()
#print words
#re_str = r'(' + '|'.join(words) + ')'
re_str = r"("
for i,word in enumerate(words):
if i == 0:
re_str += "\\b"+word+"\\b"
else:
re_str += "|"+"\\b"+word+"\\b"
re_str += ")"
#print re_str
pattern = re.compile(re_str, re.IGNORECASE)
# Helper functions to retrieve feeds and related data
# Declare a helper function for retrieving the official feed
from a given page.
def retrieve_page_feed(page_id, n_posts):
"""Retrieve the first n_posts from a page's feed in reverse
chronological order."""
feed = g.get_connections(page_id, 'posts')
posts = []
posts.extend(feed['data'])
while len(posts) < n_posts:
try:
feed = requests.get(feed['paging']['next']).json()
posts.extend(feed['data'])
except KeyError:
# When there are no more posts in the feed, break
#print('Reached end of feed.')
break
except ValueError:
continue
except facebook.GraphAPIError:
continue
if len(posts) > n_posts:
posts = posts[:n_posts]
#print('{} items retrieved from feed'.format(len(posts)))
return posts
# Declare a helper function for returning the message content
of a post or comment
def get_post_message(post):
try:
message = post['story']
except KeyError:
# Post may have 'message' instead of 'story'
pass
try:
message = post['message']
except KeyError:
# Post has neither
message = ''
return post['id'],post['created_time'], message.replace('\n', ' ')
# Declare a helper function for retrieving the comments from a
post.
def retrieve_post_comments(post_id, n_comments):
"""Retrieve the first n_comments from a post's comments in
reverse
chronological order."""
feed = g.get_connections(post_id, 'comments')
posts = []
posts.extend(feed['data'])
while len(posts) < n_comments:
try:
feed = requests.get(feed['paging']['next']).json()
posts.extend(feed['data'])
except KeyError:
# When there are no more posts in the feed, break
#print('Reached end of feed.')
break
except ValueError:
continue
except facebook.GraphAPIError:
continue
if len(posts) > n_comments:
posts = posts[:n_comments]
#print('{} items retrieved from feed'.format(len(posts)))
return posts
# Initialize MongoDB
client = MongoClient('localhost', 27017)
db = client.facebook_database
page_data = db.page_data_collection
post_data = db.post_data_collection
comment_data = db.comment_data_collection
response_data = db.response_data_collection
# Collect and store page, post, comment, and response data
for rank,topi in enumerate(top50):
print ()
print ("Checking Rank %d ----------------"%(rank + 1))
# Get the page info
page = g.get_object(str(topi))
print (page)
page_obj_id = page_data.insert_one(page).inserted_id
print ("Page's MongoDB Id: "+str(page_obj_id))
# Get lastest posts
feed = retrieve_page_feed(topi, 1000)
for i, post in enumerate(feed):
pid, created_time, message = get_post_message(post)
matches = pattern.findall(message)
# If post contains swear or sensitive words
if len(matches) > 0:
post["bad_words"] = matches
post_obj_id = post_data.insert_one(post).inserted_id
#print "Post --------------%s"%matches
#print pid,message
# get latest comments
comments = retrieve_post_comments(pid, 100)
#print "Comments --------------"
for comment in comments:
comment_obj_id =
comment_data.insert_one(comment).inserted_id
cid, created_time, comment =
get_post_message(comment)
#print cid,comment
#print
# Get response of comments
comments_of_comments =
retrieve_post_comments(cid, 100)
for c_o_comment in comments_of_comments:
response_obj_id =
response_data.insert_one(c_o_comment).inserted_id
coc_id, created_time, c_o_comment =
get_post_message(c_o_comment)
#print "\t"+c_o_comment
# Wait so we won't be banned
print ("Waiting for 3 minutes")
time.sleep(180)
print ("Done collecting data")

