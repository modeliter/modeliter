import asyncio
from cutiepy import factories
from cutiepy.core import (
    BrokerConfig,
    DashboardServerConfig,
    SupervisorConfig,
)


async def main():
    broker_config = BrokerConfig()
    broker = factories.build_broker(broker_config=broker_config)

    supervisor_config = SupervisorConfig()
    supervisor = factories.build_supervisor(
        supervisor_config=supervisor_config,
        broker=broker,
    )

    app = factories.build_app(
        broker=broker,
        supervisor=supervisor,
    )

    await app.start()


if __name__ == "__main__":
    asyncio.run(main())
