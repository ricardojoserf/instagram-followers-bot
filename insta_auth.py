import re, sys
import os, requests

CLIENT_ID = ""
REDIRECT_URI = "http://none.com"

url1 = "https://www.instagram.com/oauth/authorize/?client_id="+CLIENT_ID+"&redirect_uri="+REDIRECT_URI+"&response_type=code"
os.system("sleep 1")
r = requests.head(url1,allow_redirects=True)
print r.url


code = ""

url2="curl -F 'client_id=5c774ac3750647dab08353c3aa456f49' \
    -F 'client_secret=f557eb7c8c114044a7d24e1fced3bbf9' \
    -F 'grant_type=authorization_code' \
    -F 'redirect_uri=http://none.com' \
    -F 'code="+code+"' \
    https://api.instagram.com/oauth/access_token"
#result2 = os.popen(url2).read()
# print result2
