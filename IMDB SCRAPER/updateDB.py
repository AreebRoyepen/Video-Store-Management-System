from store.models import Product

Product.objects.update(poster = "")


f=open("forDownloads.tsv", "r")
movies = f.read().splitlines()

for i in range(0, len(movies)):

    if(i == 0):
        continue

    lst = movies[i].split("\t")

    id = lst[0]

    relativePath = "/store/static/images/"+id+".jpg"      # dean to explain this part
    print(relativePath)
    
    p = Product.objects.get(ID = id)
    print(p)
    p.poster = relativePath
    p.save()
