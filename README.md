# instagram-followers-bot

Functionality: 

- **Info**: Show report

- **Follow users**: from tag, from location, from a list or follow back who you do not follow back

- **Unfollow users**: who do not follow you back or all of them

---------------------

## Usage: 

**Show report (who follows, unfollows, follows you back):**
```
python main.py -u USERNAME -p PASSWORD -o info
```

**Follow users using the tag you introduce:**

```
python main.py -u USERNAME -p PASSWORD -o follow-tag -t TAG
```

**Follow users from a location:**

```
python main.py -u USERNAME -p PASSWORD -o follow-location -t LOCATION_ID
```

**Follow back all the users who you don't follow back:**
```
python main.py -u USERNAME -p PASSWORD -o super-followback
```

**Follow users from a list:**

```
python main.py -u USERNAME -p PASSWORD -o follow-list -t USER_LIST
```

**Unfollow all the users who don't follow you back:**
```
python main.py -u USERNAME -p PASSWORD -o super-unfollow
```
**NOTE**: Fill "whitelist.txt" file with the accounts you will never want to unfollow


**Unfollow all the users:**
```
python main.py -u USERNAME -p PASSWORD -o unfollow-all
```
**NOTE**: Fill "whitelist.txt" file with the accounts you will never want to unfollow

---------------------

## Examples:

*python main.py -u USERNAME -p PASSWORD -o follow-tag -t cat* : **Follow users using the tag 'cat'** 

*python main.py -u USERNAME -p PASSWORD -o follow-location -t 127963847* : **Follow users from Spain** 

*python main.py -u USERNAME -p PASSWORD -o super-followback*: **Now you are following users you didn't follow but they followed you**

*python main.py -u USERNAME -p PASSWORD -o follow-list -t userlist.txt* : **Follow users in each line of userlist.txt** 

*python main.py -u USERNAME -p PASSWORD -o super-unfollow*: **Now you are not following users who don't follow you**


---------------------


## Acknowledgment

The really good repo is the levpasha's one (https://github.com/LevPasha/Instagram-API-python) 

---------------------

## Note

Tested both in Python2.x (2.7.15rc1) and Python 3.x (3.6.7)