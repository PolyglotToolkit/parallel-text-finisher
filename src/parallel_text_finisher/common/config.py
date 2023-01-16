from pathlib import Path


class ConfigHandler:
    def __init__(self) -> None:
        self.src_path = Path(__file__).parent.parent
        self.package_root = self.src_path.parent
        self.config = self.src_path / "configs" / "config.yaml"
