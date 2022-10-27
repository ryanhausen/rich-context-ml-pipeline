#!/bin/bash

# download kaggle data, you need permission to do this see:
# https://www.kaggle.com/c/coleridgeinitiative-show-us-the-data

mkdir -p ./ml_pipeline/data/kaggle

# downloads coleridgeinitiative-show-us-the-data.zip to the cwdS
kaggle competitions download -c coleridgeinitiative-show-us-the-data -p ./ml_pipeline/data

# extract data and build database
python ./ml_pipeline/data/extract_and_build_repository.py

