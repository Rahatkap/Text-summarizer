import sys
from pathlib import Path

# Assuming your notebook is located in 'Text-summarizer/research'
current_dir = Path.cwd()  # Get the current working directory of the notebook
project_dir = current_dir.parent.parent  # Go up two levels to reach 'Text-summarizer'

# Add 'src' directory to sys.path
src_dir = project_dir / 'src'
sys.path.insert(0, str(src_dir))

from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories
from textSummarizer.entity import (DataIngestionConfig,
                                   )


class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    
