#Connect to IMDB SQL Server
from imdb import IMDb

#Create an object of the class IMDb
ia = IMDb()

#Create File for writing TitleID
f = open("titleID.txt","w")

#Scrape Top 250 Movies
topMovies = ia.get_top250_movies()

#The ID here is of type string
for item in topMovies:
	f.write("tt"+item.movieID+"\n")

#Each title ID needs to have the letter tt appended to the front of the titleID in order to be used online

f.close()