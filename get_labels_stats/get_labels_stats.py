import os

import dotenv
import pyorthanc

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

labels = client.get_tools_labels()
for label in labels:
    data = {
        "Labels": [label],
        "Level": "Study",
        "Query": {}
    }
    count = client.post_tools_count_resources(json=data)
    print(f'Found {count['Count']} studies with label {label}')
