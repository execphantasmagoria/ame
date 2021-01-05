import sys

sys.stdout = open("out.txt", "w")

def xyz():
    print("test")
xyz()


sys.stdout.close()