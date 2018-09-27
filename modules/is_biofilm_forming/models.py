"""IsBiofilmForming display models."""

import mongoengine as mdb


class IsBiofilmFormingResult(mdb.EmbeddedDocument):  # pylint: disable=too-few-public-methods
    """IsBiofilmForming embedded result."""

    is_biofilm_forming = mdb.BooleanField()
    citation = mdb.StringField()
