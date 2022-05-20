class Song:
    __title = ""
    __releaseYear = 0
    __duration = 60
    __likes = 0

    def __init__(self, title, releaseYear, duration=60, likes=0):
        self.__title = title.strip()
        self.__releaseYear = releaseYear
        self.__duration = duration
        self.__likes = likes

    # methods to change the amount of likes
    def like(self):
        self.__likes += 1

    def unlike(self):
        self.__likes -= 1

    # method to change the duration of the song
    def setDuration(self, time):
        if time > 720 or time < 0 or self.__duration == time:
            return False
        else:
            self.__duration = time
            return True

    # getter methods
    def getTitle(self):
        return self.__title

    def getReleaseYear(self):
        return self.__releaseYear

    def getDuration(self):
        return self.__duration

    def getLikes(self):
        return self.__likes

    # String representation of the song
    def __str__(self):
        title, duration, releaseYear, likes = self.__title, self.__duration / 60, self.__releaseYear, self.__likes
        return f"Title:{title},Duration:{duration} minutes,Release year:{releaseYear},Likes:{likes}"
