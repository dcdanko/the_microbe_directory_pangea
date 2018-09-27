"""IsSporeForming display models."""

import mongoengine as mdb


class IsSporeFormingResult(mdb.EmbeddedDocument):  # pylint: disable=too-few-public-methods
    """IsSporeForming embedded result."""

    is_spore_forming = mdb.BooleanField()
    citation = mdb.StringField()
