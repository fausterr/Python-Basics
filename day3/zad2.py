import requests

res = requests.get("https://me.hack.me", verify=False)
#print(help(res))   cos jak manual
#print(dir(res))

print(res.status_code)
print(res.text)