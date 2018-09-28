# pylint: disable=missing-docstring,too-few-public-methods

"""Factory for generating HasExtremeEnvironment models for testing."""

from random import choice

import factory

from ..models import HasExtremeEnvironmentResult


class HasExtremeEnvironmentResultFactory(factory.mongoengine.MongoEngineFactory):
    """Factory for HasExtremeEnvironmentResult."""
    class Meta:
        """Factory metadata."""
        model = HasExtremeEnvironmentResult

    citation = 'my citation 2018'

    @factory.lazy_attribute
    def has_extreme_environment(self):  # pylint: disable=no-self-use
        """Generate random samples."""
        return choice([True, False])
