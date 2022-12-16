# Tool

## Download Dataset from Google Drive

(1) Enable Drive API on Google Cloud console.

<https://console.cloud.google.com/flows/enableapi?apiid=drive.googleapis.com>

(2) Authorize credentials for a desktop application

1. 2-1: In the Google Cloud console, go to Menu menu > APIs & Services > Credentials (<https://console.cloud.google.com/apis/credentials>)
1. Click Create Credentials > OAuth client ID.
1. Click Application type > Desktop app.
1. In the Name field, type a name for the credential. This name is only shown in the Google Cloud console.
1. Click Create. The OAuth client created screen appears, showing your new Client ID and Client secret.
1. Click OK. The newly created credential appears under OAuth 2.0 Client IDs.
1. Save the downloaded JSON file as credentials.json, and move the file to your working directory.

(3) Install packages

```bash
cd openpack-toolkit
poetry install
```

(4) Download Zip Files

```bash
poetry run python download_zip_files.py
```

### Reference

- [Drive API Python quickstart](https://developers.google.com/drive/api/quickstart/python)
