# pylint: disable=missing-docstring,too-few-public-methods

"""Factory for generating IsBiofilmForming models for testing."""

from random import choice

import factory

from ..models import IsBiofilmFormingResult


class IsBiofilmFormingResultFactory(factory.mongoengine.MongoEngineFactory):
    """Factory for IsBiofilmFormingResult."""
    class Meta:
        """Factory metadata."""
        model = IsBiofilmFormingResult

    citation = 'my citation 2018'

    @factory.lazy_attribute
    def is_biofilm_forming(self):  # pylint: disable=no-self-use
        """Generate random samples."""
        return choice([True, False])
