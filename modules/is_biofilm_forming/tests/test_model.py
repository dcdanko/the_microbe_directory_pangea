"""Test suite for IsBiofilmForming AnalysisModule."""

from unittest import TestCase

from mongoengine import ValidationError

from .factory import IsBiofilmFormingResultFactory
from ..modules import IsBiofilmFormingModule # import this just to make sure no typos in module (not used otherwise)

class TestIsBiofilmFormingModels(TestCase):
    """Test suite for IsBiofilmForming AnalysisModule."""

    def test_add_is_animal_pathogen(self):
        """Ensure IsBiofilmForming model is created correctly."""

        is_biofilm_forming_result = IsBiofilmFormingResultFactory()

        try:
            is_biofilm_forming_result.validate()
        except ValidationError:
            self.fail('IsBiofilmFormingResult validation raised unexpected ValidationError.')
