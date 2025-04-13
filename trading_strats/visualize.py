"""Visualization module."""
import os
import plotly.express as px


class Visualize:
    """
    Defines different visualization options.
    """
    def __init__(self, input_data, path=os.getcwd()):
        self.input_data = input_data
        self.path = path

    def time_series_plot(self, time_column):
        pass
