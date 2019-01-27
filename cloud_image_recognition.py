from base64 import b64encode

import googleapiclient.discovery
from oauth2client.client import GoogleCredentials

IMAGE_FILE = 'road_sign.jpg'
CREDENTIALS_FILE = 'credential.json'

credentials = GoogleCredentials.from_stream(CREDENTIALS_FILE)
service = googleapiclient.discovery.build('vison', 'v1', credentials=credentials)

with open(IMAGE_FILE, mode='rb') as f:
    image_data = f.read()
    encoded_image_data = b64encode(image_data).decode('UTF-8')
