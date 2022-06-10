from importlib import import_module
from pathlib import Path
from cutiepy.config import Mode, BrokerConfig, ResultStorageConfig, WorkerConfig
from typing import Tuple

CONFIG_MODULE_NAME = "cutieconfig"
HOME_CONFIG_PATH = Path(Path.home() / ".cutiepy").resolve()
CWD_CONFIG_PATH = Path(".cutiepy").resolve()

DEFAULT_MODE_DICT = {
    "default": Mode(
        broker=BrokerConfig(
            type="sqlite",
            path="./.cutiepy/default/broker.sqlite",
        ),
        result_storage=ResultStorageConfig(
            type="sqlite",
            path="./.cutiepy/default/resultstorage.sqlite",
        ),
        workers=2 * [
            WorkerConfig(
                capabilities={"gpu": True},
                preferences={"type": "thread"},
            )
        ],
    ),
    "dev": Mode(
        broker=BrokerConfig(
            type="sqlite",
            path="./.cutiepy/dev/broker.sqlite",
        ),
        result_storage=ResultStorageConfig(
            type="sqlite",
            path="./.cutiepy/dev/resultstorage.sqlite",
        ),
        workers=[WorkerConfig(), WorkerConfig()],
    ),
}

def load_modes_from_config_file() -> dict[str, Mode]:
    try:
        import cutieconfig
    except ModuleNotFoundError:
        return DEFAULT_MODE_DICT

    attr_names: list[str] = dir(cutieconfig)
    attrs: list = map(lambda attr: getattr(cutieconfig, attr), attr_names)
    attr_tuples: Tuple[str, any] = zip(attr_names, attrs)
    mode_tuples: Tuple[str, Mode] = filter(lambda attr: isinstance(attr[1], Mode), attr_tuples)
    return dict(mode_tuples)

print(load_modes_from_config_file())
