"""Pathogen display models."""

import mongoengine as mdb


class PathogenResult(mdb.EmbeddedDocument):  # pylint: disable=too-few-public-methods
    """Pathogen Score embedded result."""

    cogem_score = mdb.IntField()
    citation = mdb.StringField()
