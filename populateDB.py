from store.models import Product
import random

f=open("raw.tsv", "r")
movies = f.read().splitlines()

for i in range(0, len(movies)):
        
    if(i == 0):
        continue

    lst = movies[i].split("\t")

    id = lst[0]
    title = lst[1]
    genre = lst[2]
    runtime = lst[3]
    adult = lst[4]
    bob = False
    if(adult == "Yes"):
        bob = True
    url = lst[5]
    disc = lst[6]

    
    p  = Product(ID = id,
	originalTitle = title,
	isAdult = bob,
	runtime = runtime,
	genres = genre,
	poster = url,
	description = disc,
	isBooked = False,
	price = random.randint(80, 101))

    p.save()
    



