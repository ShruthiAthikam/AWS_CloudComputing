import boto3
from image_helpers import get_image
from pprint import pprint

client = boto3.client('rekognition')

imgurl = 'http://www.idothat.us/images/idothat-img/features/pool-patio-lanai/ft-pool-patio-lanai-2.jpg'

# download the image from the web
imgbytes = get_image(imgurl)

# pprint(client.detect_labels(Image={'Bytes': imgbytes}))
rekognition_response = client.detect_labels(Image={'Bytes': imgbytes},
                                            MinConfidence=1)

# pprint(rekognition_response['Labels'])
pprint(rekognition_response['Labels'])

# for label in rekognition_response['Labels']:
#     print(f"{label['Name']} {label['Confidence']:.3f}")
#     pprint(label['Instances'])
#     print()
