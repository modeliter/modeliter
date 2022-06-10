from .resultstorage import (
    ResultStorage,
    ResultStorageConfig,
)
from .sqliteresultstorage import (
    SQLiteResultStorage,
    SQLiteResultStorageConfig,
)


def build_result_storage(
    *,
    result_storage_config: ResultStorageConfig,
    ) -> ResultStorage:
    config_to_constructor = {
        SQLiteResultStorageConfig: SQLiteResultStorage,
    }
    result_storage_constructor = config_to_constructor[result_storage_config.__class__]
    return result_storage_constructor(result_storage_config)
