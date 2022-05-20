class Artist:
    __firstName = ""
    __lastName = ""
    __birthYear = 0
    __albums = []
    __singles = []

    def __init__(self, firstName, lastName, birthYear, albums, singles):
        self.__firstName = firstName.strip()
        self.__lastName = lastName.strip()
        self.__birthYear = birthYear
        self.__albums = albums
        self.__singles = singles

    def mostLikedSong(self):
        allSongs = []
        for album in self.__albums:
            for eachSong in album.getSongs():
                allSongs.append(eachSong)

        for song in self.__singles:
            allSongs.append(song)

        mostLikedOne = -9223372036854775807
        mostLikedSong = ""

        for eachSong in allSongs:
            if eachSong.getLikes() > mostLikedOne:
                mostLikedOne = eachSong.getLikes()
                mostLikedSong = eachSong

        return mostLikedSong.__str__()

    def amountOfLikesTheMostLikedSongHas(self):
        allSongs = []
        for album in self.__albums:
            for eachSong in album.getSongs():
                allSongs.append(eachSong)

        for song in self.__singles:
            allSongs.append(song)

        mostLikedOne = -9223372036854775807

        for eachSong in allSongs:
            if eachSong.getLikes() > mostLikedOne:
                mostLikedOne = eachSong.getLikes()

        return mostLikedOne

    def leastLikedSong(self):
        allSongs = []
        for album in self.__albums:
            for eachSong in album.getSongs():
                allSongs.append(eachSong)

        for song in self.__singles:
            allSongs.append(song)

        leastLikedOne = 9223372036854775807
        leastLikedSong = ""

        for eachSong in allSongs:
            if leastLikedOne > eachSong.getLikes():
                leastLikedOne = eachSong.getLikes()
                leastLikedSong = eachSong

        return leastLikedSong.__str__()

    def totalLikes(self):
        allSongs = []
        for album in self.__albums:
            for eachSong in album.getSongs():
                allSongs.append(eachSong)

        for song in self.__singles:
            allSongs.append(song)

        totalLikes = 0

        for eachSong in allSongs:
            totalLikes += eachSong.getLikes()

        return totalLikes

    # getters
    def getFirstName(self):
        return self.__firstName

    def getSecondName(self):
        return self.__lastName

    def getBirthYear(self):
        return self.__birthYear

    def getAlbums(self):
        return self.__albums

    def getSingles(self):
        return self.__singles

    # method for string representation
    def __str__(self):
        totalLikes = self.totalLikes()
        return f"Name:{self.__firstName} {self.__lastName},Birth year:{self.__birthYear},Total likes:{totalLikes}"
