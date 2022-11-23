# Notebook refs
# model 1
# https://github.com/Coleridge-Initiative/rc-kaggle-models/blob/main/1st%20ZALO%20FTW/notebooks/get_candidate_labels.ipynb
# https://github.com/Coleridge-Initiative/rc-kaggle-models/blob/main/1st%20ZALO%20FTW/notebooks/preprocess.ipynb


import re
import spacy

def jaccard_similarity(str1:str, str2:str) -> float:
    """Calculate the Jaccard similarity between two strings.

    https://en.wikipedia.org/wiki/Jaccard_index

               |A ∩ B|        |A ∩ B|
    J(A, B) =  ------- = -------------------
               |A ∪ B|   |A| + |B| + |A ∩ B|

    Args:
        str1 (str): First string.
        str2 (str): Second string.

    Returns:
        float: Jaccard similarity between the two strings.
    """
    a = set(str1.lower().split())
    b = set(str2.lower().split())
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))


def coleridge_clean_label(label):
    """Label cleaning function given by competition organizers."""
    return re.sub('[^A-Za-z0-9]+', ' ', str(label).lower())



def clean_text(string: str, lower=True) -> str:
    """Remove special characters from a string and optionally lower it.

    Any character that is not one of:

    - a-z
    - A-Z
    - 0-9
    - space
    - comma
    - !, ? ', `, \", \., ()

    are replaced with a space.
    """

    return re.sub(
        r"[^A-Za-z0-9(),!?\'\`\.\"\s]",
        " ",
        string.lower() if lower else string
    )


def contains_special_character(string: str) -> bool:
    """Check if a string contains any special characters."""

    return re.search(
        r"[^A-Za-z0-9(),!?\'\`\.\"\s]",
        string
    ) is not None


