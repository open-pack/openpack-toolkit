import argparse
import logging
import os.path

import pandas as pd
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]
# Google Drive - OpenPack Dataset (v0.3.0)
ROOTDIR_FILE_ID = "1gq295W0YLa2FhLEVppurmDZZN0cUemNh"


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


def get_children_list_by_id(drive, file_id):
    results = drive.files().list(
        corpora="user",
        q=f'"{file_id}" in parents',
        includeItemsFromAllDrives=True,
        pageSize=100,
        fields="files(id, name, mimeType, version, driveId)",
        supportsAllDrives=True,
    ).execute()
    items = results.get('files', [])
    items.sort(key=lambda d: d["name"])
    return items


def get_credential():
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return creds


def main(args):
    drive = None
    creds = None

    # Authentication
    creds = get_credential()
    if creds and creds.valid:
        drive = build('drive', 'v3', credentials=creds)
    if not drive:
        print('Drive auth failed.')

    # GET Root folder
    items = get_children_list_by_id(drive, ROOTDIR_FILE_ID)
    assert len(items) == 1
    rootdir = items[0]
    rootdir.update({"path": rootdir["name"]})

    # BFS Search to obtain folder list.
    folders, df = [rootdir], []
    cnt = 0
    while len(folders) > 0:
        cnt += 1
        folder = folders.pop(-1)
        log.debug("=== {path} ===".format(**folder))
        log.debug(f"queue size: {len(folder)}")
        items = get_children_list_by_id(drive, folder["id"])

        for i, item in enumerate(items):
            item["path"] = folder["path"] + "/" + item["name"]
            log.debug("- [{ind}] {name} ({mimeType})".format(ind=i, **item))
            df.append(item)

            if item["mimeType"] == "application/vnd.google-apps.folder":
                folders.append(item)

        if args.debug and (cnt > 10):
            break
    df = pd.DataFrame(df)

    # Write CSV
    cols = ["id", "path", "mimeType", "version", "driveId"]
    df[cols].to_csv(args.output, index=False)
    log.info("write csv to {fname}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-o",
        "--output",
        default="gdrive_file_index.csv",
        help="output filename.")
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()

    main(args)
