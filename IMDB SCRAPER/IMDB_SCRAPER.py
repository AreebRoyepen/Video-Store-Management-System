import requests
from bs4 import BeautifulSoup
import re
from imdb import IMDb

#We write into file
write_file = open("raw.tsv","w")

#Write headings
write_file.write("TitleID\tMovie Title\tGenres\tRuntime\tAdult\tURL\tDESCRIPTION\n")

#Read from file
read_file = open("titleID.txt","r")

def posterURL(titleID):
    #Get Movie Year for url for yts.lt
    year = movieYear(titleID)

    #Get Movie Name to Edit
    name = movieName(titleID)

    #Remove Special Characters
    name = cleanMovieName(name)

    #Yify URL
    url = "https://img.yts.lt/assets/images/movies/"+name+"_"+str(year)+"/large-cover.jpg"

    r = requests.get(url)
    if(r.status_code == 404):
    	print(titleID)
    
    return url

def descr(titleID,page):
    
    #Create an instance of BeautifulSoup
    soup = BeautifulSoup(page.content,'html.parser')
    
    #GETTING DESCRIPTION
    desc = soup.find_all('div',class_ = 'summary_text')
    text = (desc[0].get_text()).strip()#Here is The Movie Description

    return text

def movieName(titleID):
    #Create an instance of class IMDb
    ia = IMDb()
    newID = titleID.replace('t','')
    movie = ia.get_movie(newID)
    return movie['title']

def movieGenre(titleID):
    #Create an instance of class IMDb
    ia = IMDb()
    newID = titleID.replace('t','')
    movie = ia.get_movie(newID)
    genreString = ", ".join([str(x) for x in movie['genres']])
    return genreString

def isAdult(titleID,page):
    
    #Create an instance of BeautifulSoup
    soup = BeautifulSoup(page.content,'html.parser')

    #container = soup.find_all('div',class_ = 'txt-block')
    container = soup.find_all('div',class_ = 'subtext')

    flag = "No"
    
    span = (container[0].text).strip()

    span_list = span.split('\n')

    if(span_list[0].strip()=='R'):
        flag = "Yes"

    return flag

def movieRuntime(titleID,page):
    
    #Create an instance of BeautifulSoup
    soup = BeautifulSoup(page.content,'html.parser')
    
    #GETTING Runtime
    subText = soup.find_all('div',class_ = 'subtext')

    time = (subText[0].find('time'))

    return time.get_text().strip()

def movieYear(titleID):
    #Create an instance of class IMDb
    ia = IMDb()
    newID = titleID.replace('t','')
    movie = ia.get_movie(newID)
    return movie['year']

def cleanMovieName(dirty):
    movie_name = dirty.replace(" ", "_")
    index = 0
    for char in movie_name:
        if char.isalnum()==False and char != "_":
            movie_name = movie_name.replace(char,"")
    for char in movie_name:
        if char == "_" and movie_name[index+1]=="_":
            movie_name = movie_name[:index]+movie_name[index+1:]
        if(index < len(movie_name)-1):   
            index = index+1
    return movie_name.lower()
    

def scraper(titleID):
    global write_file,read_file

    #URL
    url = "http://www.imdb.com/title/"+titleID
    
    #Get Page
    page = requests.get(url)

    #Function call
    pic_url = posterURL(titleID)#Returns String
    text = descr(titleID,page)#Returns String
    movieTitle = movieName(titleID)#Returns String
    genre = movieGenre(titleID)#Returns Comma Separated String (NOT LIST OF STRINGS). Example output: Crime, Drama, Mystery, Thriller
    adult = isAdult(titleID,page)#Returns String (Yes if Adult, No otherwise), reason can't concatenate booleans to strings when collecting massive string
    runtime = movieRuntime(titleID,page)#Returns String of time Format: 1h 35min

    #Concatenate Everything for a Movie
    Massive_String = titleID+"\t"+movieTitle+"\t"+genre+"\t"+runtime+"\t"+adult+"\t"+pic_url+"\t"+text+"\n"

    #Finally write line to file
    write_file.write(Massive_String)

#Make Function Call
movies = read_file.read()
movies_list = movies.splitlines()

counter=0

for line in movies_list:
    scraper(line)
    counter+=1
    print(counter)

#close our files
write_file.close()
read_file.close()
