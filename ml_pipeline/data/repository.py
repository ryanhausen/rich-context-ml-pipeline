from typing import Dict, List, Tuple

# import gin

Document = Dict[str, str]
Label = str
DataSample = Tuple[Document, Label]

def get_by_ids(ids, source) -> List[DataSample]:
    pass

def get_ids(source) -> List[str]:
    pass

def get_training_set(source) -> List[DataSample]:
    pass

def get_test_set(source) -> List[DataSample]:
    pass

def update(source, samples:List[DataSample]) -> None:
    pass
