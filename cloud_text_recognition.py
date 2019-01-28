from base64 import b64encode

import googleapiclient.discovery
from oauth2client.client import GoogleCredentials

IMAGE_FILE = 'text.png'
CREDENTIALS_FILE = 'credential.json'

credentials = GoogleCredentials.from_stream(CREDENTIALS_FILE)
service = googleapiclient.discovery.build('vision', 'v1', credentials=credentials)

with open(IMAGE_FILE, mode='rb') as f:
    image_data = f.read()
    encoded_image_data = b64encode(image_data).decode('UTF-8')

batch_request =[{
    'image': {
        'content': encoded_image_data
    },
    'features': [
        {
            'type':'TEXT_DETECTION'
        }
    ]
}]
request = service.images().annotate(body={'requests':batch_request})
response = request.execute()

if 'error' in response:
    raise RuntimeError(response['error'])

extracted_texts = response['responses'][0]['textAnnotations']

extracted_texts = extracted_texts[0]
print(extracted_texts['description'])

print(extracted_texts['boundingPoly'])
