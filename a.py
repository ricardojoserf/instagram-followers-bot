import re, sys
import os, requests
from python_api_instagram.instagramAPI import instagramAPI

access_token = ""

instagram = instagramAPI(access_token)

print 1

print instagram.users_self()

print 2

print instagram.users_self_media_liked()

print 3

print instagram.media_self_recent()
