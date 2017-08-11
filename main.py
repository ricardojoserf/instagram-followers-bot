import aux_funcs, sys, json, time, random
from LevPasha.InstagramAPI import InstagramAPI

followers = []
followings = []
args = aux_funcs.get_args()
api  = InstagramAPI(args.user, args.password)

def info():
	print("\nI follow them but they dont follow me:\n")
	tot = 0
	for i in followings:
		if i not in followers:
			tot=tot+1
			print(str(tot)+" "+i)		
	print("\nTotal: "+str(tot))

	print("\n\nThey follow me but i dont follow them:\n")
	tot = 0
	for i in followers:
		if i not in followings:
			tot=tot+1
			print(str(tot)+" "+i)	
	print("\nTotal: "+str(tot))

def superUnfollow():
	for i in followings:
			if i not in followers:
				user_id = aux_funcs.get_id(i)
				print("Unfollowing "+i+"(with id "+user_id+")")
				api.unfollow(user_id)

def superFollow(tag):
	api.tagFeed(tag)
	media_id = api.LastJson 
	MAXIMO = 30
	tot = 0
	print("\nTAG: "+str(tag)+"\n")
	for i in media_id["items"]:
		time.sleep( float( random.randint(10,60) / 10 ) )
		username = i.get("user")["username"]
		user_id = i.get("user")["pk"]
		api.follow(user_id)
		tot += 1
		print("Following "+str(username)+" (with id "+str(user_id)+")")	
		if(tot>=MAXIMO):
			break
	print("Total: "+str(tot)+" for tag "+tag+" (Max val: "+str(MAXIMO)+")\n")

def unfollowOneFollower(username):
	user_id = aux_funcs.get_id(username)
	api.unfollow(user_id)
	print("Unfollowing "+username+" (with id "+user_id+")")

def followOneFollower(username):
	user_id = aux_funcs.get_id(username)
	api.follow(user_id)
	print("Following "+username+" (with id "+user_id+")")	

def printUsage():
	print("Usage: \n+ python main.py -u USERNAME -p PASSWORD -o info: Show report ")
	print("+ python main.py -u USERNAME -p PASSWORD -o superFollow -t TAG: Follow users using the tags you introduce \n+ python main.py -u USERNAME -p PASSWORD -o superUnfollow: Unfollow all the users who dont follow you back")
	print("+ python main.py -u USERNAME -p PASSWORD -o unfollow - t USERNAME_TO_UNFOLLOW: Unfollow a user \n+ python main.py -u USERNAME -p PASSWORD -o follow -t USERNAME_TO_FOLLOW: Follow a user")
	return
	
def main():

	option = args.option

	api.login()

	for i in api.getTotalSelfFollowers():
		followers.append(i.get("username") )

	for i in api.getTotalSelfFollowings():
		followings.append(i.get("username") )

	if(option == "info"):
		info()

	elif(option == "superUnfollow"):
		superUnfollow()

	elif(option == "superFollow"):
		#for tag in sys.argv[2:]:
		target = args.target
		if target is not None:
			superFollow(target)
		else:
			printUsage()

	elif(option == "unfollow"):
		target = args.target
		if target is not None:
			unfollowOneFollower(target)
		else:
			printUsage()

	elif(option == "follow"):
		target = args.target
		if target is not None:
			followOneFollower(target)
		else:
			printUsage()

	else:
		printUsage()

if __name__ == "__main__":
    main()
