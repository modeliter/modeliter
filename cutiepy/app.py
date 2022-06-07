@dataclass
class App:
    supervisor: Supervisor
    dashboard_server: DashboardServer

    async def run(self):
        await asyncio.gather(
            self.supervisor.run(),
            self.dashboard_server.run(),
        )
