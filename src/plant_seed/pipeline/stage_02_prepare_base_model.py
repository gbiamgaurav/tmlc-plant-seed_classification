
from plant_seed import logger
from plant_seed.config.configuration import ConfigurationManager
from plant_seed.components.prepare_base_model import PrepareBaseModel


STAGE_NAME = "Prepare Base Model Stage"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass 


    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.updated_base_model()


if __name__ == "__main__":
    try:
        logger.info(f"Stage: {STAGE_NAME} Started")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f"Stage: {STAGE_NAME} Completed")
    except Exception as e:
        logger.exception(e)
        raise e