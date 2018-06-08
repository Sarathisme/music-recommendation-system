import os
import urllib.request
from zipfile import ZipFile

HOME_DIRECTORY = os.path.join('datasets','raw')
ROOT_URL = 'https://os.unil.cloud.switch.ch/fma/fma_metadata.zip'

if not os.path.isdir(HOME_DIRECTORY):
    os.makedirs(HOME_DIRECTORY)
zip_path = os.path.join(HOME_DIRECTORY, 'data.zip')
urllib.request.urlretrieve(ROOT_URL, zip_path)

with ZipFile(zip_path, 'r') as zip:
    zip.extractall(HOME_DIRECTORY)
    print("Done!")