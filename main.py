import config, aux_funcs, sys, json, time
from LevPasha.InstagramAPI import InstagramAPI

followers = []
followings = []
api = InstagramAPI(config.USERNAME, config.PASSWORD)

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
	MAXIMO = 50
	tot = 0
	for i in media_id["items"]:
		time.sleep(0.5)
		username = i.get("user")["username"]
		user_id = i.get("user")["pk"]
		api.follow(user_id)
		tot = tot + 1
		print("Following "+str(username)+" (with id "+str(user_id)+")")	
		if(tot >= MAXIMO):
			break
	print("Total: "+str(tot)+" for tag "+tag+" Max val: "+MAXIMO+"\n")

def unfollowOneFollower(username):
	user_id = aux_funcs.get_id(username)
	api.unfollow(user_id)
	print("Unfollowing "+username+" (with id "+user_id+")")

def followOneFollower(username):
	user_id = aux_funcs.get_id(username)
	api.follow(user_id)
	print("Following "+username+" (with id "+user_id+")")	

def printUsage():
	print("Usage: \n+ python main.py info - Show report ")
	print("+ python main.py superFollow {TAGS}- Follow users using the tags you introduce \n+ python main.py superUnfollow - Unfollow all the users who dont follow you back")
	print("+ python main.py unfollow $USERNAME - Unfollow a user \n+ python main.py follow $USERNAME - Follow a user")
	return
	
def main():

	if len(sys.argv) == 1:
		printUsage()

	api.login()

	for i in api.getTotalSelfFollowers():
		followers.append(i.get("username") )

	for i in api.getTotalSelfFollowings():
		followings.append(i.get("username") )

	if( sys.argv[1] == "info"):
		info()

	elif( sys.argv[1] == "superUnfollow"):
		superUnfollow()

	elif( sys.argv[1] == "superFollow"):
		for tag in sys.argv[2:]:
			superFollow(tag)

	elif( sys.argv[1] == "unfollow"):
		unfollowOneFollower(sys.argv[2])

	elif( sys.argv[1] == "follow"):
		followOneFollower(sys.argv[2])

	else:
		printUsage()

if __name__ == "__main__":
    main()
