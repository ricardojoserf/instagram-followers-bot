import sys, json, requests, config, os, webbrowser, urllib2
from selenium import webdriver

def get_id(username, access_token):
	url='https://api.instagram.com/v1/users/search?q='+username+'&access_token='+access_token
	response = requests.get(url)
	respJSON = response.json()
	
	try:
		user_id = respJSON['data'][0]['id']
		return user_id
	except:
		print(respJSON)
		return ""

def get_token(client_id, client_secret, redirect_uri, code):
	
	command = "curl \-F 'client_id="+client_id+"' \
	    -F 'client_secret="+client_secret+"' \
	    -F 'grant_type=authorization_code' \
	    -F 'redirect_uri="+redirect_uri+"' \
	    -F 'code="+code+"' \
	    https://api.instagram.com/oauth/access_token 2>/dev/null"

	resp = os.popen(command).read()

	respJson = json.loads(resp)

	try:

		access_token = respJson.get("access_token")
		if(access_token == None):
			print("ERROR: " + respJson.get("error_message") + ". Please use a new code and add it to the config file. Visit the url https://api.instagram.com/oauth/authorize/?client_id="+client_id+"&redirect_uri="+redirect_uri+"&response_type=code")
			return ""

		else:
			return str(access_token)

	except:
		print("Well this was unexpected...")
		return ""

def get_code(client_id, redirect_uri):
	url = "https://api.instagram.com/oauth/authorize/?client_id="+client_id+"&redirect_uri="+redirect_uri+"&response_type=code"
	#webbrowser.open(url)
	#driver = webdriver.Chrome()
	#url2 = driver.getCurrentUrl()
	#print(url2)
	r = requests.get(url)
	print(r.url)