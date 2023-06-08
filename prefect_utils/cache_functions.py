import os
from prefect.utilities.hashing import file_hash
import hashlib
from pathlib import Path
from prefect.results import PersistedResultBlob


def cache_constant(task_context, task_parameters):
    return 'dummy'

def expand_home_path(path):
    if path.startswith("~"):
        path = os.path.expanduser(path)
    return path

def cache_file_based_fn(task_context, task_parameters):
    """
    Local file based cache function to be used in prefect @task and @ flow decorators in the cache_key_fn attribute.

    IMPORTANT: It requires the @task or @flow to include a result_file_path attribute. This is the path (including filename
    and extension of the resulting file where the @task or @flow would be saving the result python object.

    The function checks whether the result file exists and if it does the @task or @flow will not run but 
    grab the result object from the file and return it instead.

    CAREFUL: It works by hashing the path to the file. So if the file is moved manually it will not be CACHED and the
    @task or @flow reruned and the file overriden.

Args:
    task_context, task_parameters (requires The @task or @flow to include a result_file_path attribute)

Returns:
    str:file hash
    """

    # Check if the result file exists
    try:
        if os.path.exists(task_parameters["result_file_path"]):
            path_to_hash = expand_home_path(task_parameters["result_file_path"])
            return hashlib.md5(path_to_hash.encode('utf8')).hexdigest()
    except:
        return None

def cache_file_content_based_fn(task_context, task_parameters):
    """
    Local file and content based cache function to be used in prefect @task and @ flow decorators in the cache_key_fn attribute.

    IMPORTANT: It requires the @task or @flow to include a result_file_path attribute. This is the path (including filename
    and extension of the resulting file where the @task or @flow would be saving the result python object.

    The function checks whether the result file exists and contains the same content as in the previous run. 
    If both conditions are met the @task or @flow will not run but 
    grab the result object from the file and return it instead.

Args:
    task_context, task_parameters (requires The @task or @flow to include a result_file_path attribute)

Returns:
    str:file hash
    """

    # Check if the result file exists
    if os.path.exists(task_parameters["result_file_path"]):
        cache_key = hashlib.md5(
            PersistedResultBlob.parse_raw(Path(task_parameters['result_file_path']).read_bytes()).data).hexdigest()
        return cache_key
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
