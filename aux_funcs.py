import sys, json, requests, os


def get_id(username):
	url="https://www.instagram.com/"+username+"/?__a=1"
	response = requests.get(url)
	respJSON = response.json()
	try:
		user_id = str(respJSON['user'].get("id"))
		return user_id
	except:
		print(respJSON)
		return "."
