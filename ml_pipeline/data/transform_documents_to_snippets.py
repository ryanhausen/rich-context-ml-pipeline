from typing import Iterable, List
from dataclasses import dataclass
from ml_pipeline.data.repository import DataSample

@dataclass
class TrainingSample:
    contains_dataset: float
    mask_labels: List[float]
    maked_sample: str
    unmasked_sample:str


def split_document_into_snippets(
    document:DataSample,
    max_snippet_length:int,
    beyond_sentence:bool,
) -> List[TrainingSample]:
    document, label = document

    text_only = " ".join(list(map(lambda x: x["text"], document)))

    snippets = []



def document_generator(source) -> Iterable[DataSample]:
    document_ids = source.get_ids()

    for document_id in document_ids:
        data_sample = source.get_by_ids([document_id])[0]
        yield data_sample




if __name__ == '__main__':
    pass