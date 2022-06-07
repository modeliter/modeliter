async def main():
    broker_config = BrokerConfig()
    broker = Broker(
        broker_config=broker_config,
    )

    supervisor_config = SupervisorConfig()
    supervisor = Supervisor(
        supervisor_config=supervisor_config,
        broker=broker,
    )

    dashboard_server_config = DashboardServerConfig()
    dashboard_server = DashboardServer(
        dashboard_server_config=dashboard_server_config,
        broker=broker,
        supervisor=supervisor,
    )

    app = App(
        supervisor=supervisor,
        dashboard_server=dashboard_server,
    )

    await app.run()


if __name__ == "__main__":
    asyncio.run(main())
