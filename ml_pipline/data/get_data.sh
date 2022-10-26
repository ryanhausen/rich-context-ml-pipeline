#!/bin/bash

# download kaggle data, you need permission to do this see:
# https://www.kaggle.com/c/coleridgeinitiative-show-us-the-data

# downloads coleridgeinitiative-show-us-the-data.zip to the cwdS
kaggle competitions download -c coleridgeinitiative-show-us-the-data

# extract data and build database
python extract_and_build_repository.py

