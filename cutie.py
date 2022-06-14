import time
from cutiepy import CutiePy

cutie = CutiePy()

def bake_a_pie(flavor, recipient):
    time.sleep(3)
    print(f"Your {flavor} pie for {recipient} is ready!")

cutie.enqueue(bake_a_pie, args=["apple", "Alice"])
