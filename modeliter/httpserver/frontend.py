from os import path
from starlette.staticfiles import StaticFiles

def _relative_path(rel: str) -> str:
    return path.join(path.dirname(__file__), rel)

DIR_PATH = _relative_path("../../modeliter_frontend")
BUILD_PATH = path.join(DIR_PATH, "build")
static_files = StaticFiles(directory=BUILD_PATH, html=True)
