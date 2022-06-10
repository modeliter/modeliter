import time
from cutiepy import CutiePy

cutie = CutiePy(mode="dev")

@cutie.task
def bake_a_pie(flavor, recipient):
    time.sleep(3)
    print(f"Your {flavor} pie for {recipient} is ready!")

# highlight-next-line-green
cutie.enqueue(bake_a_pie, args=["apple", "Alice"])
