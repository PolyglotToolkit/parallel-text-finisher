from typing import Any

from configs import ConfigHandler
from parallel_text_finisher.common.data.data_reader import read_data


class ParallelText:
    """ """

    def __init__(self, config_yaml, data_dir):
        self.config = ConfigHandler(config_yaml)
        self.data = read_data(data_dir)

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass
