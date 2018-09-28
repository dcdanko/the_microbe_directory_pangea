"""GramStain display models."""

import mongoengine as mdb


class GramStainResult(mdb.EmbeddedDocument):  # pylint: disable=too-few-public-methods
    """GramStain embedded result."""

    gram_stain = mdb.StringField()
    citation = mdb.StringField()
