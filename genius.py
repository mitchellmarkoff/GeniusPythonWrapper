import lyricsgenius
import pprint

genius = lyricsgenius.Genius("jUv62p0c58zg7c4fzIwTOYLLiw3whYP36jGhBOKnvmBjf2vkHeP49SU3X8vCMgc1")
artist = genius.search_artist("Vanilla Ice", max_songs=3, sort="title")
song = genius.search_song("Ice Ice Baby", artist.name)
# search = genius.("a lot 21 savage lyrics")
print(song.lyrics)
# print(search)
# pprint.pprint(search)