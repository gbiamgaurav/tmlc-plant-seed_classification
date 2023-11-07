
from plant_seed import logger
from plant_seed.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from plant_seed.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from plant_seed.pipeline.stage_03_training import ModelTrainingPipeline
from plant_seed.pipeline.stage_04_evaluation import ModelEvaluationPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
   logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Prepare Base Model Stage"
try:
    logger.info(f"Stage: {STAGE_NAME} Started!")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f"Stage: {STAGE_NAME} Completed!")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Training Stage"
try:
    logger.info(f"Stage: {STAGE_NAME} Started!")
    model_training = ModelTrainingPipeline()
    model_training.main()
    logger.info(f"Stage: {STAGE_NAME} Completed!")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f"Stage: {STAGE_NAME} Started!")
    model_training = ModelEvaluationPipeline()
    model_training.main()
    logger.info(f"Stage: {STAGE_NAME} Completed!")
except Exception as e:
    logger.exception(e)
    raise e