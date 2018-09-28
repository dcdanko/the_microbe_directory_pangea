"""Test suite for IsFoundInHumanMicrobiome AnalysisModule."""

from unittest import TestCase

from mongoengine import ValidationError

from .factory import IsFoundInHumanMicrobiomeResultFactory
from ..modules import IsFoundInHumanMicrobiomeModule # import this just to make sure no typos in module (not used otherwise)

class TestIsFoundInHumanMicrobiomeModels(TestCase):
    """Test suite for IsFoundInHumanMicrobiome AnalysisModule."""

    def test_add_is_animal_pathogen(self):
        """Ensure IsFoundInHumanMicrobiome model is created correctly."""

        is_found_in_human_microbiome_result = IsFoundInHumanMicrobiomeResultFactory()

        try:
            is_found_in_human_microbiome_result.validate()
        except ValidationError:
            self.fail('IsFoundInHumanMicrobiomeResult validation raised unexpected ValidationError.')
