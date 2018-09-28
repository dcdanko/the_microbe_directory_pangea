"""IsFoundInHumanMicrobiome display models."""

import mongoengine as mdb


class IsFoundInHumanMicrobiomeResult(mdb.EmbeddedDocument):  # pylint: disable=too-few-public-methods
    """IsFoundInHumanMicrobiome embedded result."""

    is_found_in_human_microbiome = mdb.BooleanField()
    citation = mdb.StringField()
