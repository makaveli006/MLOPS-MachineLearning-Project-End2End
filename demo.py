
# # #### logger submodule testing in demo.py ####
# from us_visa.logger import logging
# # logging.info("Demo file executed")

# ###### exception submodule testing in demo.py ####
# from us_visa.exception import USvisaException
# import sys

# try:
#     a = 1 / 0
# except Exception as e:
#     raise USvisaException(e, sys)
# import os

# print(os.getenv("MONGODB_URL"))

from us_visa.pipline.training_pipeline import TrainPipeline

obj = TrainPipeline()
obj.run_pipeline()