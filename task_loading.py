from functools import reduce
import p
import importlib
import logging

f = logging.warning
f_name = f.__module__ + "." + f.__qualname__
# Save f_name to broker.
# Get f_name from broker.
f_name_parts = f_name.split(sep=".")
f_module = importlib.import_module(f_name_parts[0])
f_func = reduce(lambda obj, attr: getattr(obj, attr), f_name_parts[1:], f_module)
f_func("Hello")
