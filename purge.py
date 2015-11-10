import shutil
import os

def purge():
    folder = 'images'
    shutil.rmtree(folder)
    os.makedirs(folder)
