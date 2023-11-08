from plant_seed.config.configuration import ConfigurationManager
from plant_seed.components.evaluation import Evaluation
from plant_seed import logger

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            eval_config = config.get_evaluation_config()
            evaluation = Evaluation(eval_config)
            evaluation.evaluation()
            evaluation.save_score()
            evaluation.log_into_mlflow()
        except Exception as e:
            logger.error(f"Error during model evaluation: {e}")
            raise e

if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f"Stage {STAGE_NAME} started")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f"Stage {STAGE_NAME} completed")
    except Exception as e:
        logger.exception(f"An error occurred in {STAGE_NAME}: {e}")
        raise e
