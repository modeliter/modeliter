from pathlib import Path
from typing import Tuple
from cutiepy.brokers import SQLiteBrokerConfig
from cutiepy.resultstorages import SQLiteResultStorageConfig
from cutiepy.modes import Mode
from cutiepy.workers import WorkerConfig


CONFIG_MODULE_NAME = "cutieconfig"
HOME_CONFIG_PATH = Path(Path.home() / ".cutiepy").resolve()
CWD_CONFIG_PATH = Path(".cutiepy").resolve()


def build_default_mode_dict():
    return {
        "default": Mode(
            broker=SQLiteBrokerConfig(
                path="./broker.sqlite",
            ),
            result_storage=SQLiteResultStorageConfig(
                path="./.cutiepy/default/resultstorage.sqlite",
            ),
            workers=[WorkerConfig(), WorkerConfig()],
        ),
        "dev": Mode(
            broker=SQLiteBrokerConfig(
                path="./broker.sqlite",
            ),
            result_storage=SQLiteResultStorageConfig(
                path="./.cutiepy/dev/resultstorage.sqlite",
            ),
            workers=[WorkerConfig(), WorkerConfig()],
        ),
    }


def load_modes_from_config_file() -> dict[str, Mode]:
    try:
        import cutieconfig
    except ModuleNotFoundError:
        return build_default_mode_dict()

    attr_names: list[str] = dir(cutieconfig)
    attrs: list = map(lambda attr: getattr(cutieconfig, attr), attr_names)
    attr_tuples: Tuple[str, any] = zip(attr_names, attrs)
    mode_tuples: Tuple[str, Mode] = filter(lambda attr: isinstance(attr[1], Mode), attr_tuples)
    return dict(mode_tuples)