import lyricsgenius
import pprint

genius = lyricsgenius.Genius("jUv62p0c58zg7c4fzIwTOYLLiw3whYP36jGhBOKnvmBjf2vkHeP49SU3X8vCMgc1")
artist = genius.search_artist("Vanilla Ice", max_songs=3, sort="title")
song = genius.search_song("Ice Ice Baby", artist.name)
#Uncomment Code to run search for specific song or keyword
# search = genius.("you give love a bad name")
# print(search)
# pprint.pprint(search)
print(song.lyrics)
