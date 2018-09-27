"""ExtremeEnvironment display models."""

import mongoengine as mdb


class HasExtremeEnvironmentResult(mdb.EmbeddedDocument):  # pylint: disable=too-few-public-methods
    """HasExtremeEnvironment embedded result."""

    has_extreme_environment = mdb.BooleanField()
    citation = mdb.StringField()
