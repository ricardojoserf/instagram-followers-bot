import os, sys, time
from random import randint

# Input values: min_delay, max_delay, username, password
# Follow people using the hashtag followforfollow

while(1):
	try:
		os.system("python main.py -u "+sys.argv[3]+" -p "+sys.argv[4]+" -o follow-tag -t followforfollow ")
		secs = randint(int(sys.argv[1]), int(sys.argv[2]))
		time.sleep(secs)
		os.system("python main.py -u "+sys.argv[3]+" -p "+sys.argv[4]+" -o super-unfollow")
		secs = randint(int(sys.argv[1]), int(sys.argv[2]))
		time.sleep(secs)
	except:
		pass

