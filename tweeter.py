
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

ckey ='93l97g6ggvi0DPZxLhzODAbwV'
csecret ='6AVDl51sgA1UI6UyUM0GPpYHCeMmNvd1nbbCgNlk2B5NtL4Tfh'
atoken ='102916423-iN3du6DHWWKvfDHCnwGKPjUUDHgc5pTxnj7vzMpS'
asecret ='Gat18F3CTOWOe1urvGCpHresn0YBcbnjBkGHZZoVpk1ZG'


class listener(StreamListener):
	def on_data(self,data):
		try:
			#print data
			tweet = data.split(',"text":"')[1].split('","source')[0]
			print tweet
			#count = count - 1	
			saveThis = str(time.time())+'::'+tweet
			savefile = open('twit2.csv','a')
			savefile.write(saveThis)
			savefile.write('\n')
			savefile.close()
			return True
			
		except BaseException, e:
			print 'failed on data,',str(e)
			time.sleep(5)
		except:
			print "End of the stream"
			exit()
	
	def on_error(self,status):
		print status
		
auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
twitterStream = Stream(auth,listener())
twitterStream.filter(track=["soccer"])



