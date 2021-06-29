import random

class Movie:
    def __init__(self, title, released, genre, views) :
        self.title=title
        self.released=released
        self.genre=genre
        self.views=views

class Series (Movie):
    def __init__(self, season, episode, *args, **kwargs): 
        super().__init__(*args, **kwargs)
        self.season=season
        self.episode=episode

self.views=0

def play(self, view=1):
    self.views+=view

if Series:
    print (title + 'S'+ f'{val:02}' + 'E'+ f'{val:02}'.format(season, episode))
else:
    print(title + released)

Movies_and_series= [
        Movie(
            title="Czasem słońce czasem deszcz",
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

def get_movies(): 
   print(sorted(Movies))

def get_series():
    print(sorted(Series))

def search():
    visual=string(input("Proszę podać nazwę filmu lub serialu"))
    for c in title:
        visual = title,key=lambda c: c.title
        print(title + released)    

def generate_views():
    for i in range len(Movies_and_series):
        print(title + views=random.randint(1,100))

def multi_views():
    for i in range (1,10):
        generate_views

def top_titles:
    while True:
       try:
           i=int(input("Proszę podać ilość filmów lub seriali do wyświeltenia")
       break
    except ValueError:
       print("Ups!  To nie jest odpowiednia liczba.  Spróbuj jeszcze raz...")
    print(Movies_and_series[i])