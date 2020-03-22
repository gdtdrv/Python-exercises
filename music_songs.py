class Song:
    count = 0

    def __init__(self, title, artist, album, length):
        Song.count = Song.count + 1
        self.title = title
        self.artist = artist
        self.album = album
        self.len = length

    def __str__(self):
        return ('{} - {} from {} - {}'.format(self.artist, self.title, self.album, self.len))

    def __eq__(self, other):
        return(
        self.__class__ == other.__class__ and
        self.title == other.title and
        self.artist == other.artist and
        self.album  == other.album and
        self.len == other.len
        )

    def length(self, seconds = False, minutes = False, hours = False):

        total_lenght = self.len.split(':')

        if seconds:
            return str(total_lenght[-1])
        elif minutes:
            return str(total_lenght[-2])
        elif hours:
            if len(total_lenght)==2: raise Exception('No hours given')
            else: return str(total_lenght[-3])
print('alala')

a = Song('odrin', 'Beatles', 'Yellow Sub', '11:22:40')

print(a.length(hours = True))

print(str(a))


