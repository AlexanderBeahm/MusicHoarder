import mutagen
import os
from musichoarder.fileinfo.taghandlers.fileinfo import FileInfo

class Lossless(FileInfo):
    '''
    Represents a lossless file with no ID3 tags.
    '''
    def __init__(self, filename):
        if filename == '' or filename is None:
            raise FileNotFoundError
        self.filename = filename
        self.file = mutagen.File(filename)
        self.file_extension = os.path.splitext(filename)[1]

    def is_audio_file(self):
        return True
    
    def get_file_extension(self):
        return super().get_file_extension()

    def get_filename(self):
        return super().get_filename()

    def get_fileinfo(self):
        return super().get_fileinfo()

    def get_artist(self):
        return self.file.tags.get('ARTIST')[0]

    def get_album(self):
        return self.file.tags.get('ALBUM')[0]

    def get_track(self):
        return self.file.tags.get('TRACKNUMBER')[0]

    def get_title(self):
        return self.file.tags.get('TITLE')[0]

    def get_album_artist(self):
        return self.file.tags.get('ALBUMARTIST')[0]

    def get_year(self):
        return self.file.tags.get('DATE')[0]

    def get_genre(self):
        return self.file.tags.get('GENRE')[0]
