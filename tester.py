import sys

sys.stdout = open("out.txt", "w")

k = input("hey: ")

print(f"hey {k}")

sys.stdout.close()