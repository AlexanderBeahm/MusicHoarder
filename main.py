#main.py
import musichoarder.fileinfo.fileinfofactory as FileInfoFactory
import musichoarder.filetransfer.filetransfer as FileTransfer
from file_traversal import FileTraversal
import os

if not os.path.exists(os.path.join(os.getcwd(), '.env')):
    with open(".env", "a") as config:
        config.writelines(['MUSIC_LIBRARY_PATH=\'\'','\nMUSIC_STAGING_PATH=\'\'', '\nZIP_FILE_STAGING_PATH=\'\''])

music_library_path = os.getenv('MUSIC_LIBRARY_PATH')
complete_path = os.getenv('MUSIC_STAGING_PATH')
zipped_staging_path = os.getenv('ZIP_FILE_STAGING_PATH')

if (music_library_path is None or music_library_path == '' 
    or complete_path is None or complete_path == '' 
    or zipped_staging_path is None or zipped_staging_path == ''):
    print("Please set your .env variables for music directory and staging paths.")
    quit("Config issue, please fill out required values in .env file.")

if music_library_path == complete_path or music_library_path == zipped_staging_path or complete_path == zipped_staging_path:
    print("Please ensure each path is unique.")
    quit("Config issue, please make each path unique in .env file.")

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
        print("hi I'm an audio file {0}\n artist is {1}\n album is {2}\n title is {3}\n track-number is {4}\n year is {5}\n.".format(filename, artist, album, title, track, year))
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
    if(foldername != music_library_path and foldername != zipped_staging_path and foldername != complete_path):
        FileTransfer.delete_directory(foldername)


if __name__ == '__main__':
    '''
    Main entry point
    '''
    #Run the CLI from here
    print('Hello, world! Time to open the plunder chest.')

    traverser = FileTraversal(soulseek_folder_config, soulseek_file_config)
    if complete_path is not None and os.path.exists(complete_path):
        traverser.recurse(complete_path)
    if zipped_staging_path is not None and os.path.exists(zipped_staging_path):
        traverser.recurse(zipped_staging_path)

    #Somehow run import on MusicBee OR just have it auto-enabled
    #Assuming library data is correct...
        #Somehow run import on PLEX
    input("Press enter to exit...")