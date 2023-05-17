import os
import hashlib
def cache_file_based_fn(task_context,task_parameters):
    # Check if the result file exists
    if os.path.exists(task_parameters["result_file_path"]):
        # Compute the hash of the result file
        with open(task_parameters["result_file_path"], 'rb') as f:
            file_hash = hashlib.md5(f.read()).hexdigest()
            
        # Return the hash as the cache key
        return file_hash
    
    # Return None if the result file does not exist
    return None