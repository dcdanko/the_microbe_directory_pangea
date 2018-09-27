"""IsPlantPathogen display models."""

import mongoengine as mdb


class IsPlantPathogenResult(mdb.EmbeddedDocument):  # pylint: disable=too-few-public-methods
    """IsPlantPathogen embedded result."""

    is_plant_pathogen = mdb.BooleanField()
    citation = mdb.StringField()
