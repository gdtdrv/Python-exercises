class Song:
    count = 0

    def __init__(self, title, artist, album, length):
        Song.count = Song.count + 1
        self.title = title
        self.artist = artist
        self.album = album
        self._length = length

    def __str__(self):
        return ('{} - {} from {} - {}'.format(self.artist, self.title, self.album, self.length))

    def __eq__(self, other):
        return(
        self.__class__ == other.__class__ and
        self.title == other.title and
        self.artist == other.artist and
        self.album  == other.album and
        self._length == other._length
        )

    def length(self, seconds = False, minutes = False, hours = False):

        total_lenght = self._length.split(':')

        if seconds:
            return total_lenght[0]
        elif minutes:
            return total_lenght[1]
        elif hours:
            if len(total_lenght)==2: raise Exception('No hours given')
            else: return total_lenght[2]
print('alala')

a = Song('odrin', 'Beatles', 'Yellow Sub', '22:40')

a.length(hours = True)
print(str(a))


