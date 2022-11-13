from typing import Dict, List, Tuple

# import gin

Document = Dict[str, str]
Label = str
DataSample = Tuple[Document, Label]

def get_by_ids(source, ids) -> List[DataSample]:
    return source.get_by_ids(ids)

def get_ids(source) -> List[str]:
    return source.get_ids()

def get_training_set(source) -> List[DataSample]:
    return source.get_training_set()

def get_test_set(source) -> List[DataSample]:
    return source.get_test_set()

def update(source, samples:List[DataSample]) -> None:
    return source.update(samples)
