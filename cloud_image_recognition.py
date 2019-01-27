from base64 import b64encode

import googleapiclient.discovery
from oauth2client.client import GoogleCredentials

IMAGE_FILE = 'road_sign.jpg'
CREDENTIALS_FILE = 'credential.json'

credentials = GoogleCredentials.from_stream(CREDENTIALS_FILE)
