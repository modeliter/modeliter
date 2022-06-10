from .sqlitebroker import SQLiteBroker

def build_broker(config) -> Broker:
    broker_type_to_class = {
        "sqlite": SQLiteBroker,
    }
    broker_constructor = broker_type_to_class[broker_config.type]
    return broker_constructor(broker_config=broker_config)
