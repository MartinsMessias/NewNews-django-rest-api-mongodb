class News:

    def __init__(self, title, content, author):
        self.__title = title
        self.__content = content
        self.__author = author

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content):
        self.__content = content

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author):
        self.__author = author