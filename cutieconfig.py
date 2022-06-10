from cutiepy.config import Mode, BrokerConfig, ResultStorageConfig, WorkerConfig

dummy = Mode(
    broker=BrokerConfig(
        type="sqlite",
        path="./default.sqlite",
    ),
    result_storage=ResultStorageConfig(
        type="sqlite",
        path="./default.sqlite",
    ),
    workers=2 * [
        WorkerConfig(
            capabilities={"gpu": True},
            preferences={"type": "thread"},
        )
    ],
)

a = 10
b = BrokerConfig(type="sqlite", path="./default.sqlite")
c = ["hello"] * a
