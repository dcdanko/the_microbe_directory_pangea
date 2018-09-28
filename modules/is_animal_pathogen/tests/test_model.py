"""Test suite for IsAnimalPathogen AnalysisModule."""

from unittest import TestCase

from mongoengine import ValidationError

from .factory import IsAnimalPathogenResultFactory
from ..modules import IsAnimalPathogenModule # import this just to make sure no typos in module (not used otherwise)

class TestIsAnimalPathogenModels(TestCase):
    """Test suite for IsAnimalPathogen AnalysisModule."""

    def test_add_is_animal_pathogen(self):
        """Ensure IsAnimalPathogen model is created correctly."""

        is_animal_pathogen_result = IsAnimalPathogenResultFactory()

        try:
            is_animal_pathogen_result.validate()
        except ValidationError:
            self.fail('IsAnimalPathogenResult validation raised unexpected ValidationError.')
