import os
import hashlib
def cache_file_based_fn(task_context,task_parameters):
    """
    Local file based cache function to be used in prefect @task and @ flow decorators in the cache_key_fn attribute.

    IMPORTANT: It requires the @task or @flow to include a result_file_path attribute. This is the path (including filename
    and extension of the resulting file where the @task or @flow would be saving the result python object.

    The function checks whether the result file exists and if it does the @task or @flow will not run but 
    grab the reuslt object from the file and return it instead.

Args:
    task_context, task_parameters (requires The @task or @flow to include a result_file_path attribute)

Returns:
    str:file hash
    """
    
    # Check if the result file exists
    if os.path.exists(task_parameters["result_file_path"]):
        # Compute the hash of the result file
        with open(task_parameters["result_file_path"], 'rb') as f:
            file_hash = hashlib.md5(f.read()).hexdigest()
            
        # Return the hash as the cache key
        return file_hash
    
    # Return None if the result file does not exist
    return None