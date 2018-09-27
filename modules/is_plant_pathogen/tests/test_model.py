"""Test suite for IsPlantPathogen AnalysisModule."""

from unittest import TestCase

from mongoengine import ValidationError

from .factory import IsPlantPathogenResultFactory
from ..modules import IsPlantPathogenModule # import this just to make sure no typos in module (not used otherwise)

class TestIsPlantPathogenModels(TestCase):
    """Test suite for IsPlantPathogen AnalysisModule."""

    def test_add_is_plant_pathogen(self):
        """Ensure IsPlantPathogen model is created correctly."""

        is_plant_pathogen_result = IsPlantPathogenResultFactory()

        try:
            is_plant_pathogen_result.validate()
        except ValidationError:
            self.fail('IsPlantPathogenResult validation raised unexpected ValidationError.')
