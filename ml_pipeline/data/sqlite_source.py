import json
import sqlite3
from typing import List

import ml_pipeline.data.repository as repo


class SQLiteSource:

    SELECT_DOCUMENT_BY_DOCUMENT_ID = """
        SELECT id, title, text
        FROM documents WHERE id = ?
    """

    SELECT_LABELS_BY_DOCUMENT_ID = """
        SELECT dataset_label
        FROM labels WHERE document_id = ?
    """

    SELECT_DOCUMENT_IDS = """
        SELECT id
        FROM documents
    """


    def __init__(self, path:str) -> None:
        self.path = path

    def get_by_ids(self, ids:List[str]) -> List[repo.DataSample]:
        connection = sqlite3.connect(self.path)
        cursor = connection.cursor()

        samples = []

        for doc_id in ids:
            document = cursor.execute(
                SQLiteSource.SELECT_DOCUMENT_BY_DOCUMENT_ID,
                [doc_id]
            ).fetchone()

            labels = cursor.execute(
                SQLiteSource.SELECT_LABELS_BY_DOCUMENT_ID,
                [doc_id]
            ).fetchall()

            labels = [l[0] for l in labels]
            doc = json.loads(document[2].decode())
            doc.insert(0, {"section_title":"title", "text":document[1]})
            samples.append((doc, "|".join(labels)))

        connection.close()
        return samples

    def get_training_set() -> List[repo.DataSample]:
        raise NotImplementedError()

    def get_test_set() -> List[repo.DataSample]:
        raise NotImplementedError()

    def update(samples:List[repo.DataSample]) -> None:
        raise NotImplementedError()

    def get_ids(self) -> List[str]:
        connection = sqlite3.connect(self.path)
        cursor = connection.cursor()

        results =  cursor.execute(SQLiteSource.SELECT_DOCUMENT_IDS).fetchall()

        connection.close()

        return results


if __name__=="__main__":
    src = SQLiteSource("./ml_pipline/data/dataset.db")

    returns = src.get_by_ids(["2f392438-e215-4169-bebf-21ac4ff253e1"])

    print(returns)