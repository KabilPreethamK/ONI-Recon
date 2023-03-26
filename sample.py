with open("./data/network/local_ip.txt","r") as f:
    lines = [line.rstrip('\n') for line in f]

for i in range(0, len(lines)):
    print(lines[i])