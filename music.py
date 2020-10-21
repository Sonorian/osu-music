import os
import zipfile

files = os.listdir()
files.remove('music.py')
files.remove('.git')
strange = input('Are there underscores instead of spaces in filenames?(y/n) ')

for file in files:
    with zipfile.ZipFile(file, 'r') as osz:
            osz.extract('audio.mp3')
    msg = file.replace('.osz',' ')
    pos = input(msg)
    if len(pos) == 1:
        pos = '0' + pos  # makes it easy
    os.rename('audio.mp3', pos+' '+file.replace('osz','mp3'))
    if strange == 'y':
        os.rename(file.replace('osz', 'mp3'), file.replace('osz','mp3').replace('_',' '))
    os.remove(file)