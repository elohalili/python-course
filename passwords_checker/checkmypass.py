import hashlib
import sys

import requests


# function to get data from the api
def request_api_data(query_char):
    url = f'https://api.pwnedpasswords.com/range/{query_char}'
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f'Error with the api: {res.status_code}, check out the api and try again')
    return res


# functions that returns the count of the given password leaks
def get_password_leaks_count(hashes, hash_to_check):
    # knowing that the data will be structured like this:
    # SHA-1 tail hash : count
    # generate a tuple that will contain (hash, count)
    hashes = (line.split(':') for line in hashes.splitlines())
    # iterate through the hashes and find a match
    for hash_pass, count in hashes:
        if hash_pass == hash_to_check:
            return count
    return 0


def pwnd_api_check(password):
    # create the SHA-1 uppercased string hash
    # N.B. password string has to be encoded before generating the hash
    sha1_pass = hashlib.sha1(password.encode('UTF-8')).hexdigest().upper()
    # call api passing the first 5 char of the hash
    res = request_api_data(sha1_pass[:5])
    # check the leaks
    return get_password_leaks_count(res.text, sha1_pass[5:])


def main(passwords):
    if not passwords:
        print('You have to input some passwords!')
        return

    passwords = sys.argv[1:]
    for password in passwords:
        count = pwnd_api_check(password)
        if int(count) > 0:
            print(f'D: ...your password has been leaked {count} times...')
        else:
            print('Great! Yout password has never been leaked')


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
