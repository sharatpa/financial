"""Deals with data ingestion or reading."""
import os
import pandas as pd
import numpy as np
import plotly.express as px
import yfinance as yf


class DataProcessor:
    """
    Helps pass data onto other modules.
    Whether it's a csv of yfinance API.
    """
    def __init__(self, type_of_data):
        self.type_of_data = type_of_data

    def get_data(self):
        """
        Fetches data as per type.
        """
        if self.type_of_data == "standard_api":
            nifty_df = yf.download("^NSEI")
