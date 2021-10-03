import facebook
import requests
ACCESS_TOKEN ='EAACEdEose0cBAMWlfbjK8ZA7IOGk3kI8NYAc40bdZCXPHo8J1mBFE6a6lpkQJYfohZACbZB21Ab2upZAytCHSRSNbpPrcn6W910db3HpaBKZCwdiaimrXUQTEXOkcZCKFLi9TbVuZAzZBsIfEVe7BHIc54niO1olktqMS9uYfLFFvk9tiQdvHUcxThKXZCDDAgyssrd6VYPz7aZBgZDZD'
access_tokens = [ACCESS_TOKEN, ACCESS_TOKEN ,
ACCESS_TOKEN]
#Create a connection to the Graph API with your access token
g = facebook.GraphAPI(ACCESS_TOKEN, version='2.7')
#seeds = [153080620724, 1220332944702810, 80256732576,
108331419836570, 95475020353, 1133625796661853,
303994289775267, 319222721600593, 695526053890545]
def get_famous_followed(access_tokens, uids, min_likes,
level, max_level, file_obj):
 level = level + 1
if level > max_level:
 return
 print ("Level %d"%level)
 access_token = access_tokens[level - 1]
 print ("Using access token %s"%access_token)
 g = facebook.GraphAPI(access_token, version='2.7')
 follows = []
 count_requests = 0
 for uid in uids:
 #print "Getting the pages ID %s likes"%uid
 page = 1
 #print "Page %d -----------------"%page
 likes = g.get_connections(id=uid,
connection_name='likes')
 count_requests = count_requests + 1
 for i,liker in enumerate(likes['data']):
 fan_count = g.get_object(id=liker['id'],
fields=['fan_count'])['fan_count']
 count_requests = count_requests + 1
 if count_requests > 500:
 count_requests = 0
 time.sleep(360)
 if fan_count > min_likes:
 print (liker['id']+" - "+liker['name'] + " - "
+str(g.get_object(id=liker['id'],
fields=['fan_count'])['fan_count']))
 follows.append(liker['id'])
 file_obj.write(str(uid)+"\t"+str(liker['id'])+"\n")
 while True:
 try:
 likes = requests.get(likes['paging']['next']).json()
 page = page + 1
 #print "Page %d -----------------"%page
 fan_count = g.get_object(id=liker['id'],
fields=['fan_count'])['fan_count']
 count_requests = count_requests + 1
 if count_requests > 500:
 count_requests = 0
 time.sleep(360)
 if fan_count > min_likes:
 #print liker['id']+" - "+liker['name'] + " - "
+str(g.get_object(id=liker['id'],
fields=['fan_count'])['fan_count'])
 follows.append(liker['id'])
 file_obj.write(str(uid)+"\t"+str(liker['id'])+"\n")
 except KeyError:
 # When there are no more posts in the feed, break
 #print('Reached end of feed.')
 break
time.sleep(360)
 get_famous_followed(access_tokens, follows, min_likes,
level, max_level, file_obj)
 return
f = open("edges_l3_prueba.txt","w")
get_famous_followed(access_tokens, seeds, 0, 0, 3, f)
f.close()