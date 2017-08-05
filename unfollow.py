import config, aux_funcs, json
from InstagramAPI import InstagramAPI as instapi

api = instapi.InstagramAPI(config.USERNAME, config.PASSWORD)

api.login()

# user_id = aux_funcs.get_id(username, config.ACCESS_TOKEN)
# user_tok = aux_funcs.get_token(config.CLIENT_ID, config.CLIENT_SECRET, config.REDIRECT_URI, config.CODE)
# aux_funcs.get_code(config.CLIENT_ID, config.REDIRECT_URI)

followers = []
followings = []

for i in api.getTotalSelfFollowers():
	followers.append(i.get("username") )

for i in api.getTotalSelfFollowings():
	followings.append(i.get("username") )

print("\n\n\nI follow them but they dont follow me:\n")
tot = 0
for i in followings:
	if i not in followers:
		print(i)
		tot=tot+1
print("Total: "+str(tot))

print("\n\n\nThey follow me but i dont follow them:\n")
tot = 0
for i in followers:
	if i not in followings:
		print(i)
		tot=tot+1
print("Total: "+str(tot))

