import os
from prefect.utilities.hashing import file_hash
import hashlib
from pathlib import Path
from prefect.results import PersistedResultBlob


def cache_constant(task_context, task_parameters):
    return 'dummy'


def cache_file_based_fn_OG(task_context, task_parameters):
    """
    Local file based cache function to be used in prefect @task and @ flow decorators in the cache_key_fn attribute.

    IMPORTANT: It requires the @task or @flow to include a result_file_path attribute. This is the path (including filename
    and extension of the resulting file where the @task or @flow would be saving the result python object.

    The function checks whether the result file exists and if it does the @task or @flow will not run but 
    grab the result object from the file and return it instead.

Args:
    task_context, task_parameters (requires The @task or @flow to include a result_file_path attribute)

Returns:
    str:file hash
    """

    # Check if the result file exists
    if os.path.exists(task_parameters["result_file_path"]):
        # Compute the hash of the result file
        hash_md5 = hashlib.md5()
        with open(task_parameters["result_file_path"], 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
            file_hash = hash_md5.hexdigest()
        # Return the hash as the cache key
        return file_hash
    else:
        return None



def cache_file_and_input_based_fn(task_context, task_parameters):
    """
    Input and local file based cache function to be used in prefect @task and @ flow decorators in the cache_key_fn attribute.

    IMPORTANT: It requires the @task or @flow to include a result_file_path attribute. This is the path (including filename
    and extension of the resulting file where the @task or @flow would be saving the result python object.

    The function checks whether the result file exists and if the input arguments are the same as in the previous run. 
    If both conditions are satisfied, the @task or @flow will not run but 
    grab the result object from the file and return it instead.

Args:
    task_context, task_parameters (requires The @task or @flow to include a result_file_path attribute)

Returns:
    str:file hash
    """

    # TODO
