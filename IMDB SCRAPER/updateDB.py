from store.models import Product

Product.objects.update(poster = "")


f=open("forDownloads.tsv", "r")
movies = f.read().splitlines()

for i in range(0, len(movies)):

    if(i == 0):
        continue

    lst = movies[i].split("\t")

    id = lst[0]
    poster = lst[1]

    relativePath = ""       # dean to explain this part
    Product.objects.filter(originalTitle = id).update(poster = relativePath+id)