import os
__version__ = "1.0.0"

from os import write

if not os.path.exists(os.path.path.join(os.getcwd(), '.env')):
    with open(".env", "a") as config:
        config.writelines(['MUSIC_LIBRARY_PATH=\'\'','MUSIC_STAGING_PATH=\'\'', 'ZIP_FILE_STAGING_PATH=\'\''])
