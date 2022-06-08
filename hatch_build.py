from hatchling.builders.hooks.plugin.interface import BuildHookInterface
import subprocess


class BuildFrontend(BuildHookInterface):
    PLUGIN_NAME = "build_frontend"
    FRONTEND_DIR_PATH = "cutiepy_dashboard_frontend"

    def initialize(self, version, build_data):
        subprocess.run(
            args=["npm", "run", "build"],
            cwd=self.FRONTEND_DIR_PATH,
            check=True,
        )

        return super().initialize(version, build_data)
