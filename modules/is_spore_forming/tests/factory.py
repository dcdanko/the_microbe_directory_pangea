# pylint: disable=missing-docstring,too-few-public-methods

"""Factory for generating IsSporeForming models for testing."""

from random import choice

import factory

from ..models import IsSporeFormingResult


class IsSporeFormingResultFactory(factory.mongoengine.MongoEngineFactory):
    """Factory for IsSporeFormingResult."""
    class Meta:
        """Factory metadata."""
        model = IsSporeFormingResult

    citation = 'my citation 2018'

    @factory.lazy_attribute
    def is_spore_forming(self):  # pylint: disable=no-self-use
        """Generate random samples."""
        return choice([True, False])
