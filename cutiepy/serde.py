import base64
import pickle

def serialize(obj: any) -> str:
    obj_pickled: bytes = pickle.dumps(obj)
    obj_pickled_b85: bytes = base64.b85encode(obj_pickled)
    return obj_pickled_b85.decode()

def deserialize(s: str) -> any:
    obj_pickled: bytes = base64.b85decode(s)
    return pickle.loads(obj_pickled)
