import random

class Movie:
    def __init__(self, title, released, genre, views) :
        self.title=title
        self.released=released
        self.genre=genre
        self.views=views
    
   # def play(self, view=1):
       #visual=input("Proszę podać tytuł filmu lub serialu ")
       #random.choice(Movies_and_series).views =+ 1
       #else:
      #   print "Wystąpił błąd")

class Series (Movie):
    def __init__(self, season, episode, *args, **kwargs): 
        super().__init__(*args, **kwargs)
        self.season=season
        self.episode=episode
    
def showing_titles(list_of_items):
    visual=input("Proszę podać tytuł filmu lub serialu ")
    for item in list_of_items:
        if isinstance(item, Series) and visual in item.title: 
            return ('{} S:{02}E:{02}'.format(item.title, item.season, item.episode))
        return ('''Brak pozycji na liście. Sprawdź czy nie zrobiłeś literówki
        UWAGA: wielkość liter ma znaczenie''')

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
showing_titles(Movies_and_series)


def get_movies(): 
    print([item for item in Movies_and_series if not hasattr(item, 'episode')]) 
get_movies()

def get_series():
    print([item for item in Movies_and_series if hasattr(item, 'episode')]) 
get_series()

def search():
    showing_title(Movies_and_series)
search()

def generate_views():
    i=random.randomint(len(Movies_and_series))
    title[i].views=random.randint(1,100)
generate_views()

def multi_views(): 
    for _ in range (10):
        generate_views()
multi_views()

def top_titles():
    while True:
       try:
           i=int(input("Proszę podać ilość filmów lub seriali do wyświeltenia "))
           for n, item in enumarate(Movies_and_series):
               print(item.title)
               if n>i:
                   break
       except ValueError:
            print("Ups!  To nie jest odpowiednia liczba.  Spróbuj jeszcze raz...")
top_titles()