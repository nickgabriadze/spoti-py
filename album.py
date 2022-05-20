class Album:
    __title = ""
    __releaseYear = 0

    def __init__(self, title, releaseYear):
        self.__title = title.strip()
        self.__releaseYear = releaseYear
        self.__songs = []

    # method for adding songs
    def addSongs(self, *listOfSongs):
        addedSongs = 0
        ourSongs = [song for song in listOfSongs]
        for eachOne in ourSongs:
            howMany = 0
            for songs in self.__songs:
                if eachOne.getTitle() == songs.getTitle() and \
                        eachOne.getReleaseYear() == songs.getReleaseYear() and \
                        eachOne.getDuration() == songs.getDuration():
                    howMany += 1
            if howMany == 0:
                self.__songs.append(eachOne)
                addedSongs += 1

        return addedSongs

    # sorting methods

    def sortBy(self, byKey, reverse):
        if reverse:
            return sorted(self.__songs, key=byKey)
        else:
            return (sorted(self.__songs, key=byKey))[::-1]

    def sortByName(self, reverse):
        sortedList = [song for song in self.__songs]

        # using bubble sort algorithm
        for n, song in enumerate(sortedList):
            for i, eachSong in enumerate(sortedList):
                if (sortedList[n].getTitle()).lower() < (sortedList[i].getTitle()).lower():
                    sortedList[i], sortedList[n] = sortedList[n], sortedList[i]

        if reverse:
            return sortedList

        return sortedList[::-1]

    def sortByPopularity(self, reverse):
        sortedList = [song for song in self.__songs]

        # using bubble sort algorithm
        for n, song in enumerate(sortedList):
            for i, eachSong in enumerate(sortedList):
                if sortedList[n].getLikes() < sortedList[i].getLikes():
                    sortedList[i], sortedList[n] = sortedList[n], sortedList[i]

        if reverse:
            return sortedList

        return sortedList[::-1]

    def sortByDuration(self, reverse):
        sortedList = [song for song in self.__songs]

        # using bubble sort algorithm
        for n, song in enumerate(sortedList):
            for i, eachSong in enumerate(sortedList):
                if sortedList[n].getDuration() < sortedList[i].getDuration():
                    sortedList[i], sortedList[n] = sortedList[n], sortedList[i]

        if reverse:
            return sortedList

        return sortedList[::-1]

    def sortByReleaseYear(self, reverse):
        sortedList = [song for song in self.__songs]

        # using bubble sort algorithm
        for n, song in enumerate(sortedList):
            for i, eachSong in enumerate(sortedList):
                if sortedList[n].getReleaseYear() < sortedList[i].getReleaseYear():
                    sortedList[i], sortedList[n] = sortedList[n], sortedList[i]

        if reverse:
            return sortedList

        return sortedList[::-1]

    # method to get the total likes of album
    def getTotalLikesOfAlbum(self):
        totalLikes = 0

        for song in self.__songs:
            totalLikes += song.getLikes()

        return totalLikes

    # getter methods
    def getTitle(self):
        return self.__title

    def getReleaseYear(self):
        return self.__releaseYear

    def getSongs(self):
        return self.__songs

    # string representation of an Album
    def __str__(self):
        songs = list(map(lambda song: song.__str__(), self.__songs))
        everySong = '{' + '|'.join(songs) + '}'
        return f"Title:{self.__title},Release year:{self.__releaseYear},songs:{everySong}"
