import pickle 
import os
import base64
from pathlib import Path
from prefect.results import PersistedResultBlob

def load_pickle(path_to_folder, file_name):
    path_to_file = os.path.join(path_to_folder,file_name)
    object = pickle.loads(
                base64.b64decode(
                PersistedResultBlob.parse_raw(
                    Path(path_to_file).read_bytes()
                ).data
                )
            )
    return object