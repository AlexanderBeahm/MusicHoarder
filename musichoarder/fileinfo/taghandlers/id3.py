import mutagen
import os
from musichoarder.fileinfo.taghandlers.fileinfo import FileInfo

# https://help.mp3tag.de/main_tags.html - Site that displays all ID3 tag keys

class ID3(FileInfo):
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
        artist = self.file.tags.get('TPE1')
        if artist is None:
            return None
        return self.file.tags.get('TPE1').text[0]

    def get_album(self):
        artist = self.file.tags.get('TALB')
        if artist is None:
            return None
        return self.file.tags.get('TALB').text[0]

    def get_track(self):
        artist = self.file.tags.get('TRCK')
        if artist is None:
            return None
        return self.file.tags.get('TRCK').text[0]

    def get_title(self):
        artist = self.file.tags.get('TIT2')
        if artist is None:
            return None
        return self.file.tags.get('TIT2').text[0]

    def get_album_artist(self):
        artist = self.file.tags.get('TPE2')
        if artist is None:
            return None
        return self.file.tags.get('TPE2').text[0]

    def get_year(self):
        year = self.file.tags.get('TYER')
        if year is None:
            return None
        return self.file.tags.get('TYER').text[0]

    def get_genre(self):
        genre = self.file.tags.get('TCON')
        if genre is None:
            return None
        return self.file.tags.get('TCON').text[0]
