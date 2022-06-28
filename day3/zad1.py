import urllib3

http = urllib3.PoolManager(cert_reqs='CERT_NONE') #pominiecie certyfikatu, bo inaczej blad
res = http.request("GET", "https://me.hack.me/login")
print(res.status)
print(res.data.decode("utf-8"))