import logging

from data_processor import DataProcessor

dp = DataProcessor("standard")
try:
    dt = dp.get_data()
except Exception as e:
    logging.error("Could not fetch data.")
    logging.error(e)
