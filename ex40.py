# evan johanns
# ex 40
# 11/20/19
class Song():

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy bithday to you",
                   "I don't want to get sued",
                   "so I'll stop right there"])
bulls_on_a_parade = Song(["They rally around tha family",
                          "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_a_parade.sing_me_a_song()
