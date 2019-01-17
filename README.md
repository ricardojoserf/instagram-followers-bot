# instagram-followers-bot


## Usage: 

*python main.py -u USERNAME -p PASSWORD -o follow-tag -t TAG*: **Follow users using the tags you introduce**

*python main.py -u USERNAME -p PASSWORD -o follow-location -t LOCATION_ID*: **Follow users from a location**

*python main.py -u USERNAME -p PASSWORD -o super-followback*: **Follow back all the users who you don't follow back**

*python main.py -u USERNAME -p PASSWORD -o super-unfollow*: **Unfollow all the users who don't follow you back**

**NOTE**: Fill "whitelist.txt" file with the accounts you will never want to unfollow

*python main.py -u USERNAME -p PASSWORD -o info*: **Show report**



## Examples:

*python main.py -u USERNAME -p PASSWORD -o follow-tag -t cat* : **Follow users using the tag 'cat'** 

*python main.py -u USERNAME -p PASSWORD -o follow-location -t 127963847* : **Follow users from Spain** 

*python main.py -u USERNAME -p PASSWORD -o super-followback*: **Now you are following users you didn't follow but they followed you**

*python main.py -u USERNAME -p PASSWORD -o super-unfollow*: **Now you are not following users who don't follow you**



## Acknowledgment

The really good repo is the levpasha's one (https://github.com/LevPasha/Instagram-API-python) 


## Note

Tested both in Python2.x (2.7.15rc1) and Python 3.x (3.6.7)
