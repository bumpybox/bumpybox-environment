import os

import requests
import zipfile


def download_file(url, path):
    r = requests.get(url, stream=True)
    with open(path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    if os.path.exists(path):
        return True
    else:
        return False


def install_djv():

    root = os.path.dirname(__file__)
    applications_path = os.path.join(root, "applications")
    application_path = os.path.join(applications_path, "djv-1.1.0-Windows-64")

    if not os.path.exists(applications_path):
        os.makedirs(applications_path)

    path = os.path.join(applications_path, "djv.zip")

    if not os.path.exists(application_path) and not os.path.exists(path):
        print "Installing DJV..."
        url = "https://downloads.sourceforge.net/project/djv/djv-stable/1.1.0/"
        url += "djv-1.1.0-Windows-64.zip"
        download_file(url, path)

        zip_ref = zipfile.ZipFile(path, "r")
        zip_ref.extractall(applications_path)
        zip_ref.close()

        os.remove(path)


if __name__ == "__main__":
    install_djv()
