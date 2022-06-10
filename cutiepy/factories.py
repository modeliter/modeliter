from cutiepy.brokers import InProcessBroker
from cutiepy.core import (
    App,
    Broker,
    BrokerConfig,
)


def build_app(
    *,
    broker: Broker,
    ) -> App:
    return App(
        broker=broker,
    )

def build_broker(*, broker_config: BrokerConfig) -> Broker:
    broker_type_to_class = {
        "sqlite": InProcessBroker,
    }
    broker_constructor = broker_type_to_class[broker_config.type]
    return broker_constructor(broker_config=broker_config)
