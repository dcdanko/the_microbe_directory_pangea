# pylint: disable=missing-docstring,too-few-public-methods

"""Factory for generating IsPlantPathogen models for testing."""

from random import choice

import factory

from ..models import IsPlantPathogenResult


class IsPlantPathogenResultFactory(factory.mongoengine.MongoEngineFactory):
    """Factory for IsPlantPathogenResult."""
    class Meta:
        """Factory metadata."""
        model = IsPlantPathogenResult

    citation = 'my citation 2018'

    @factory.lazy_attribute
    def is_plant_pathogen(self):  # pylint: disable=no-self-use
        """Generate random samples."""
        return choice([True, False])
