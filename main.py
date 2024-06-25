import sys
from pathlib import Path

# Get the current file's directory
current_dir = Path(__file__).resolve().parent

# Add the src directory to sys.path
src_dir = current_dir / 'src'
sys.path.insert(0, str(src_dir))

# Now you can import from your package
from textSummarizer.pipeline.stage1 import DataIngestionTrainingPipeline
from textSummarizer.logging import logger

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

