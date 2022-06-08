from cutiepy.brokers import InProcessBroker
from cutiepy.core import (
    App,
    Broker,
    BrokerConfig,
    DashboardServer,
    DashboardServerConfig,
    Supervisor,
    SupervisorConfig,
    Worker,
    WorkerConfig,
)
from cutiepy.dashboardservers import InProcessDashboardServer
from cutiepy.supervisors import InProcessSupervisor
from cutiepy.workers import InProcessWorker


def build_app(
    *,
    broker: Broker,
    supervisor: Supervisor,
    dashboard_server: DashboardServer,
    ) -> App:
    return App(
        broker=broker,
        supervisor=supervisor,
        dashboard_server=dashboard_server,
    )


def build_broker(*, broker_config: BrokerConfig) -> Broker:
    broker_type_to_class = {
        "inprocess": InProcessBroker,
    }
    broker_constructor = broker_type_to_class[broker_config.type]
    return broker_constructor(broker_config=broker_config)


def build_dashboard_server(
    *,
    dashboard_server_config: DashboardServerConfig,
    broker: Broker,
    supervisor: Supervisor,
    ) -> DashboardServer:

    dashboard_server_type_to_class = {
        "inprocess": InProcessDashboardServer,
    }
    dashboard_server_constructor = dashboard_server_type_to_class[dashboard_server_config.type]
    return dashboard_server_constructor(
        dashboard_server_config=dashboard_server_config,
        broker=broker,
        supervisor=supervisor,
    )
    

def build_supervisor(
    *,
    supervisor_config: SupervisorConfig,
    broker: Broker,
    ) -> Supervisor:
    supervisor_type_to_class = {
        "inprocess": InProcessSupervisor,
    }
    supervisor_constructor = supervisor_type_to_class[supervisor_config.type]
    return supervisor_constructor(
        supervisor_config=supervisor_config,
        broker=broker,
    )


def build_worker(*, worker_config: WorkerConfig, broker: Broker) -> Worker:
    worker_type_to_class = {
        "inprocess": InProcessWorker,
    }
    worker_constructor = worker_type_to_class[worker_config.type]
    return worker_constructor(worker_config=worker_config, broker=broker)

