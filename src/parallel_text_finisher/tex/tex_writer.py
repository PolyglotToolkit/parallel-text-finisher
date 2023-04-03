from pathlib import Path
from typing import Optional, Tuple

from dynaconf import Dynaconf


class TexWriter:
    def __init__(self, input_file_paths: Tuple[Path, Path]) -> None:
        self.input_file_paths = input_file_paths


class TexWriterBuilder:
    def __init__(self, cfg: Dynaconf) -> None:
        self.cfg = cfg


def get_tex_writer(settings_object):
    ...
