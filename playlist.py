import music_songs as m
import pandas as pd
import matplotlib.pyplot as plt

class Playlist:

    def __init__(self, name, repeat=False, shuffle= False):

        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.content = []

    def add_song(self, song):

        self.content.append(song)
        return self.content

    def add_songs(self,*args):

        for i in args:
            self.content.append(i)

        return self.content

    def total_lenght(self):
        total = 0
        for s in self.content:
            total += s.length(seconds = True)

        return ("Total length of the playlist is {} munites").format(total/60)

    def artists(self):

        all_artists = {}
        for s in self.content:

            all_artists[s.artist] = all_artists.get(s.artist, 0) + 1

        artist_dataframe = pd.DataFrame.from_dict(all_artists, orient = 'index')
        # artist_dataframe.index = artist_dataframe['artist']
        artist_dataframe.columns = ['count']

        return artist_dataframe #plt.bar(artist_dataframe.artist, artist_dataframe.count)



b = m.Song('Lucy in the Sky with Diamonds', 'the Beatles', 'Yellow Submarine', '3:40')
f = m.Song('Under the Bridge', 'Red Hot Chili Peppers', 'Blood Sugar Sex Magik', '5:30')

e = m.Song('One', 'U2', 'Achtung Baby', '5:70')
d = m.Song('With or Without You', 'U2', 'The Joshua Tree', '2:30')
c = Playlist(name = 'Led Zeppelin')
print(c.add_song(b))

print(c.add_songs(d,e,f))
print(c.total_lenght())

artists_plot = c.artists()
print(artists_plot)
# artists_plot.show()
# print(artists_plot)

print('zebra')