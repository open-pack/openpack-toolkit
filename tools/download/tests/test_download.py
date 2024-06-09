from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from tools.download.download import (
    download_and_extract_single_user_from_zenodo,
    download_file_with_progress_bar,
    extract_zip,
)


@patch("requests.get")
def test_download_file(mock_get: MagicMock, tmp_path: Path):
    # Dummy address
    url = "http://example.com/fake.zip"
    download_path = Path(tmp_path, "data", "zip", "downloaded_file.zip")
    # Mock for requests
    mock_response = MagicMock()
    mock_response.iter_content = lambda chunk_size: [b"a" * 1024] * 5
    mock_response.headers = {"content-length": f"{1024 * 5}"}
    mock_get.return_value = mock_response

    download_file_with_progress_bar(url, download_path)

    assert download_path.exists()


@patch("zipfile.ZipFile")
def test_extract_zip(mock_zipfile: MagicMock):
    file_path = "downloaded_file.zip"
    extract_path = "extracted"
    # Mock for zipfile.ZipFile
    mock_zip = MagicMock()
    mock_zipfile.return_value.__enter__.return_value = mock_zip

    result = extract_zip(file_path, extract_path)

    assert result == extract_path
    mock_zip.extractall.assert_called_once_with(extract_path)


@patch("tools.download.download.download_file_with_progress_bar")
@patch("tools.download.download.extract_zip")
def test_smoke_download_and_extract_single_user_from_zenodo(
    mock_download: MagicMock, mock_extract: MagicMock
):
    openpack_dir = Path("openpack")
    version = "v1.0.0"
    user_id = "U0101"

    download_and_extract_single_user_from_zenodo(openpack_dir, version, user_id)
