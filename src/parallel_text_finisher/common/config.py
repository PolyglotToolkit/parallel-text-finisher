from pathlib import Path

from .locations import Locations


class ConfigHandler:
    def __init__(self, locations_class) -> None:
        self.locations = Locations()
        self.package_root = self.src_path.parent
        self.config = self.src_path / "configs" / "config.yaml"
