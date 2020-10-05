import mutagen
import os
from musichoarder.fileinfo.taghandlers.fileinfo import FileInfo

# Lists all MP4 tag dictionary keys
# https://mutagen.readthedocs.io/en/latest/api/mp4.html#mutagen.mp4.MP4Tags

class M4A(FileInfo):
    '''
    Reprsents any file information objects with an ID3 tag.
    '''

    def __init__(self, filename):
        super()
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
        artist = self.file.tags.get('\xa9ART')
        if artist is None:
            return None
        return self.file.tags.get('\xa9ART').text[0]

    def get_album(self):
        artist = self.file.tags.get('\xa9alb')
        if artist is None:
            return None
        return self.file.tags.get('\xa9alb').text[0]

    def get_track(self):
        artist = self.file.tags.get('sonm')
        if artist is None:
            return None
        return self.file.tags.get('sonm').text[0]

    def get_title(self):
        artist = self.file.tags.get('\xa9nam')
        if artist is None:
            return None
        return self.file.tags.get('\xa9nam').text[0]

    def get_album_artist(self):
        artist = self.file.tags.get('aART')
        if artist is None:
            return None
        return self.file.tags.get('aART').text[0]

    def get_year(self):
        year = self.file.tags.get('\xa9day')
        if year is None:
            return None
        return self.file.tags.get('\xa9day').text[0]

    def get_genre(self):
        genre = self.file.tags.get('\xa9gen')
        if genre is None:
            return None
        return self.file.tags.get('\xa9gen').text[0]
