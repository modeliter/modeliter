import time
import uuid
import pydantic
import pickle

data = [b"b" * (2 ** 10)]

def a():
    time.sleep(100)
    print(data)

def b():
    a()
    uuid.uuid4()

def c():
    b()
    pydantic.BaseClass()


print(len(str(pickle.dumps(a))))
print(len(str(pickle.dumps(b))))
print(len(str(pickle.dumps(c))))
print(len(pickle.dumps(data)))
a(b=10)
