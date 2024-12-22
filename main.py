from hate_spch_clsf.logger import logging
from hate_spch_clsf.exception import CustomException
import sys


logging.info("Hii Aski !")

try:
    a = 7 /" 0"

except Exception as e:
    raise CustomException(e , sys) from e


