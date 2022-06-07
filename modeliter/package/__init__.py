from pathlib import Path
from string import Template
from tempfile import mkdtemp
from typing import Optional

class Package:
    def __init__(
        self,
        *,
        name: Optional[str] = None,
        version: Optional[str] = None,
        description: Optional[str] = None,
    ):
        self.name = name
        self.version = version
        self.description = description
        

    def generate(self, *, path: Optional[str] = None):
        if path is None:
            with mkdtemp() as path:
                self._generate(path)
        else:
            self._generate(path)

    def _generate(self, path: str):
        Path(path).mkdir(parents=True, exist_ok=True)
        template = Template("$name-$version")
        contents = template.safe_substitute(name=self.name, version=self.version)
        
