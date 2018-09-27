# pylint: disable=missing-docstring,too-few-public-methods

"""Factory for generating IsAnimalPathogen models for testing."""

from random import choice

import factory

from ..models import IsAnimalPathogenResult


class IsAnimalPathogenResultFactory(factory.mongoengine.MongoEngineFactory):
    """Factory for IsAnimalPathogenResult."""
    class Meta:
        """Factory metadata."""
        model = IsAnimalPathogenResult

    citation = 'my citation 2018'

    @factory.lazy_attribute
    def is_animal_pathogen(self):  # pylint: disable=no-self-use
        """Generate random samples."""
        return choice([True, False])
