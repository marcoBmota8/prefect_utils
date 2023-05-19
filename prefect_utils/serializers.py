import pickle
from typing import TypeVar, Any
from typing_extensions import Literal
import base64
from prefect.serializers import Serializer

D = TypeVar("D")

class CustomPickleSerializer(Serializer):
    """
    Custom serializer for pickle files compatible with both
    the `pickle` package and `pandas.read_pickle`.
    """

    type: Literal["CustomPickle"] = "CustomPickle"
        

    def dumps(self, obj: Any) -> bytes:
        """Encode the object into a blob of bytes."""
        blob = pickle.dumps(obj, protocol=pickle.HIGHEST_PROTOCOL)
        return base64.encodebytes(blob)
    
    def loads(self, blob: bytes) -> Any:
        """Decode the blob of bytes into an object."""
        return pickle.loads(base64.decodebytes(blob))