"""CogemPathogenicity display models."""

import mongoengine as mdb


class CogemPathogenicityResult(mdb.EmbeddedDocument):  # pylint: disable=too-few-public-methods
    """CogemPathogenicity Score embedded result."""

    cogem_pathogenicity = mdb.IntField()
    citation = mdb.StringField()
