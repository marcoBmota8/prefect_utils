import pickle 
import base64
from pathlib import Path
from prefect.results import PersistedResultBlob

def load_pickle(path_to_file):
    object = pickle.loads(
                base64.b64decode(
                PersistedResultBlob.parse_raw(
                    Path(path_to_file).read_bytes()
                ).data
                )
            )
    return object