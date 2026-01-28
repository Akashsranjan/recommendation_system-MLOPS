import os
import pandas as pd
from google.cloud import storage
from src.logger import get_logger
from src.custom_exception import CustomException
from config.path_config import *
from utils.common_functions import read_yaml
import sys


logger = get_logger(__name__)

class Dataingestion:
    def __init__(self, config):
        self.config = config["data_ingestion"]
        self.bucket_name = self.config["bucket_name"]
        self.file_name = self.config["bucket_file_name"]

        os.makedirs(RAW_DIR, exist_ok=True)

        logger.info(f"Data Ingestion Started...")
    
    def download_csv_from_gcp(self):
        try:
            client = storage.Client()
            bucket = client.bucket(self.bucket_name)

            for file_name in self.file_name:
                file_path = os.path.join(RAW_DIR,file_name)

                if file_name =="animelist.csv":
                    blob = bucket.blob(file_name)
                    blob.download_to_filename(file_path)

                    data = pd.read_csv(file_path,nrows=5000000)
                    data.to_csv(file_path,index=False)
                    logger.info("Large file detected only download 5m")
                
                else:
                    blob = bucket.blob(file_name)
                    blob.download_to_filename(file_path)

                    logger.info("downloading smaller file ie anime and anime with synopsis")

        except Exception as e:
            logger.error(f"GCP DOWNLOAD ERROR → {e}", exc_info=True)
            raise CustomException("failed to download data", e)

        


    def run(self):
        """Run the ingestion workflow"""
        try:
            logger.info("Starting data ingestion process...")
            self.download_csv_from_gcp()
            logger.info("Data ingestion completed successfully!")
        except CustomException as ce:
            logger.error(f"CustomException: {str(ce)}")
        finally:
            logger.info("Data ingestion process finished.")


if __name__ == "__main__":
    config = read_yaml(CONFIG_PATH)
    data_ingestion = Dataingestion(config)
    data_ingestion.run()