"""Test suite for IsSporeForming AnalysisModule."""

from unittest import TestCase

from mongoengine import ValidationError

from .factory import IsSporeFormingResultFactory
from ..modules import IsSporeFormingModule # import this just to make sure no typos in module (not used otherwise)

class TestIsSporeFormingModels(TestCase):
    """Test suite for IsSporeForming AnalysisModule."""

    def test_add_is_animal_pathogen(self):
        """Ensure IsSporeForming model is created correctly."""

        is_spore_forming_result = IsSporeFormingResultFactory()

        try:
            is_spore_forming_result.validate()
        except ValidationError:
            self.fail('IsSporeFormingResult validation raised unexpected ValidationError.')
