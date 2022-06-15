from ast import Assert
from collections import namedtuple
import cutiepy.serde as serde
from dataclasses import dataclass

@dataclass
class _ModuleLevelClass:
    pass

def _module_level_function():
    pass


def test_serde():
    TestCase = namedtuple("TestCase", ["name", "object"])

    test_cases = [
        TestCase(
            name="none",
            object=None,
        ),
        TestCase(
            name="int",
            object=1,
        ),
        TestCase(
            name="float",
            object=-1.1,
        ),
        TestCase(
            name="bool",
            object=True,
        ),
        TestCase(
            name="str",
            object="Hello, World!",
        ),
        TestCase(
            name="tuple",
            object=("Hello", "World!"),
        ),
        TestCase(
            name="list",
            object=["Hello", "World!"],
        ),
        TestCase(
            name="dict",
            object={"Hello": "World!"},
        ),
        TestCase(
            name="set",
            object=set(["Hello", "World!"]),
        ),
        TestCase(
            name="module level function",
            object=_module_level_function,
        ),
        TestCase(
            name="module level class definition",
            object=_ModuleLevelClass,
        ),
        TestCase(
            name="module class instance (dataclass)",
            object=_ModuleLevelClass(),
        ),
    ]

    roundtrip = lambda x: serde.deserialize(serde.serialize(x))
    for test_case in test_cases:
        try:
            if test_case.object != roundtrip(test_case.object):
                raise AssertionError(f"Roundtripped {test_case.name} was not the same.")
        except Exception as exc:
            raise AssertionError(f"Failed to serialize or deserialize {test_case.name}: {exc}")
