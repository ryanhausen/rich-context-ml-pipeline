from typing import Iterable, List, Tuple
from dataclasses import dataclass

import spacy

from ml_pipeline.data.repository import DataSample

nlp = spacy.load("en_core_web_trf")

@dataclass
class TrainingSample:
    contains_dataset: float # snipet contains dataset 0<=x<=1
    snippet: str            # snippet of text
    token_labels: List[int] # 0 for no dataset, 1 for dataset
    document_text: str
    document_id: str


def split_document_into_snippets(
    document:DataSample,
    n_sentences_per_snippet:int,
) -> List[TrainingSample]:
    document, label = document

    text_only = " ".join(list(map(lambda x: x["text"], document)))

    processed = nlp(text_only)

    for i in range(0, len(processed.sents), n_sentences_per_snippet):
        snippet = processed.sents[i:i+n_sentences_per_snippet].text

    snippets = []


def string_is_acronym(string:str) -> bool:
    return all(map(lambda x: x.isupper(), string))



def label_in_snippet(snippet:str, processed_label:Tuple[str, str]) -> bool:
    # This is pretty much the goal of the whole project, so it's a bit tricky

    expansion, acronym = processed_label
    complete_label = expansion + " (" + acronym + ")"

    if complete_label in snippet:
        return True

    if expansion in snippet:
        return True

    if acronym in snippet:
        return True

    return False

def document_generator(source) -> Iterable[DataSample]:
    document_ids = source.get_ids()

    for document_id in document_ids:
        data_sample = source.get_by_ids([document_id])[0]
        yield data_sample





if __name__ == '__main__':
    pass