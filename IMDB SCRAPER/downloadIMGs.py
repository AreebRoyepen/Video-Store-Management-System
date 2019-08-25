import urllib.request

f = open("forDownloads.tsv", "r")

line = f.read().splitlines()

for i in range(1, len(line)):

    x = line[i].split("\t")

    try:
        urllib.request.urlretrieve(x[1], x[0]+".jpg")
    except :
        pass
