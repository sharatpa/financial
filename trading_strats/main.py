import logging

from data_processor import DataProcessor

dp = DataProcessor("standard")
try:
    dt = dp.get_data()
except:
    logging.error("Could not fetch data.")