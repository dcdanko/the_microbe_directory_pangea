"""OptimalPh display models."""

import mongoengine as mdb


class OptimalPhResult(mdb.EmbeddedDocument):  # pylint: disable=too-few-public-methods
    """OptimalPh embedded result."""

    optimal_ph = mdb.FloatField()
    citation = mdb.StringField()
