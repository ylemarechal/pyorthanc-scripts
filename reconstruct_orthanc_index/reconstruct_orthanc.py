import os

import dotenv
from alive_progress import alive_bar
from httpx import HTTPError
from pyorthanc import find_series, Orthanc

dotenv.load_dotenv('.env')

orthanc_url = os.getenv('ORTHANC_URL')
orthanc_username = os.getenv('ORTHANC_USERNAME')
orthanc_password = os.getenv('ORTHANC_PASSWORD')

client = Orthanc(
    orthanc_url,
    username=orthanc_username,
    password=orthanc_password,
    timeout=240
)

series_count = client.get_statistics()['CountSeries']
print(f'Reconstructing {series_count} series...')

all_series = find_series(
    client=client
)

with alive_bar(len(all_series)) as bar:
    for series in all_series:
        bar()
        try:
            client.post_series_id_reconstruct(series.id_)
        except HTTPError:
            print(f'Error in reconstructing series {series.id_}...')
