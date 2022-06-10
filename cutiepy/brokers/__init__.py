from .broker import (
    Broker,
    BrokerConfig,
)
from .sqlitebroker import (
    SQLiteBroker,
    SQLiteBrokerConfig,
)


def build_broker(*, broker_config: BrokerConfig) -> Broker:
    config_to_constructor = {
        SQLiteBrokerConfig: SQLiteBroker,
    }
    broker_constructor = config_to_constructor[broker_config.__class__]
    return broker_constructor(broker_config=broker_config)
