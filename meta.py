import os
from mutagen.easyid3 import EasyID3

files = os.listdir()
files.remove('.git')
files.remove('meta.py')
files.remove('music.py')
files.remove('README.md')

album = input('Album? ')
year = input('Year? ')

for file in files:
    name_clean = file.partition(' ')[2].replace('.mp3', '')
    song = EasyID3(file)
    song['tracknumber'] = file.partition(' ')[0]
    song['album'] = album
    song['date'] = year
    song['artist'] = name_clean.partition(' - ')[0]
    song['albumartist'] = name_clean.partition(' - ')[0]
    song['title'] = name_clean.partition(' - ')[2]
    song.save()