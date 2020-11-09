import organizeit
import os

FOLDERS_NAME = ['Images', 'Music', 'Videos', 'Applications', 'Documents', 'Others']
path = os.path.expanduser('E:\\Bedant Site\\')

organizeit.createFolders(FOLDERS_NAME, path)
organizeit.insertFiles(path)
