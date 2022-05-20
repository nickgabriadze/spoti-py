from album import Album
from artist import Artist
from song import Song


class SpotiPy:

    def __init__(self):
        self.__artists = []

    # getter
    def getArtists(self):
        return self.__artists

    # function to add artists
    def addArtists(self, *artist):
        ourArtists = [song for song in artist]
        for eachOne in ourArtists:
            howMany = 0
            for artist in self.__artists:
                if eachOne.getFirstName() == artist.getFirstName() and \
                        eachOne.getSecondName() == artist.getSecondName() and \
                        eachOne.getBirthYear() == artist.getBirthYear():
                    howMany += 1
            if howMany == 0:
                self.__artists.append(eachOne)

    # method for finding out who is the most liked artist
    def getTopTrendingArtist(self):
        mostLikedIndicator = -9223372036854775807
        topTrendingArtist = ""
        for index, artist in enumerate(self.__artists):
            if mostLikedIndicator < artist.totalLikes():
                mostLikedIndicator = artist.totalLikes()
                topTrendingArtist = artist.getFirstName(), artist.getSecondName()

        return tuple(topTrendingArtist)

    # method for finding the most liked album
    def getTopTrendingAlbum(self):
        trendingAlbumIndicator = -9223372036854775807
        topTrendingAlbum = ""
        for eachArtist in self.__artists:
            for everyAlbum in eachArtist.getAlbums():
                if trendingAlbumIndicator < everyAlbum.getTotalLikesOfAlbum():
                    trendingAlbumIndicator = everyAlbum.getTotalLikesOfAlbum()
                    topTrendingAlbum = everyAlbum.getTitle()

        return topTrendingAlbum

    def getTopTrendingSong(self):
        topTrendingSongIndicator = -9223372036854775807
        topTrendingSong = ""

        for eachArtist in self.__artists:
            artistsTopTrendingSong = eachArtist.mostLikedSong()
            likesOfThatSong = eachArtist.amountOfLikesTheMostLikedSongHas()
            if topTrendingSongIndicator < likesOfThatSong:
                topTrendingSongIndicator = likesOfThatSong
                topTrendingSong = artistsTopTrendingSong

        return topTrendingSong

    def loadFromFile(self, pathToFile):
        with open(pathToFile, "r") as artistsFile:
            artistsFile = artistsFile.readlines()
            artists = "".join(artistsFile).split("#")
            artistsList = []
            for index, everyArtist in enumerate(artists):
                if index > 0:
                    artistsName = everyArtist.split(",")[0]
                    artistsLastName = everyArtist.split(",")[1]
                    artistsBirthYear = int(everyArtist.split(",")[2])
                    albumsList = []
                    singlesList = []
                    for sIndex, singles in enumerate(everyArtist.split("@")):
                        if sIndex > 0:
                            for singlesListCounter in range(1, len(singles.split("|"))):
                                singleName = singles.split("|")[singlesListCounter].split(",")[0]
                                singleDuration = float(singles.split("|")[singlesListCounter].split(",")[1]
                                                       .split(" ")[0]) * 60
                                singleReleaseDate = int(singles.split("|")[singlesListCounter].split(",")[2])
                                singleLikes = int(singles.split("|")[singlesListCounter].split(",")[3].split(" ")[0]
                                                  .strip())
                                newSong = Song(singleName, singleReleaseDate, singleDuration, singleLikes)
                                singlesList.append(newSong)

                    for aIndex, albums in enumerate(everyArtist.split("%")):
                        if aIndex > 0:
                            albumName = albums.split(",")[0]
                            albumReleaseYear = int(albums.split(",")[1])
                            newAlbum = Album(albumName, albumReleaseYear)
                            for sIndex, songs in enumerate(albums.split("|")):
                                if sIndex > 0:
                                    songName = songs.split(",")[0]
                                    songDuration = float(songs.split(",")[1].split(" ")[0]) * 60
                                    songReleaseYear = int(songs.split(",")[2])
                                    songLikes = int(songs.split(",")[3].split(" ")[0].strip())
                                    createSong = Song(songName, songDuration, songReleaseYear, songLikes)
                                    newAlbum.addSongs(createSong)
                            albumsList.append(newAlbum)
                        createArtist = Artist(artistsName, artistsLastName, artistsBirthYear, albumsList, singlesList)
                    artistsList.append(createArtist)
