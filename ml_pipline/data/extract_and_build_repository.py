from base64 import encode
import csv
from itertools import count
import json
import os
import sqlite3
from zipfile import ZipFile

from tqdm import tqdm

kaggle_dir = "./ml_pipline/data/kaggle"
kaggle_download = "./ml_pipline/data/coleridgeinitiative-show-us-the-data.zip"
database_location = "./ml_pipline/data/dataset.db"

def extract():
    print("Extracting kaggle data")
    assert os.path.exists(kaggle_download), "Please download kaggle data, see /data/README.md"

    with ZipFile(kaggle_download, "r") as zip:
        zip.extractall(kaggle_dir)

def build_repository():
    print("Making db")
    if not os.path.exists(database_location):
        connection = sqlite3.connect(database_location)
        cursor = connection.cursor()

        # make tables
        cursor.execute("CREATE TABLE documents(id TEXT, title TEXT, text BLOB)")
        cursor.execute("CREATE TABLE labels(id INT, dataset_title TEXT, dataset_label TEXT, document_id TEXT, parent_id INT)")

        connection.close()


def load_repository():
    print("Loading db")
    assert os.path.exists(database_location), "Please make database, execute build_respository()"
    assert os.path.exists(kaggle_dir), "Please download kaggle data, execute extract()"

    connection = sqlite3.connect(database_location)
    cursor = connection.cursor()

    if cursor.execute("SELECT * FROM labels").fetchone():
        print("Database loaded already")
    else:
        _id = count()
        labels = []
        documents = []
        seen_doc =[]
        with open(os.path.join(kaggle_dir, "train.csv"), "r") as f:
            lines = csv.DictReader(f)
            for l in tqdm(lines, desc="Reading csv lines"):
                document_id = l["Id"]
                labels.append((next(_id), l["dataset_title"], l["dataset_label"], document_id, -1))

                with open(f"./data/kaggle/train/{document_id}.json", "r") as f:
                    text = json.dumps(json.load(f)).encode()

                if document_id not in seen_doc:
                    documents.append((
                        document_id,
                        l["pub_title"],
                        text
                    ))
                    seen_doc.append(document_id)


        cursor.executemany("INSERT INTO documents VALUES(?, ?, ?)", documents)
        cursor.executemany("INSERT INTO labels VALUES(?, ?, ?, ?, ?)", labels)
        connection.commit()

    connection.close()

def main():
    extract()
    build_repository()
    load_repository()



if __name__=="__main__":
    main()