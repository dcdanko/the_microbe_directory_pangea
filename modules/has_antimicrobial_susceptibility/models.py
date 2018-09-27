"""HasAntimicrobialSusceptibility display models."""

import mongoengine as mdb


class HasAntimicrobialSusceptibilityResult(mdb.EmbeddedDocument):  # pylint: disable=too-few-public-methods
    """HasAntimicrobialSusceptibility embedded result."""

    has_antimicrobial_susceptibility = mdb.BooleanField()
    citation = mdb.StringField()
