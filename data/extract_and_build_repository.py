import os
import json
import sqlite3
from zipfile import ZipFile

def download_and_extract() -> None:
    kaggle_dir = "./data/kaggle"
    kaggle_download = "./data/coleridgeinitiative-show-us-the-data.zip"

    assert os.path.exists(kaggle_download), "Please download kaggle data"

    with ZipFile(kaggle_download, "r") as zip:
        zip.extractall(kaggle_dir)

def build_repository():
    con = sqlite3.connect("./data/kaggle_data.db")
    
    cur  = con.cursor()


def load_repository():
    pass

def main():
    download_and_extract()
    build_repository()
    load_repository()



if __name__=="__main__":
    main()