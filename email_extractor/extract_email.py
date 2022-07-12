fname = input("Enter file name: (Press Enter) \n ")
if len(fname) < 1:
    fname = "email.txt.py"

fh = open(fname)
count = 0
lst = []

for line in fh:
    line = line.rstrip()
    if not line.startswith('From'): continue
    if line.startswith('From:'): continue
    email = line.split()
    count += 1


    print(email[1])

print("\nThere are", count, "sender emails in this file")
