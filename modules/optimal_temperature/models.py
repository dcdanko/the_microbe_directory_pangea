"""OptimalTemperature display models."""

import mongoengine as mdb


class OptimalTemperatureResult(mdb.EmbeddedDocument):  # pylint: disable=too-few-public-methods
    """OptimalTemperature embedded result."""

    optimal_temperature = mdb.FloatField()
    citation = mdb.StringField()
