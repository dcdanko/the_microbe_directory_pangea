# pylint: disable=missing-docstring,too-few-public-methods

"""Factory for generating GramStain models for testing."""

from random import choice

import factory

from ..models import GramStainResult


class GramStainResultFactory(factory.mongoengine.MongoEngineFactory):
    """Factory for GramStainResult."""
    class Meta:
        """Factory metadata."""
        model = GramStainResult

    citation = 'my citation 2018'

    @factory.lazy_attribute
    def gram_stain(self):  # pylint: disable=no-self-use
        """Generate random samples."""
        return choice(['positive', 'negative', 'indeterminate'])
