"""Class for technical analysis indicators."""


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
