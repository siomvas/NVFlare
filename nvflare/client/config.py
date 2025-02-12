# Copyright (c) 2023, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Dict

from .constants import ModelExchangeFormat


class ConfigKey:
    EXCHANGE_PATH = "exchange_path"
    EXCHANGE_FORMAT = "exchange_format"
    TRANSFER_TYPE = "transfer_type"


class ClientConfig:
    """Config class used in nvflare.client module.

    Example:
        {
            "exchange_path": "./",
            "exchange_format": "pytorch",
            "transfer_type": "FULL"
        }
    """

    def __init__(self, config: Dict):
        for required_key in (ConfigKey.EXCHANGE_PATH, ConfigKey.EXCHANGE_FORMAT):
            if required_key not in config:
                raise RuntimeError(f"Missing required_key: {required_key} in config.")

        config[ConfigKey.EXCHANGE_FORMAT] = ModelExchangeFormat(config[ConfigKey.EXCHANGE_FORMAT])
        self.config = config

    def get_config(self):
        return self.config

    def get_exchange_path(self):
        return self.config[ConfigKey.EXCHANGE_PATH]

    def get_exchange_format(self) -> ModelExchangeFormat:
        return self.config[ConfigKey.EXCHANGE_FORMAT]

    def get_transfer_type(self):
        return self.config[ConfigKey.TRANSFER_TYPE]
