from store.models import Product

p = Product.objects.get(ID = "tt0910970")
p.delete()

p = Product.objects.get(ID = "tt0089881")
p.delete()

p = Product.objects.get(ID = "tt0060107")
p.delete()

p = Product.objects.get(ID = "tt1954470")
p.delete()
