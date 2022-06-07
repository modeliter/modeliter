from . import *

app: App = App()

@app.task
@app.retries(max_retries=3)
@app.timeout(timeout_seconds=60)
def long_running_function(arg1, arg2):
    time.sleep(10)
    return 10



# Call normally
long_running_function(1, 2)     # 10

# Enqueue task
run: Run = long_running_function.run(1, 2)


