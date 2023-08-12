class Person:
    def __init__(self, name, friends, watchlist, watched):
        self.name = name
        self.friends = friends
        self.watchlist = watchlist
        self.watched = watched
    
    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)
    
    def add_movie_to_watchlist(self, new_movie):
        if new_movie not in self.watchlist:
            self.watchlist.append(new_movie)
 
    def person_watching_a_movie(self, watching):
        if watching not in self.watched:
            self.watched.append(watching)
        if watching in self.watchlist:
            self.watchlist.remove(watching)
