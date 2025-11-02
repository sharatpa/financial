"""Class for technical analysis indicators."""
import logging
from datetime import timedelta

import pandas as pd

class Indicators():
    """Defines indicators."""

    def __init__(self):
        return None

    def macd(self, tag):
        """Moving average convergence divergence. Difference between 12
        period EMA and 26 period EMA.
        Input: tag (df column) representing the close value.
        Output: MACD."""
        exp1 = tag.ewm(span=12, adjust=False).mean()
        exp2 = tag.ewm(span=26, adjust=False).mean()
        macd = exp1 - exp2
        signal_line = macd.ewm(span=9, adjust=False).mean()
        return macd, signal_line

    def parabolic_sar(self, tag, max_af=0.2):
        """Parabolic Stop and Reverse. It is used to find potential
        reversals in market price directions.
        If SAR is above current market price, it suggests a downtrend.
        If SAR is below current market price, it suggests an uptrend.
        There are two PSARs - rising and falling. This indicator
        requires traversing the dataframe.
        
        tag is a DF that has open, close, high and low prices.
        At least two weeks of data is needed.
        """
        # PSAR's effectiveness is weak in the absence of strong trends.
        if len(tag) < 100:
            logging.info("Data too small to compute PSAR.")
            return None
        if (tag.at[-1, "Time"] - tag.at[0,"Time"]) < timedelta(weeks=2):
            logging.info("Less than two weeks of data provided. "
             "Can't compute SAR.")
            return None
        # Check if tag is trending upward or downward first
        # using two weeks of data (more the better I suppose).
        len_df = tag.shape[0]
        period_1_close_avg = tag["Close"].iloc[[0, len_df/3]].mean()
        period_2_close_avg = tag["Close"].iloc[[len_df/3, 2*len_df/3]].mean()
        prev_trend = "Down"
        if period_2_close_avg >= period_1_close_avg:
            prev_trend = "Up"
        # Now iterate through the rest of the DF to calculate PSAR.
        tag["PSAR"] = 0
        tag.loc[0, "AF"] = 0.02
        return tag