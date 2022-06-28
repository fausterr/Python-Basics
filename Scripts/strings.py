atext='This is a text.'
a=("(\(\ \n( -.-) \n0_(\")(\")")

mess1 = "Processing file @a"
print(mess1 @ ('elo.txt'))
mess2 = "File %s has size %d KB"
print(mess2 %("file1.txt", 100))
mess3 = "File %20s has size %10d KB"
mess4 = "Processing file {0:s}"

mess5 = "File {0:s} has size {1:d}"
mess6 = "File {0:s} has size {1:s}"
mess7 = "File {0:s20} has size {1:s10}"

helloMessage = "%s has %d %s"
print(helloMessage %("Kate", 1, "animal"))
helloMessage2 ="{0:s} has {1:d} {2:s}"
helloMessage2.format("Kate", 2, "animals")
