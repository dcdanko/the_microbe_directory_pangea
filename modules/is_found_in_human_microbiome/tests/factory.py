# pylint: disable=missing-docstring,too-few-public-methods

"""Factory for generating IsFoundInHumanMicrobiome models for testing."""

from random import choice

import factory

from ..models import IsFoundInHumanMicrobiomeResult


class IsFoundInHumanMicrobiomeResultFactory(factory.mongoengine.MongoEngineFactory):
    """Factory for IsFoundInHumanMicrobiomeResult."""
    class Meta:
        """Factory metadata."""
        model = IsFoundInHumanMicrobiomeResult

    citation = 'my citation 2018'

    @factory.lazy_attribute
    def is_found_in_human_microbiome(self):  # pylint: disable=no-self-use
        """Generate random samples."""
        return choice([True, False])
