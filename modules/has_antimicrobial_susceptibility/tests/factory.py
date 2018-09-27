# pylint: disable=missing-docstring,too-few-public-methods

"""Factory for generating HasAntimicrobialSusceptibility models for testing."""

from random import choice

import factory

from ..models import HasAntimicrobialSusceptibilityResult


class HasAntimicrobialSusceptibilityResultFactory(factory.mongoengine.MongoEngineFactory):
    """Factory for HasAntimicrobialSusceptibilityResult."""
    class Meta:
        """Factory metadata."""
        model = HasAntimicrobialSusceptibilityResult

    citation = 'my citation 2018'

    @factory.lazy_attribute
    def has_antimicrobial_susceptibility(self):  # pylint: disable=no-self-use
        """Generate random samples."""
        return choice([True, False])
