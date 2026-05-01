import os

import dotenv
import pyorthanc
import yaml

dotenv.load_dotenv('.env')

client = pyorthanc.Orthanc(
    os.environ['ORTHANC_URL'],
    username=os.environ['ORTHANC_USERNAME'],
    password=os.environ['ORTHANC_PASSWORD'],
    timeout=180
)

existing_modalities = client.get_modalities()

with open('modalities.yml', 'r') as f:
    modalities = yaml.safe_load(f)

for modality_id, modality_config in modalities.items():
    if modality_id not in existing_modalities:
        print(f"Adding modality {modality_id}")
        client.put_modalities_id(
            id_=modality_id,
            json=modality_config
        )
    else:
        print(f"Modality {modality_id} already exists")
