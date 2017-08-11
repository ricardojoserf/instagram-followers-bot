import sys, json, requests, os
import argparse

def get_args():
  parser = argparse.ArgumentParser()
  parser.add_argument('-u', '--user', required=True, action='store', help='Username')
  parser.add_argument('-p', '--password', required=True, action='store', help='Password')
  parser.add_argument('-o', '--option', required=True, action='store', help='Option')
  parser.add_argument('-t', '--target', required=False, action='store', help='Target(s)')
  my_args = parser.parse_args()
  return my_args


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
