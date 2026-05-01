# Add New Modalities to Orthanc

This script automates the process of adding new DICOM modalities to an Orthanc server. It reads modality configurations from a YAML file and adds them to Orthanc if they don't already exist.

## Prerequisites

- Python 3.x
- Dependencies listed in `requirements.txt`
- Orthanc server running on `http://localhost:8042` with `DicomModalitiesInDatabase` enabled

## Installation

1. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

### Environment Variables

Create a `.env` file in the same directory as the script with the following variables:

```env
ORTHANC_URL=http://localhost:8042
ORTHANC_USERNAME=orthanc
ORTHANC_PASSWORD=orthanc
```

### Modalities Configuration

Define the modalities you want to add in `modalities.yml`. The file should follow this format:

```yaml
MODALITY_NAME:
  AET: YOUR_AET
  Host: 192.168.1.1
  Port: 4242
```

Example `modalities.yml`:
```yaml
DICOM_2:
  AET: DICOM_2
  Host: 192.168.1.2
  Port: 4243
```

## Usage

Run the script using Python:

```bash
python add_new_modalities.py
```

The script will:
1. Connect to the Orthanc server using the provided credentials.
2. Retrieve the list of existing modalities.
3. Compare them with the modalities defined in `modalities.yml`.
4. Add any missing modalities to the Orthanc server.
