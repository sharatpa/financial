"""Deals with data ingestion or reading."""
import os
import pandas as pd
import numpy as np
import yfinance as yf


class DataProcessor:
    """
    Helps pass data onto other modules.
    Whether it's a csv of yfinance API.
    """
    def __init__(self, type_of_data):
        self.type_of_data = type_of_data
        self.data_to_return = None

    def get_data(self):
        """
        Fetches data as per type.
        """
        if self.type_of_data == "standard":
            self.data_to_return = yf.download("^NSEI")
        return self.data_to_return
