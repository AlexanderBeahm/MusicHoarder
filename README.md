# MusicHoarder
Future: A multi-functional CLI tool for music hoarding/ratings needs.

Present: A runnable Python script that will auto-organize music files (included archived files) into your music library.

---

## Prerequisites

### RECOMMENDED: Create a virtual environment.

Run command `pip install -r requirements.txt`

Create a `.env` file in the root project directory. This can be generated for you with the required keys by running the program for the first time.

For example:
```
MUSIC_LIBRARY_PATH='E:\\Music\\MusicLibrary'
MUSIC_STAGING_PATH='E:\\Music\\ToBeAdded\\complete'
ZIP_FILE_STAGING_PATH='E:\\Music\\ToBeAdded\\unzipped'
```

**MUSIC_LIBRARY_PATH** is the folder where your music library exists. MusicHoarder will organize music files into this directory.

**MUSIC_STAGING_PATH** is the folder where your unprocessed downloads and zip files are contained. MusicHoarder targets this folder in it's recursive run to process files.

**ZIP_FILE_STAGING_PATH** is the folder where your zip files will be initially extracted to before being processed in a secondary recursive run. I do realize this is a big O(2n) no no siuation but it's not like we are processing huge amounts of data here.

These folder at this point in time need to be unique values.
---

## How To Run

Run `python main.py`

## Known Restrictions

1. Only one format is currently supported for organization, that being "{Album Artist}/{Album}({Year})/{Track}_{Title}.{EXT}"
2. There is no I/O way to supply or change environment values, these will need to be manually configured in your local `.env` file.
3. Only .zip archives are supported at the moment.
