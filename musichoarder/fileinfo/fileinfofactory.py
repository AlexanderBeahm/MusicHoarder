from musichoarder.fileinfo.taghandlers.m4a import M4A
import os
from musichoarder.fileinfo.taghandlers.fileinfo import FileInfo
from musichoarder.fileinfo.taghandlers.lossless import Lossless
from musichoarder.fileinfo.taghandlers.id3 import ID3
__supported_audio_filetypes = ['.aac', '.alac', '.aif', '.aifc', '.aiff', '.dsf', '.ape', '.flac', '.mka', '.mkv', '.mp3', '.mp4', '.m4a', '.m4b', '.mpc', '.ogg', '.opus', '.ofr', '.ofs', '.spx', '.tak', '.tta', '.wav', '.wv', '.wma']

def construct_file_info(filepath):
    '''
    Constructs file information object from filepath, choosing implementation based on file extension.
    '''
    name, ext = os.path.splitext(filepath)
    if ext in __supported_audio_filetypes :
        if(ext == '.mp3'):
            return ID3(filepath)
        if(ext == '.m4a'):
            return M4A(filepath)
        if(ext == '.flac'):
            return Lossless(filepath)
    return FileInfo(filepath)
