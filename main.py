import aux_funcs, sys, json, time, random
from LevPasha.InstagramAPI import InstagramAPI

followers = []
followings = []
args = aux_funcs.get_args()
api  = InstagramAPI(args.user, args.password)


def info():
	print("I follow them but they dont follow me:\n")
	tot = 0
	for i in followings:
		if i not in followers:
			tot=tot+1
			print(str(tot)+" "+i)		
	print("\nTotal: "+str(tot))

	print("\nThey follow me but i dont follow them:\n")
	tot = 0
	for i in followers:
		if i not in followings:
			tot=tot+1
			print(str(tot)+" "+i)	
	print("\nTotal: "+str(tot))


def super_unfollow():
	whitelist = open("whitelist.txt").read().splitlines()
	count = 0
	for i in followings:
		if (i not in followers) and (i not in whitelist):
			count+=1
			time.sleep(1)
			user_id = aux_funcs.get_id(i)
			print(str(count)+") Unfollowing "+i)
			api.unfollow(user_id)


def super_followback():
	count = 0
	for i in followers:
		if i not in followings:
			count+=1
			time.sleep(1)
			user_id = aux_funcs.get_id(i)
			print(str(count)+") Following back "+i)
			api.follow(user_id)


def follow_tag(tag):
	api.tagFeed(tag)
	media_id = api.LastJson 
	MAXIMO = 100
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


def printUsage():
	print("Usage: \n+ python main.py -u USERNAME -p PASSWORD -o info: Show report")
	print("+ python main.py -u USERNAME -p PASSWORD -o super-followback: Follow back all the users who you dont follow back")
	print("+ python main.py -u USERNAME -p PASSWORD -o super-unfollow: Unfollow all the users who dont follow you back")
	print("+ python main.py -u USERNAME -p PASSWORD -o follow-tag -t TAG: Follow users using the tags you introduce")
	print("+ python main.py -u USERNAME -p PASSWORD -o follow-location -t LOCATION_ID: Follow users from a location")


def follow_location(target):
	users_madrid = []
	api.getLocationFeed(target)
	media_id = api.LastJson 
	for i in media_id.get("items"):
		username = i.get("user").get("username")
		user_id = aux_funcs.get_id(username)
		print ("Following " + username)
		api.follow(user_id)



def main():
	option = args.option
	api.login()

	for i in api.getTotalSelfFollowers():
		followers.append(i.get("username") )

	for i in api.getTotalSelfFollowings():
		followings.append(i.get("username") )

	if(option == "info"):
		info()

	elif(option == "super-followback"):
		super_followback()

	elif(option == "super-unfollow"):
		super_unfollow()

	elif(option == "follow-tag"):
		target = args.target
		if target is not None:
			follow_tag(target)
		else:
			printUsage()

	elif(option == "follow-location"):
		target = args.target
		if target is not None:
			follow_location(target)
		else:
			printUsage()

	elif(option == "upload"):
		image = args.image
		if image is not None:
			api.uploadPhoto(photo=image, caption=args.caption)
		else:
			printUsage()

	else:
		printUsage()


if __name__ == "__main__":
    main()
