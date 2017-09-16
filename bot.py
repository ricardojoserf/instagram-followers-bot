import os, sys, time
from random import randint


while(1):
	try:
		secs = randint(int(sys.argv[1]), int(sys.argv[2]))
		time.sleep(secs)
		os.system("python main.py -u "+sys.argv[3]+" -p "+sys.argv[4]+" -o follow-location -t 127963847 ")
		os.system("python main.py -u "+sys.argv[3]+" -p "+sys.argv[4]+" -o super-followback")
	except:
		pass

