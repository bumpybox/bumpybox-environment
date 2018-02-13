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


def get_applications_path():

    applications_path = os.path.join(os.path.dirname(__file__), "applications")
    if not os.path.exists(applications_path):
        os.makedirs(applications_path)

    return applications_path


def install_djv():

    applications_path = get_applications_path()
    application_path = os.path.join(applications_path, "djv-1.1.0-Windows-64")

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


def install_alshaders():

    applications_path = get_applications_path()
    application_path = os.path.join(
        applications_path, "alShaders-win-2.0.0b2-ai5.0.1.0"
    )

    path = os.path.join(applications_path, "alshaders.zip")

    if not os.path.exists(application_path) and not os.path.exists(path):
        print "Installing AlShaders..."
        url = "https://github.com/anderslanglands/alShaders2/releases/"
        url += "download/2.0.0-beta2/alShaders-win-2.0.0b2-ai5.0.1.0.zip"
        download_file(url, path)

        zip_ref = zipfile.ZipFile(path, "r")
        zip_ref.extractall(application_path)
        zip_ref.close()

        os.remove(path)


if __name__ == "__main__":
    install_djv()
    install_alshaders()
