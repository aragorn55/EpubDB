from fanfic import FanFic
from fanfic import Author

class FanFicEBook(FanFic):
    _FilePath = ''
    _Packaged = ''
    _Tags = []
    _Pairings = []
    _Publisher = ''

    def __init__(self):
        self._Url = ""
        self._Title = ""
        self._Published = ""
        self._Updated = ""
        self._CharactersString = ""
        self._Summary = ""
        self._Rating = ""
        self._GenreString = ""
        self._Words = 0
        self._Characters = []
        self._Relationships = []
        self._Fandoms = []
        self._Chapters = 0
        self._FFNetID = ""
        self._FicID = 0
        self._Status = ''
        self._Genres = []
        self._Author = Author()
        self._FilePath = ''
        self._Packaged = ''
        self._Tags = []
        self._Pairings = []
        self._Publisher = ''

    def reset(self):
        self._Url = ""
        self._Title = ""
        self._Published = ""
        self._Updated = ""
        self._CharactersString = ""
        self._Summary = ""
        self._Rating = ""
        self._GenreString = ""
        self._Words = 0
        self._Characters = []
        self._Relationships = []
        self._Fandoms = []
        self._Chapters = 0
        self._FFNetID = ""
        self._FicID = 0
        self._Genres = []
        self._Author.reset()
        self._Status = ''
        self._FilePath = ''
        self._Packaged = ''
        self._Tags = []
        self._Pairings = []
        self._Publisher = ''


    @property
    def FilePath(self):
        return self._FilePath

    @FilePath.setter
    def FilePath(self, vsFilePath):
        self._FilePath = vsFilePath

    @property
    def Packaged(self):
        return self._Packaged

    @Packaged.setter
    def Packaged(self, vsPackaged):
        self._Packaged = vsPackaged

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, vTags):
        self._Tags = vTags

    @property
    def Pairings(self):
        return self._Pairings

    @Pairings.setter
    def Pairings(self, vs_Pairings):
        self._Pairings = vs_Pairings

    @property
    def Publisher(self):
        return self._Publisher

    @Publisher.setter
    def Publisher(self, vsPublisher):
        self._Publisher = vsPublisher



