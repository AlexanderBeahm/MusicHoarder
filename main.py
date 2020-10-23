#main.py
import musichoarder.fileinfo.fileinfofactory as FileInfoFactory
import musichoarder.filetransfer.filetransfer as FileTransfer
from file_traversal import FileTraversal

'''
import click

For later when I implement CLI
'''

music_library_path = 'E:\\Music\\MusicLibrary'
zipped_staging_path = 'E:\\Music\\ToBeAdded\\unzipped'

def soulseek_file_config(filename):
    '''
    Soulseek file configuration test.
    '''
    print("hi I'm a file:\n\t{filename}".format(filename=filename))
    if "__MACOSX" in filename:
        return
    file_info = FileInfoFactory.construct_file_info(filename)
    if file_info is not None and file_info.is_audio_file():
        artist = file_info.get_artist()
        album = file_info.get_album()
        title = file_info.get_title()
        track = file_info.get_track()
        year = file_info.get_year()
        print("hi I'm an audio file {0}\n artist is {1}\n album is {2}\n title is {3}\n track-number is {4}\n.".format(filename, artist, album, title, track))
        print("this is the assembled file path, {0}".format(FileTransfer.__assemble_file_path(file_info, music_library_path)))
        FileTransfer.move_file(file_info, music_library_path)
    elif file_info.get_file_extension() == '.zip' or file_info.get_file_extension() == '.rar' or file_info.get_file_extension() == '.7z':
        FileTransfer.unzip_file(file_info, zipped_staging_path)
        FileTransfer.delete_file(file_info.get_filename())
    elif file_info is not None:
        FileTransfer.delete_file(file_info.get_filename())


def soulseek_folder_config(foldername):
    '''
    Soulseek folder configuration test.
    '''
    print("hello we're a folder:\n\t{foldername}".format(foldername=foldername))
    if(foldername != music_library_path and foldername != zipped_staging_path):
        FileTransfer.delete_directory(foldername)


if __name__ == '__main__':
    '''
    Main entry point
    '''
    #Run the CLI from here
    print('Hello, world')

    musicpath = 'E:\\Music\\ToBeAdded\\complete'
    zipped_path = 'E:\\Music\\ToBeAdded\\unzipped'

    traverser = FileTraversal(soulseek_folder_config, soulseek_file_config)
    traverser.recurse(musicpath)
    traverser.recurse(zipped_path)

    #Somehow run import on MusicBee OR just have it auto-enabled
    #Assuming library data is correct...
        #Somehow run import on PLEX