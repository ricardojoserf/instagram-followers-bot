import os, sys, time
from random import randint


while(1):
	try:
		secs = randint(int(sys.argv[1]), int(sys.argv[2]))
		time.sleep(secs)
		os.system("python main.py -u "+sys.argv[3]+" -p "+sys.argv[4]+" -o "+sys.argv[5]+" -t "+sys.argv[6])
	except:
		pass

