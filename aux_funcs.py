import sys, json, requests, os
import argparse

def get_args():
  parser = argparse.ArgumentParser()
  parser.add_argument('-u', '--user', required=True, action='store', help='Username')
  parser.add_argument('-p', '--password', required=True, action='store', help='Password')
  parser.add_argument('-o', '--option', required=True, action='store', help='Option')
  parser.add_argument('-t', '--target', required=False, action='store', help='Target(s)')
  parser.add_argument('-i', '--image', required=False, action='store', help='Image')
  parser.add_argument('-c', '--caption', required=False, action='store', help='Caption')
  my_args = parser.parse_args()
  return my_args


def get_id(username):
	url = "https://www.instagram.com/web/search/topsearch/?context=blended&query="+username+"&rank_token=0.3953592318270893&count=1"
	response = requests.get(url)
	respJSON = response.json()
	try:
		user_id = str( respJSON['users'][0].get("user").get("pk") )
		return user_id
	except:
		print(respJSON)
		return "Unexpected error"