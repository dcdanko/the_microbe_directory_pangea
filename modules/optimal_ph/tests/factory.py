# pylint: disable=missing-docstring,too-few-public-methods

"""Factory for generating OptimalPh models for testing."""

from random import random

import factory

from ..models import OptimalPhResult


class OptimalPhResultFactory(factory.mongoengine.MongoEngineFactory):
    """Factory for OptimalPhResult."""
    class Meta:
        """Factory metadata."""
        model = OptimalPhResult

    citation = 'my citation 2018'

    @factory.lazy_attribute
    def optimal_ph(self):  # pylint: disable=no-self-use
        """Generate random samples."""
        return random() * 14
