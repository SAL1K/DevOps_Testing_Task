import requests
import shutil

FILE_URL = "https://example.com/largefile.bin"
LOCAL_FILE_PATH = "large_file.bin"
UPLOAD_URL = "https://example.com/upload"


def download_file(url, local_path, chunk_size=1024 * 1024):
    with requests.get(url, stream=True) as response:
        response.raise_for_status()
        with open(local_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=chunk_size):
                if chunk:
                    file.write(chunk)
    print(f"Файл скачан: {local_path}")


def upload_file(local_path, upload_url, chunk_size=1024 * 1024):
    """Загружает файл по частям."""
    with open(local_path, "rb") as file:
        with requests.post(upload_url, data=file, headers={"Content-Type": "application/octet-stream"}) as response:
            response.raise_for_status()
            print(f"Файл загружен: {response.status_code}")


if name == "main":
    download_file(FILE_URL, LOCAL_FILE_PATH)

    upload_file(LOCAL_FILE_PATH, UPLOAD_URL)