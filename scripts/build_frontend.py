from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class BuildFrontend(BuildHookInterface):
    PLUGIN_NAME = "build_frontend"

    def initialize(self, version, build_data):
        print("Building frontend...")
        print(f"Build Data: {build_data}")
        return super().initialize(version, build_data)

    def clean(self, version):
        print("Cleaning frontend...")
        return super().clean(version)