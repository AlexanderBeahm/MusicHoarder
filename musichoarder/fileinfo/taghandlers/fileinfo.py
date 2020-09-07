import mutagen
import os
from abc import ABC, abstractmethod

class FileInfo:
    '''
    Represents base file information with file and tag appropriate accessors.
    '''
    def __init__(self, filename):
        if filename == '' or filename is None:
            raise FileNotFoundError
        self.filename = filename
        self.file = mutagen.File(filename)
        self.file_extension = os.path.splitext(filename)[1]

    @abstractmethod
    def is_audio_file(self):
        '''
        Returns if audio file or not.
        '''
        return False

    @abstractmethod
    def get_file_extension(self):
        '''
        Returns file extension.
        '''
        return self.file_extension

    @abstractmethod
    def get_filename(self):
        '''
        Returns full file name.
        '''
        return self.filename

    @abstractmethod
    def get_fileinfo(self):
        '''
        Returns the loaded file information object.
        '''
        return self.file

    @abstractmethod
    def get_artist(self):
        '''
        Returns file artist.
        '''
        raise NotImplementedError

    @abstractmethod
    def get_album(self):
        '''
        Returns file artist.
        '''
        raise NotImplementedError

    @abstractmethod
    def get_track(self):
        '''
        Returns file track number.
        '''
        raise NotImplementedError

    @abstractmethod
    def get_title(self):
        '''
        Returns file title.
        '''
        raise NotImplementedError

    @abstractmethod
    def get_album_artist(self):
        '''
        Returns file album artist.
        '''
        raise NotImplementedError

    @abstractmethod
    def get_year(self):
        '''
        Returns file year.
        '''
        raise NotImplementedError

    @abstractmethod
    def get_genre(self):
        '''
        Returns file genre.
        '''
        raise NotImplementedError