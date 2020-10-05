import os
import mutagen
import musichoarder.fileinfo.taghandlers.fileinfo
import zipfile

def move_file(fileinfo, target_directory):
    '''
    Moves and renames file to the target directory.
    '''
    filename = os.path.basename(fileinfo.filename)
    target_file_path = __assemble_file_path(fileinfo, target_directory)
    os.makedirs(os.path.dirname(target_file_path), exist_ok=True)
    os.rename(fileinfo.filename, target_file_path)

def unzip_file(fileinfo, target_directory):
    '''
    Unzips files to the target directory.
    '''
    with zipfile.ZipFile(fileinfo.filename, 'r') as zip_ref:
        zip_ref.extractall(os.path.join(target_directory, os.path.splitext(os.path.split(fileinfo.get_filename())[1])[0]))

def delete_directory(directory):
    '''
    Deletes directory
    '''
    os.removedirs(directory)

def delete_file(filename):
    '''
    Delete file
    '''
    if(os.path.exists(filename)):
        os.remove(filename)

def __assemble_file_path(fileinfo, target_directory):
    '''
    Assembles organized file path based on music file tag data.
    '''
    artist = fileinfo.get_album_artist()
    if artist == '' or artist == None :
        artist = fileinfo.get_artist()

    album = fileinfo.get_album()
    year = fileinfo.get_year()

    if year == '' or year == None :
        year = ''

    track = fileinfo.get_track()

    if track == '' or track == None :
        track = ''

    title = fileinfo.get_title()
    if title == '' or title == None :
        title =  os.path.split(os.path.split(fileinfo.get_filename())[1])[1]
    
    album = __replace_special_characters(album)
    artist = __replace_special_characters(artist)
    title = __replace_special_characters(title)
    year = __replace_special_characters(year)
    track = __extract_track_value(track)

    extension = fileinfo.get_file_extension()
    
    tagged_path = '{0}\\{1}({2})\\{3}_{4}{5}'.format(artist, album, year, track, title, extension)
    return os.path.join(target_directory, tagged_path)

def __replace_special_characters(value):
    '''
    Replace any special characters in string that will break file/folder conventions.
    '''
    value = value.replace('?', '')
    value = value.replace('/', '')
    value = value.replace('>', '')
    value = value.replace('\'', '')
    value = value.replace('<', '')
    value = value.replace(':', '')
    value = value.replace('|', '')
    value = value.replace('*', '')
    value = value.replace('"', '')
    value = value.replace("[", '')
    value = value.replace("]", '')
    return value

def __extract_track_value(value):
    '''
    Replace/extract the actual track number given a forward/backward slash in the track number.
    '''
    value = value.split('/')[0]
    value = __replace_special_characters(value)