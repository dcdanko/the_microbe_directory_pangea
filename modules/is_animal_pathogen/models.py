"""IsAnimalPathogen display models."""

import mongoengine as mdb


class IsAnimalPathogenResult(mdb.EmbeddedDocument):  # pylint: disable=too-few-public-methods
    """IsAnimalPathogen embedded result."""

    is_animal_pathogen = mdb.BooleanField()
    citation = mdb.StringField()
