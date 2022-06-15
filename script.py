import pickle
import pickletools
import base64
import json
def f():
    print("Hello, World!")

f_pickled = pickle.dumps(f)
f_pickled_encoded = base64.b85encode(f_pickled).decode()
print(type(f_pickled_encoded))
print(f_pickled_encoded)

def to_pickled_b85(obj: any) -> str:
    obj_pickled: bytes = pickle.dumps(obj)
    obj_pickled_b85: bytes = base64.b85encode(obj_pickled)
    return obj_pickled_b85.decode()

def from_pickled_b85(obj_pickled_b85: str) -> any:
    obj_pickled: bytes = base64.b85decode(obj_pickled_b85)
    return pickle.loads(obj_pickled)

assert(from_pickled_b85(to_pickled_b85(f)) is f)
