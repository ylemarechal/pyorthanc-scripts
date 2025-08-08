import os

import dotenv
import pyorthanc
from pyorthanc import find_studies
from httpx import HTTPError

dotenv.load_dotenv('.env')

orthanc_url = os.getenv('ORTHANC_URL')
orthanc_username = os.getenv('ORTHANC_USERNAME')
orthanc_password = os.getenv('ORTHANC_PASSWORD')

client = pyorthanc.Orthanc(
    orthanc_url,
    username=orthanc_username,
    password=orthanc_password,
    timeout=240
)

studies = find_studies(
    client=client,
    labels=os.getenv('LABELS')
)

print(f'Found {len(studies)} studies with labels {os.getenv("LABELS")}')

# Exit here to prevent unwanted deletion...
exit(0)

try:
    for study in studies:
        print(f'Deleting study {study.id_}...')
        client.delete_studies_id(study.id_)
except HTTPError:
    print(f'Error in deleting study {study.id_}...')
