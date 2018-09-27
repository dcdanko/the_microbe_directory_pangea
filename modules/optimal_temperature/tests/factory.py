# pylint: disable=missing-docstring,too-few-public-methods

"""Factory for generating OptimalTemperature models for testing."""

from random import random

import factory

from ..models import OptimalTemperatureResult


class OptimalTemperatureResultFactory(factory.mongoengine.MongoEngineFactory):
    """Factory for OptimalTemperatureResult."""
    class Meta:
        """Factory metadata."""
        model = OptimalTemperatureResult

    citation = 'my citation 2018'

    @factory.lazy_attribute
    def optimal_temperature(self):  # pylint: disable=no-self-use
        """Generate random samples."""
        return random() * 200
