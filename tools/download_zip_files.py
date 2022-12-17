import argparse
import io
import logging
import shutil
from pathlib import Path

import pandas as pd
from download_file_list import get_credential
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

MIMETYPE_ZIP = "application/zip"


def download_zip(drive, item, zip_dir):
    try:
        log.info("download {path} ({id}).".format(**item))

        # pylint: disable=maybe-no-member
        request = drive.files().get_media(fileId=item["id"])
        file = io.BytesIO()
        downloader = MediaIoBaseDownload(file, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            log.debug(f'Download {int(status.progress() * 100)} %')
            # if args.debug:
            #     break

        path = Path(zip_dir, item["path"].replace("/", "__"))
        log.info(f"write {path}")
        if path.exists():
            path.unlink()
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "wb") as f:
            f.write(file.getbuffer())

    except HttpError as error:
        print(F'An error occurred: {error}')
        return None

    return path


def unzip_downloaded_file(rootdir, item, path_zip_file):

    output_dir = Path(rootdir, item["path"].replace(".zip", ""))
    output_dir.mkdir(parents=True, exist_ok=True)
    if output_dir.exists():
        shutil.rmtree(output_dir.parent)

    try:
        log.debug(f"unzip to {output_dir}")
        shutil.unpack_archive(path_zip_file, output_dir)
    except Exception as e:
        log.error(f"Failed to unzip {path_zip_file}")
        log.error(e)
        return False

    return True


def main(args):
    df = pd.read_csv(args.input)
    df_zip = df[df["mimeType"] == MIMETYPE_ZIP].reset_index(drop=True)
    log.info(f"{len(df_zip)} zip files are found.")
    if args.debug:
        df_zip = df_zip.head(2)
    print(df_zip.head())

    # Authentication
    drive = None
    creds = None
    creds = get_credential()
    if creds and creds.valid:
        drive = build('drive', 'v3', credentials=creds)
    if not drive:
        print('Drive auth failed.')

    # Download
    zip_dir = Path(args.output, "zip", "google-drive")
    for _, item in df_zip.iterrows():
        path_zip_file = download_zip(drive, item, zip_dir)
        if path_zip_file is None:
            continue

        _ = unzip_downloaded_file(args.output, item, path_zip_file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--input",
        default="gdrive_file_index.csv",
        help="path to the file index CSV.")

    parser.add_argument(
        "-o",
        "--output",
        default="./data/openpack",
        help="dataset root directory.")
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()

    main(args)
