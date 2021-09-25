import random
from operator import itemgetter

class Movie:
    def __init__(self, title, released, genre, views) :
        self.title=title
        self.released=released
        self.genre=genre
        self.views=views
    
   # def play(self, view=1):
    #   visual=input("Proszę podać tytuł filmu lub serialu ")
    #   if visual in Movies_and_series:  
    #     print (self.views += view) #podkreśla '+=' i chce zamiast tego nawias - czemu?
    #   else:
      #   print "Wystąpił błąd")

class Series (Movie):
    def __init__(self, season, episode, *args, **kwargs): 
        super().__init__(*args, **kwargs)
        self.season=season
        self.episode=episode
    
def showing_titles():
    visual=input("Proszę podać tytuł filmu lub serialu ")
    if visual in Series.title: #nie rozumiem dlaczego Series nie ma atrybutu title
        return (title + 'S'+ f'{val:02}' + 'E'+ f'{val:02}'.format(season, episode)) #nie jestem pewna tego formatowania
    elif visual in Movie.title:
        return(self.title + self.released)
    else:
        return ('''Brak pozycji na liście. Sprawdź czy nie zrobiłeś literówki
        UWAGA: wielkość liter ma znaczenie''')
showing_titles()

Movies_and_series= [
        Movie(
            title="Czasem słońce, czasem deszcz",
            released=2001,
            genre="bollywood",
            views=620
        ),  
        Movie(
            title="Mad hot ballroom",
            released=2005,
            genre="Documentary",
            views=250
        ),
        Movie(
            title="Motyl i skafander",
            released=2007,
            genre="Biography/drama",
            views=795
        ),
        Movie(
            title="Pina",
            released=2011,
            genre="Documentary",
            views=216
        ),
        Movie(
            title="Buena Vista Social Club",
            released=1999,
            genre="Documentary",
            views=98
        ),
        Series(
            title="Przyjaciele",
            released=1994,
            genre="comedy",
            views=200,
            season=1,
            episode=2
        ),
        Series(
            title="Little Britain",
            released=2003,
            genre="Comedy",
            views=2000,
            season=2,
            episode=6
        ),
        Series(
            title="Ulica sezamkowa",
            released=1969,
            genre="Animation",
            views=260,
            season=6,
            episode=99
        )
    ]
'''
#def get_movies(): 
 #   print(Movies_and_series.sort(key=Movie)) traktuje 'movie' jak title
#get_movies()

def get_series():
    print(Movies_and_series.sort(key=itemgetter("Series"))) #nie ma takiego atrybutu jak series
get_series()

def search():
  #  showing_title()
search()

def generate_views():
    i = random.randint(len(Movies_and_series))
    print(title[i] + views=random.randint(1,100))
generate_views()

def multi_views(): #wydaje mi się, że to będzie działać jeśli generate_views będzie poprawna
    for i in range (10):
        generate_views()
multi_views()
'''
def top_titles():
    while True:
       try:
           i=int(input("Proszę podać ilość filmów lub seriali do wyświeltenia "))
           for i in range(len(Movies_and_series)): #bez tej pętli wypisywał miejsce w pamięci filmu o indexie i    
               print(title)#title jest niezdefiniowane a w self.title self jest niezdefiniowane
           break
       except ValueError:
            print("Ups!  To nie jest odpowiednia liczba.  Spróbuj jeszcze raz...")
top_titles() 