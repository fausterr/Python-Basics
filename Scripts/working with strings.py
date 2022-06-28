s="A python scripts"
print(s[0])
print(s[2:7])
print(s[2:8])
print(s[:8])
print(s[8:])
print(s[2:9999])
print(s[666:9999]) #pusty

message = 'Document "cv.doc" was printed od printer: XEROX'
print(message.find(':'))
print(message[message.find(':'):])
print(message[message.find(':')+2:])

tmp = message[message.find('"')+1:]
print(tmp[:tmp.find('"')])
