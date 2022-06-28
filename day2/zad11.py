import os

# os.system("ping 8.8.8.8")
# os.system("dir")

command = os.system("ping 8.8.8.8")
result = command.real()
print(result)