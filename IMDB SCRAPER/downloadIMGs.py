import urllib.request

f = open("errors.txt", "r")

line = f.read().splitlines()

for i in range(1, len(line)):

    if(line[i] == ""):
        continue

    x = line[i].split("\t")

    try:
        urllib.request.urlretrieve(x[1], x[0]+".jpg")
    except :
        print(x[0])
