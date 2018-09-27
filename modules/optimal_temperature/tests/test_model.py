"""Test suite for OptimalTemperature AnalysisModule."""

from unittest import TestCase

from mongoengine import ValidationError

from .factory import OptimalTemperatureResultFactory
from ..modules import OptimalTemperatureModule # import this just to make sure no typos in module (not used otherwise)

class TestOptimalTemperatureModels(TestCase):
    """Test suite for OptimalTemperature AnalysisModule."""

    def test_add_is_animal_pathogen(self):
        """Ensure OptimalTemperature model is created correctly."""

        optimal_temperature_result = OptimalTemperatureResultFactory()

        try:
            optimal_temperature_result.validate()
        except ValidationError:
            self.fail('OptimalTemperatureResult validation raised unexpected ValidationError.')
