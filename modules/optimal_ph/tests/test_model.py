"""Test suite for OptimalPh AnalysisModule."""

from unittest import TestCase

from mongoengine import ValidationError

from .factory import OptimalPhResultFactory
from ..modules import OptimalPhModule # import this just to make sure no typos in module (not used otherwise)

class TestOptimalPhModels(TestCase):
    """Test suite for OptimalPh AnalysisModule."""

    def test_add_is_animal_pathogen(self):
        """Ensure OptimalPh model is created correctly."""

        optimal_ph_result = OptimalPhResultFactory()

        try:
            optimal_ph_result.validate()
        except ValidationError:
            self.fail('OptimalPhResult validation raised unexpected ValidationError.')
