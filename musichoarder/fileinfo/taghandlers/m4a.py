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
            return ''
        return artist.text[0]

    def get_album(self):
        album = self.file.tags.get('\xa9alb')
        if album is None:
            return ''
        return album.text[0]

    def get_track(self):
        track = self.file.tags.get('sonm')
        if track is None:
            return ''
        return track.text[0]

    def get_title(self):
        title = self.file.tags.get('\xa9nam')
        if title is None:
            return ''
        return title.text[0]

    def get_album_artist(self):
        artist = self.file.tags.get('aART')
        if artist is None:
            return ''
        return artist.text[0]

    def get_year(self):
        year = self.file.tags.get('\xa9day')
        if year is None:
            return ''
        return year.text[0]

    def get_genre(self):
        genre = self.file.tags.get('\xa9gen')
        if genre is None:
            return ''
        return genre.text[0]
