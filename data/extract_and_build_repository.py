import os
from zipfile import ZipFile

def download_and_extract():
    kaggle_dir = "./kaggle"
    kaggle_download = "coleridgeinitiative-show-us-the-data.zip"

    assert os.path.exists(kaggle_download), "Please download kaggle data"

    with ZipFile("coleridgeinitiative-show-us-the-data.zip", "r") as zip:
        zip.extractall("kaggle")

def build_repository():
    pass

def load_repository():
    pass

def main():
    download_and_extract()
    build_repository()
    load_repository()



if __name__=="__main__":
    main()